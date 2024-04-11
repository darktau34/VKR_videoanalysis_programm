import time
import argparse
import logging
import os
import numpy as np
import cv2 as cv
import pandas as pd
import supervision as sv
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
from videoprocessing import get_video_fps

from moviepy.editor import VideoFileClip
from PIL import Image
from videoprocessing import cut_photobox

logger = logging.getLogger(__name__)


def detect_items(yolo_df, video_path, items_path, to_csv_path, person_arr):
    model = YOLO('data/models/yolov8l.pt')
    yolo_df['class_id'] = yolo_df['class_id'].astype(int)
    yolo_df['tracker_id'] = yolo_df['tracker_id'].astype(int)

    class_items_df = pd.read_csv('data/class_items.csv')
    class_items = np.asarray(class_items_df['id'])[1:]

    items_list = []
    items_df_to_save = pd.DataFrame()

    counter = 1
    for person_id in person_arr:
        only_person_df = yolo_df.loc[yolo_df.tracker_id == person_id]
        only_person_df.reset_index(drop=True, inplace=True)

        video = VideoFileClip(video_path)
        fps = video.fps
        only_person_df = only_person_df[(only_person_df.frame % fps) == 0]

        items_df = get_items_df(only_person_df, model, video, class_items)

        if not items_df.empty:
            items_df_to_save = pd.concat([items_df_to_save, items_df], ignore_index=True)
            person_items = save_items_photoboxes(items_df, only_person_df, video, class_items_df, person_id, items_path)
            items_list.append(person_items)

        logger.info("Detection items for person: %s / %s finished", str(counter), str(len(person_arr)))
        counter += 1

    items_df_to_save.to_csv(to_csv_path, index=False)
    return items_list


def save_items_photoboxes(items_df, only_person_df, video, class_items_df, person_id, items_path):
    person_id_list = []
    item_name_list = []
    item_conf_list = []
    item_path_list = []
    for index, row in items_df.iterrows():
        item_x1 = int(row['x1'])
        item_y1 = int(row['y1'])
        item_x2 = int(row['x2'])
        item_y2 = int(row['y2'])
        item_frame = row['frame']
        item_class_id = row['class_id']
        item_conf = row['confidence']

        person_row = only_person_df.loc[only_person_df.frame == item_frame]
        person_row.reset_index(drop=True, inplace=True)

        frame = person_row['frame'][0]
        x1 = person_row['x1'][0]
        y1 = person_row['y1'][0]
        x2 = person_row['x2'][0]
        y2 = person_row['y2'][0]
        box = (x1, y1, x2, y2)

        photobox = cut_photobox(video, frame, box)

        img_arr = np.asarray(photobox)
        img = img_arr.copy()
        cv.rectangle(img, (item_x1, item_y1), (item_x2, item_y2), (0, 255, 0), 1)
        img = Image.fromarray(img)

        class_items_row = class_items_df.loc[class_items_df.id == item_class_id]
        class_name = class_items_row['name'].values[0]
        filepath = items_path + str(person_id) + '-' + str(class_name) + '-' + str(int(item_conf * 100)) + '.png'
        img.save(filepath)

        person_id_list.append(person_id)
        item_name_list.append(str(class_name))
        item_conf_list.append(int(item_conf * 100))
        item_path_list.append(filepath)

    return [person_id_list, item_name_list, item_conf_list, item_path_list]


def get_items_df(only_person_df, model, video, class_items):
    items_df = pd.DataFrame(columns=['frame', 'x1', 'y1', 'x2', 'y2', 'confidence', 'class_id'])
    for index, row in only_person_df.iterrows():
        x1 = row['x1']
        y1 = row['y1']
        x2 = row['x2']
        y2 = row['y2']
        box = (x1, y1, x2, y2)
        frame = row['frame']

        photobox = cut_photobox(video, frame, box)

        results = model.predict(source=photobox, classes=class_items, verbose=False)[0]
        xyxy = results.boxes.xyxy.cpu().numpy()
        confidence = results.boxes.conf.cpu().numpy()
        class_id = results.boxes.cls.cpu().numpy().astype(int)

        if len(class_id) == 0:
            continue

        data = np.array(
            [frame, xyxy[0][0], xyxy[0][1], xyxy[0][2], xyxy[0][3], confidence[0], class_id[0]]
        )

        if (len(class_id)) == 1:
            data = [data]

        for i in range(1, len(class_id)):
            item = np.array(
                [frame, xyxy[i][0], xyxy[i][1], xyxy[i][2], xyxy[i][3], confidence[i], class_id[i]]
            )
            data = np.vstack([data, item])

        df = pd.DataFrame(
            data=data,
            columns=['frame', 'x1', 'y1', 'x2', 'y2', 'confidence', 'class_id']
        )

        items_df = (
            items_df.copy() if df.empty else df.copy() if items_df.empty else pd.concat([items_df, df])
        )

    items_df.reset_index(drop=True, inplace=True)
    items_df.frame = items_df.frame.astype(int)
    items_df.class_id = items_df.class_id.astype(int)
    items_arr = items_df.class_id.unique().astype(int)
    true_idx = []
    for item in items_arr:
        only_item_df = items_df.loc[items_df.class_id == item]
        true_idx.append(only_item_df['confidence'].idxmax())

    items_df = items_df.iloc[true_idx]
    return items_df


