import logging
import os
import numpy as np
import cv2 as cv
import pandas as pd

from ultralytics import YOLO
from hsemotion.facial_emotions import HSEmotionRecognizer
from facenet_pytorch import MTCNN

from fer_detection import transform_emotions

logger = logging.getLogger(__name__)


def load_models():
    yolo_model = YOLO('data/models/yolov8l.pt')
    class_items_df = pd.read_csv('data/class_items.csv')
    class_items = np.asarray(class_items_df['id'])[1:]

    fer_detector = HSEmotionRecognizer(model_name='enet_b0_8_best_afew', device='cuda')
    mtcnn = MTCNN(select_largest=True, min_face_size=20)

    return yolo_model, class_items, fer_detector, mtcnn


def target_video_detection(video_path, detections_path, progress_bar):
    detections_df = pd.read_csv(detections_path)

    target_items_df = pd.DataFrame(columns=['frame', 'item_id', 'tracker_id', 'xyxy', 'conf', 'xyxy_ph'])
    target_emotions_df = pd.DataFrame(columns=['frame', 'emotion', 'tracker_id', 'xyxy', 'conf', 'xyxy_ph'])

    yolo_model, class_items, fer_detector, mtcnn = load_models()

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.critical("Video Capture is not opened")

    fps = cap.get(cv.CAP_PROP_FPS)
    frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    logger.info("Frames Per Second: %s", fps)
    logger.info("Number of frames: %s", frames)
    logger.info("Video length: %s sec", int(frames / fps))

    start_frame = int(detections_df.iloc[0].frame)
    last_frame = int(detections_df.iloc[len(detections_df) - 1].frame)

    logger.info("Start target frame: %s", start_frame)
    logger.info("Last target frame: %s", last_frame)

    cap.set(cv.CAP_PROP_POS_FRAMES, start_frame)

    step = 10  # только каждый 10-й кадр будет обрабатываться

    pb_steps = (last_frame - start_frame) // step
    upd_pb = 95 / pb_steps
    pb_value = 0

    frame_counter = start_frame
    while cap.isOpened():
        if frame_counter == last_frame + 1:
            break

        if frame_counter % step == 0:
            if progress_bar is not None:
                pb_value += upd_pb
                pb_value_int = round(pb_value)
                progress_bar.setValue(pb_value_int)
        else:
            frame_counter += 1
            continue

        only_frame_df = detections_df.loc[detections_df.frame == frame_counter]
        if len(only_frame_df) == 0:
            frame_counter += 1
            continue

        # print(only_frame_df)

        ret, frame = cap.read()
        if not ret:
            logger.warning('Not ret')
            break

        for index, row in only_frame_df.iterrows():
            x1 = 0 if int(row.x1) < 0 else int(row.x1)
            y1 = 0 if int(row.y1) < 0 else int(row.y1)
            x2 = width if int(row.x2) > width else int(row.x2)
            y2 = height if int(row.y2) > height else int(row.y2)
            ph_width = x2 - x1
            ph_height = y2 - y1

            tracker_id = int(row.tracker_id)

            photobox = frame[y1:y2, x1:x2]
            photobox = cv.cvtColor(photobox, cv.COLOR_BGR2RGB)

            items = target_detection_items(yolo_model, class_items, photobox, ph_width, ph_height)
            emotions = target_detection_emotions(photobox, fer_detector, mtcnn, ph_width, ph_height)

            if len(items) != 0:
                for i in items:
                    items_row = {
                        'frame': frame_counter,
                        'item_id': i['class_id'],
                        'tracker_id': tracker_id,
                        'xyxy': i['xyxy'],
                        'conf': i['conf'],
                        'xyxy_ph': (x1, y1, x2, y2)
                    }
                    items_row_df = pd.DataFrame([items_row])
                    if not target_items_df.empty:
                        target_items_df = pd.concat([target_items_df, items_row_df], ignore_index=True)
                    else:
                        target_items_df = items_row_df.copy()

            if len(emotions) != 0:
                for i in emotions:
                    emotions_row = {
                        'frame': frame_counter,
                        'emotion': i['emotion'],
                        'tracker_id': tracker_id,
                        'xyxy': i['xyxy'],
                        'conf': i['conf'],
                        'xyxy_ph': (x1, y1, x2, y2)
                    }
                    emotions_row_df = pd.DataFrame([emotions_row])
                    if not target_emotions_df.empty:
                        target_emotions_df = pd.concat([target_emotions_df, emotions_row_df], ignore_index=True)
                    else:
                        target_emotions_df = emotions_row_df.copy()

        frame_counter += 1

    cap.release()

    return target_items_df, target_emotions_df


def target_detection_emotions(photobox, fer_detector, mtcnn, ph_width, ph_height):
    emotions = []

    boxes, _ = mtcnn.detect(photobox)
    if boxes is not None:
        x1_bb = 0 if int(boxes[0][0]) < 0 else int(boxes[0][0])
        x2_bb = ph_width if int(boxes[0][2]) > ph_width else int(boxes[0][2])
        y1_bb = 0 if int(boxes[0][1]) < 0 else int(boxes[0][1])
        y2_bb = ph_height if int(boxes[0][3]) > ph_height else int(boxes[0][3])

        face_img = photobox[y1_bb:y2_bb, x1_bb:x2_bb]
        _, scores_hsemotions = fer_detector.predict_emotions(face_img, logits=False)

        fer_result = transform_emotions(scores_hsemotions)
        top_emotion_key = max(fer_result[0]['emotions'], key=fer_result[0]['emotions'].get)
        top_emotion_value = fer_result[0]['emotions'].get(top_emotion_key)

        emotion_dict = {
            'emotion': top_emotion_key,
            'conf': top_emotion_value,
            'xyxy': (x1_bb, y1_bb, x2_bb, y2_bb)
        }

        emotions.append(emotion_dict)

    return emotions


def target_detection_items(model, class_items, photobox, ph_width, ph_height):
    results = model.predict(source=photobox, classes=class_items, verbose=False)[0]
    xyxy = results.boxes.xyxy.cpu().numpy()
    confidence = results.boxes.conf.cpu().numpy()
    class_id = results.boxes.cls.cpu().numpy().astype(int)

    items = []

    for i in range(len(class_id)):
        x1 = 0 if int(xyxy[i][0]) < 0 else int(xyxy[i][0])
        y1 = 0 if int(xyxy[i][1]) < 0 else int(xyxy[i][1])
        x2 = ph_width if int(xyxy[i][2]) > ph_width else int(xyxy[i][2])
        y2 = ph_height if int(xyxy[i][3]) > ph_height else int(xyxy[i][3])
        item_dict = {
            'class_id': class_id[i],
            'conf': confidence[i],
            'xyxy': (x1, y1, x2, y2)
        }
        items.append(item_dict)

    return items
