import time
import argparse
import logging
import numpy as np
import cv2 as cv
import pandas as pd
from ultralytics import YOLO
from supervision.annotators.core import BoundingBoxAnnotator
from supervision.detection.core import Detections

from moviepy.editor import VideoFileClip
from PIL import Image
from videoprocessing import cut_photobox

logger = logging.getLogger(__name__)


def detect_items(yolo_df, video_path, items_path):
    model = YOLO('data/models/yolov8l.pt')
    yolo_df['class_id'] = yolo_df['class_id'].astype(int)
    yolo_df['tracker_id'] = yolo_df['tracker_id'].astype(int)

    class_items_df = pd.read_csv('data/class_items.csv')
    class_items = np.asarray(class_items_df['id'])[1:]

    person_arr = yolo_df.tracker_id.unique().astype(int)
    counter = 1
    for person_id in person_arr:
        only_person_df = yolo_df.loc[yolo_df.tracker_id == person_id]
        only_person_df.reset_index(drop=True, inplace=True)

        video = VideoFileClip(video_path)
        fps = video.fps
        only_person_df = only_person_df[(only_person_df.frame % fps) == 0]

        items_df = get_items_df(only_person_df, model, video, class_items)
        save_items_photoboxes(items_df, only_person_df, video, class_items_df, person_id, items_path)

        logger.info("Detection items for person: %s / %s finished", str(counter), str(len(person_arr)))
        counter += 1


def save_items_photoboxes(items_df, only_person_df, video, class_items_df, person_id, items_path):
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

        img = np.asarray(photobox)
        cv.rectangle(img, (item_x1, item_y1), (item_x2, item_y2), (0, 255, 0), 1)
        img = Image.fromarray(img)

        class_items_row = class_items_df.loc[class_items_df.id == item_class_id]
        class_name = class_items_row['name'].values[0]
        filename = str(person_id) + '-' + str(class_name) + '-' + str(int(item_conf * 100)) + '.png'
        img.save(items_path + filename)


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


def detect_peoples(video_path, show_results, to_csv_path):
    model = YOLO('data/models/yolov8l.pt')
    yolo_df = video_processing(model, video_path)
    yolo_df.to_csv(to_csv_path)
    logger.info("Results saved to csv: %s", to_csv_path)

    if show_results:
        yolo_df = pd.read_csv(to_csv_path)
        show_detection_results(video_path, yolo_df)


def video_processing(yolo, video_path):
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.critical("Video Capture is not opened")

    fps = cap.get(cv.CAP_PROP_FPS)
    frames = cap.get(cv.CAP_PROP_FRAME_COUNT)

    logger.info("Frames Per Second: %s", fps)
    logger.info("Number of frames: %s", frames)
    logger.info("Video length: %s sec", int(frames / fps))

    all_df = pd.DataFrame(columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class_id', 'tracker_id'])
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

            frame_df = frame_processing(frame, yolo, frames_counter)
            frames_counter += 1

            all_df = (
                all_df.copy() if frame_df.empty else frame_df.copy() if all_df.empty else pd.concat([all_df, frame_df])
            )
            all_df.index.rename('frame', inplace=True)

            if frames_counter >= one_percent * stager:
                if stager <= 90:
                    logger.info("%s%% \t %s / %s frames", stager, frames_counter, frames)
                    stager += 10
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


def frame_processing(frame, yolo, frames_counter):
    results = yolo.track(source=frame,
                         tracker='bytetrack.yaml',
                         classes=[0],
                         persist=True,
                         verbose=False)[0]

    xyxy = results.boxes.xyxy.cpu().numpy()
    if len(xyxy) == 0:
        xyxy = [[0, 0, 0, 0]]
        confidence = [0]
        class_id = [0]
        tracker_id = [np.nan]
    else:
        confidence = results.boxes.conf.cpu().numpy()
        class_id = results.boxes.cls.cpu().numpy().astype(int)
        try:
            tracker_id = results.boxes.id.cpu().numpy().astype(int)
        except AttributeError:
            tracker_id = [np.nan]

    data = np.array(
        [xyxy[0][0], xyxy[0][1], xyxy[0][2], xyxy[0][3], confidence[0], class_id[0], tracker_id[0]]
    )

    if (len(tracker_id)) == 1:
        data = [data]

    for i in range(1, len(tracker_id)):
        item = np.array(
            [xyxy[i][0], xyxy[i][1], xyxy[i][2], xyxy[i][3], confidence[i], class_id[i], tracker_id[i]]
        )
        data = np.vstack([data, item])

    index_list = [str(frames_counter)] * len(class_id)

    df = pd.DataFrame(
        data=data,
        columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class_id', 'tracker_id'],
        index=index_list
    )

    return df


def show_detection_results(video_path, yolo_df):
    logger.info("----Show result video----")
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.critical("Video Capture is not opened")

    frames_counter = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_df = yolo_df.loc[yolo_df['frame'] == frames_counter]
        if not frame_df.empty:
            frame_df.reset_index(drop=True, inplace=True)
            frame = annotate_detections(frame, frame_df)

        frames_counter += 1

        cv.imshow('Result Video', frame)
        key = cv.waitKey(10)
        if key == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


def annotate_detections(frame, frame_df):
    xyxy = np.array([[frame_df['x1'][0], frame_df['y1'][0], frame_df['x2'][0], frame_df['y2'][0]]])
    for i in range(1, len(frame_df)):
        xyxy = np.append(xyxy, [[frame_df['x1'][i], frame_df['y1'][i], frame_df['x2'][i], frame_df['y2'][i]]], axis=0)

    conf = np.array(frame_df['confidence'])
    class_id = np.array(frame_df['class_id']).astype(int)
    tracker_id = np.array(frame_df['tracker_id']).astype(int)

    detections = Detections(xyxy=xyxy, confidence=conf, class_id=class_id, tracker_id=tracker_id)
    box_annotator = BoundingBoxAnnotator()

    frame = box_annotator.annotate(scene=frame.copy(), detections=detections)
    return frame


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
    parser.add_argument("show_results", type=bool, help="Will detection results be shown or not")
    parser.add_argument("to_csv_path", type=str, help="Path to csv file which will be consist detection results")
    args = parser.parse_args()
    detect_peoples(args.video_path, args.show_results, args.to_csv_path)