def detect_peoples(video_path, save_results, to_csv_path, ui_progress_bar):
    yolo_model = YOLO('data/models/yolov8l.pt')
    tracker = DeepSort(max_age=20, embedder='torchreid')
    yolo_df = video_processing(yolo_model, tracker, video_path, ui_progress_bar)
    yolo_df.to_csv(to_csv_path + 'detections.csv')
    clear_df(to_csv_path + 'detections.csv', video_path)
    logger.info("Results saved to csv: %s", to_csv_path + 'detections.csv')

    if save_results:
        yolo_df = pd.read_csv(to_csv_path + 'detections.csv')
        save_detection_results(video_path, yolo_df)


def clear_df(yolo_df_path, video_path):
    """
    Очищает yolo df от мерцающих tracker id (которые трекаются меньше чем 1 сек. видео, т.е. не непрерывно)
    """
    logger.info('DataFrame clearing...')
    yolo_df = pd.read_csv(yolo_df_path)
    video_fps = int(get_video_fps(video_path))

    tracker_id_arr = yolo_df.tracker_id.unique().astype(int)
    for tracker in tracker_id_arr:
        only_tracker_df = yolo_df.loc[yolo_df.tracker_id == tracker]
        if len(only_tracker_df) < video_fps:
            del_indexes = [i for i in only_tracker_df.index.values]
        else:
            sequence_counter = 0
            prev_frame = int(only_tracker_df.iloc[0].frame)
            prev_positive_frame = 0  # пооследний фрейм удачной последовательности которую не нужно удалять
            del_indexes = []
            for index, row in only_tracker_df.iterrows():
                frame = int(row.frame)
                difference = frame - prev_frame
                if difference == 0 or difference == 1:
                    sequence_counter += 1
                elif sequence_counter >= video_fps:
                    sequence_counter = 0
                    prev_positive_frame = prev_frame
                else:
                    temp_df = only_tracker_df.loc[(only_tracker_df.frame < frame) & (only_tracker_df.frame > prev_positive_frame)]
                    for i in temp_df.index.values:
                        if i not in del_indexes:
                            del_indexes.append(i)

                    sequence_counter = 0

                prev_frame = frame

        yolo_df = yolo_df.drop(index=del_indexes)

    yolo_df.to_csv(yolo_df_path, index=False)


