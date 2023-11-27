import time
import logging
import numpy as np
import cv2 as cv
import pandas as pd
from ultralytics import YOLO
import supervision as sv


LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(name)s -- %(funcName)s  %(lineno)d: %(message)s'
DATE_FORMAT = '%H:%M:%S'
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def detect(video_path='videos/1min10sec.mkv', to_csv_path='test/1min10sec.csv'):
    model = YOLO('data/models/yolov8l.pt')
    yolo_df = video_processing(model, video_path)
    yolo_df.to_csv(to_csv_path)
    logger.info("Results saved to csv: %s", to_csv_path)


def save_res(video_path='videos/1min10sec.mkv', to_csv_path='test/1min10sec.csv', output_name='test/1min10sec.mp4'):
    yolo_df = pd.read_csv(to_csv_path)
    model = YOLO('data/models/yolov8l.pt')
    class_names = model.model.names

    bounding_box_annotator = sv.BoundingBoxAnnotator()

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.critical("Video Capture is not opened")

    frames_counter = 0

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv.CAP_PROP_FPS))
    fourcc = cv.VideoWriter_fourcc(*'mp4v')

    out = cv.VideoWriter(output_name,
                         fourcc,
                         fps, (width, height),
                         isColor=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_df = yolo_df.loc[yolo_df['frame'] == frames_counter]
        if not frame_df.empty:
            frame_df.reset_index(drop=True, inplace=True)
            frame = add_yolo_detections(frame, frame_df, bounding_box_annotator, class_names)

        frames_counter += 1

        out.write(frame)

    cap.release()
    cv.destroyAllWindows()


def add_yolo_detections(frame, df, bounding_box_annotator, class_names):
    """ A function that adds detection results in the form of boxes to each frame """
    xyxy = np.array([[df['x1'][0], df['y1'][0], df['x2'][0], df['y2'][0]]])
    for i in range(1, len(df)):
        xyxy = np.append(xyxy, [[df['x1'][i], df['y1'][i], df['x2'][i], df['y2'][i]]], axis=0)

    confidence = np.array(df['confidence'])
    class_id = np.array(df['class_id']).astype(int)
    tracker_id = np.array(df['tracker_id']).astype(int)

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
    label_annotator = sv.LabelAnnotator(text_position=sv.Position.CENTER)
    annotated_frame = label_annotator.annotate(scene=annotated_frame.copy(), detections=detections, labels=labels)
    return annotated_frame


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


if __name__ == '__main__':
    detect()
    save_res()