def video_processing(yolo, tracker, video_path, ui_progress_bar):
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.critical("Video Capture is not opened")

    fps = cap.get(cv.CAP_PROP_FPS)
    frames = cap.get(cv.CAP_PROP_FRAME_COUNT)

    logger.info("Frames Per Second: %s", fps)
    logger.info("Number of frames: %s", frames)
    logger.info("Video length: %s sec", int(frames / fps))

    all_df = pd.DataFrame(columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class_id', 'tracker_id', 'box_square'])
    frames_counter = 0
    one_percent = int(frames * 0.01)
    stager = 10
    logger.info("----Video processing started----")
    begin_time = time.time()
    while cap.isOpened():
        try:
            ret, frame = cap.read()
            if not ret:
                break

            frame_df = frame_processing(frame, yolo, tracker, frames_counter)
            frames_counter += 1

            all_df = (
                all_df.copy() if frame_df.empty else frame_df.copy() if all_df.empty else pd.concat([all_df, frame_df])
            )
            all_df.index.rename('frame', inplace=True)

            if frames_counter >= one_percent * stager:
                if stager <= 90:
                    logger.info("%s%% \t %s / %s frames", stager, frames_counter, frames)
                    stager += 10
                    if ui_progress_bar is not None:
                        ui_progress_bar.setValue(ui_progress_bar.value() + 6)
                elif frames_counter == frames:
                    logger.info("%s%% \t %s / %s frames", stager, frames_counter, frames)

        except KeyboardInterrupt:
            logger.warning("Video processing ended forcibly")
            break

    end_time = time.time()
    logger.info("----Video processing completed----")
    logger.info("Frames processed: %s", frames_counter)
    logger.info("Processing time: %s seconds", int(end_time - begin_time))
    cap.release()
    cv.destroyAllWindows()

    return all_df


def frame_processing(frame, yolo, tracker, frames_counter):
    results = yolo.track(source=frame,
                         tracker='bytetrack.yaml',
                         classes=[0],
                         conf=0.5,
                         persist=True,
                         verbose=False)[0]

    xyxy = results.boxes.xyxy.cpu().numpy()
    confidence = results.boxes.conf.cpu().numpy()
    class_id = results.boxes.cls.cpu().numpy().astype(int)

    frame_df = pd.DataFrame(columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class_id', 'tracker_id', 'box_square'])

    detections = []
    for i in range(len(xyxy)):
        left = xyxy[i][0]
        top = xyxy[i][1]
        w = xyxy[i][2] - xyxy[i][0]
        h = xyxy[i][3] - xyxy[i][1]
        conf = confidence[i]
        detection_class = class_id[i]
        detections.append(([left, top, w, h], conf, detection_class))

    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        if track.det_conf is None:  # не подходит для теста трекера
            continue

        ltrb = track.to_ltrb()
        conf = track.det_conf
        box_width = ltrb[2] - ltrb[0]
        box_height = ltrb[3] - ltrb[1]
        box_square = round(box_width * box_height, 2)
        frame_dict = {
            'x1': ltrb[0],
            'y1': ltrb[1],
            'x2': ltrb[2],
            'y2': ltrb[3],
            'confidence': conf,
            'class_id': track.det_class,
            'tracker_id': track.track_id,
            'box_square': box_square
        }

        frame_dict_df = pd.DataFrame([frame_dict], index=[str(frames_counter)])

        if frame_df.empty:
            frame_df = frame_dict_df.copy()
        else:
            frame_df = pd.concat([frame_df, frame_dict_df])

    return frame_df


def save_detection_results(video_path, yolo_df):
    logger.info("----Save result video----")

    bounding_box_annotator = sv.BoundingBoxAnnotator(color_map='track')
    label_annotator = sv.LabelAnnotator(text_position=sv.Position.CENTER, color_map='track', text_padding=5)

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.critical("Video Capture is not opened")

    out_path = 'test/' + video_path.split('/')[-1]
    out_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    out_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    out_fps = int(cap.get(cv.CAP_PROP_FPS))
    out_fourcc = cv.VideoWriter_fourcc(*'mp4v')

    out_cap = cv.VideoWriter(out_path, out_fourcc, out_fps, (out_width, out_height), isColor=True)

    frames_counter = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_df = yolo_df.loc[yolo_df['frame'] == frames_counter]
        if not frame_df.empty:
            frame_df.reset_index(drop=True, inplace=True)
            frame = annotate_detections(frame, frame_df, bounding_box_annotator, label_annotator, ['person'])

        frames_counter += 1

        out_cap.write(frame)

    cap.release()
    out_cap.release()
    cv.destroyAllWindows()


def annotate_detections(frame, frame_df, bounding_box_annotator, label_annotator, class_names):
    xyxy = np.array([[frame_df['x1'][0], frame_df['y1'][0], frame_df['x2'][0], frame_df['y2'][0]]])
    for i in range(1, len(frame_df)):
        xyxy = np.append(xyxy, [[frame_df['x1'][i], frame_df['y1'][i], frame_df['x2'][i], frame_df['y2'][i]]], axis=0)

    confidence = np.array(frame_df['confidence'])
    class_id = np.array(frame_df['class_id']).astype(int)
    tracker_id = np.array(frame_df['tracker_id']).astype(int)

    detections = sv.Detections(
        xyxy=xyxy,
        confidence=confidence,
        class_id=class_id,
        tracker_id=tracker_id
    )

    labels = [
        f"#{tracker_id[i]} {class_names[class_id[i]]} {confidence[i]:0.2f}"
        for i in range(len(confidence))
    ]

    annotated_frame = bounding_box_annotator.annotate(scene=frame.copy(), detections=detections)
    annotated_frame = label_annotator.annotate(scene=annotated_frame.copy(), detections=detections, labels=labels)
    return annotated_frame


if __name__ == '__main__':
    import torch
    LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(funcName)s  %(lineno)d: %(message)s'
    DATE_FORMAT = '%H:%M:%S'
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

    if torch.cuda.is_available():
        logger.info("CUDA device's count: %s", torch.cuda.device_count())
        logger.info("CUDA current device: %s", torch.cuda.get_device_name(torch.cuda.current_device()))

    parser = argparse.ArgumentParser(description="Mp4 yolo detection")
    parser.add_argument("video_path", type=str, help="Path to video file")
    parser.add_argument("save_results", type=bool, help="Will detection results be saved or not")
    parser.add_argument("to_csv_path", type=str, help="Path to csv file which will be consist detection results")
    args = parser.parse_args()
    detect_peoples(args.video_path, args.save_results, args.to_csv_path)
