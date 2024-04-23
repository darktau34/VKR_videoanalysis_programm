import logging
import os
import numpy as np
import cv2 as cv
import pandas as pd
from moviepy.editor import VideoFileClip
from PIL import Image
from facenet_pytorch import MTCNN
from db_processing import insert_to_videoclip_table

logger = logging.getLogger(__name__)


def save_photoboxes_from_yolo(video_path, yolo_df, dir_to_save, person_arr, ui_progress_bar):
    """
    анализируем боксы людей, берем наибольший бокс, проверяем чтоб лицо нахоидилось и сохраняем
    """
    video = VideoFileClip(video_path)
    mtcnn = MTCNN(select_largest=True)
    step = 5  # каждый 5 кадр берем и смотрим бокс лица
    photoboxes_paths_list = []
    person_counter = 0
    logger.info('Persons number: %s', len(person_arr))
    for person in person_arr:
        person_counter += 1
        logger.info('Person  %s / %s', person_counter, len(person_arr))
        only_person_df = yolo_df.loc[yolo_df.tracker_id == person]

        if ui_progress_bar is not None:
            if person_counter == int(len(person_arr) / 4):
                ui_progress_bar.setValue(ui_progress_bar.value() + 5)
            elif person_counter == int(len(person_arr) / 3):
                ui_progress_bar.setValue(ui_progress_bar.value() + 5)
            elif person_counter == int(len(person_arr) / 2):
                ui_progress_bar.setValue(ui_progress_bar.value() + 5)
            else:
                ui_progress_bar.setValue(ui_progress_bar.value() + 5)

        for i in range(0, len(only_person_df), step):
            frame_row = only_person_df.loc[only_person_df.box_square == only_person_df.box_square.max()]
            frame_row.reset_index(drop=True, inplace=True)
            x1 = frame_row.x1.values[0]
            y1 = frame_row.y1.values[0]
            x2 = frame_row.x2.values[0]
            y2 = frame_row.y2.values[0]
            box = (x1, y1, x2, y2)
            box_width = x2 - x1
            box_height = y2 - y1
            frame_number = int(frame_row.frame.values[0])
            # print(frame_row)

            photobox = cut_photobox(video, frame_number, box)
            if i == 0:
                photobox_start_iter = photobox.copy()

            boxes = None
            try:
                boxes, probs = mtcnn.detect(photobox)
            except RuntimeError:
                pass
            # print(boxes, probs)

            skip = False
            if boxes is not None:
                # Если mtccn нашло лицо
                # Проверяем чтобы координаты бокса mtcnn не были за границами фотобокса
                for k in range(len(boxes)):  # цикл по массиву найденных боксов
                    if boxes[k][0] < 0:
                        skip = True
                        break
                    if boxes[k][1] < 0:
                        skip = True
                        break
                    if boxes[k][2] > box_width:
                        skip = True
                        break
                    if boxes[k][3] > box_height:
                        skip = True
                        break

                    if (boxes[k][2] - boxes[k][0]) * (boxes[k][3] - boxes[k][1]) < 48 * 48:
                        skip = True
                    else:
                        skip = False

                if not skip:
                    # сохраняем
                    path = dir_to_save + 'person' + str(person) + '.png'
                    photoboxes_paths_list.append(path)
                    photobox.save(path)
                    break

            if skip or boxes is None:
                if i >= 40 or i + step > len(only_person_df):
                    # Если уже на протяжении N кадров не находит лицо
                    path = dir_to_save + 'person' + str(person) + '.png'
                    photoboxes_paths_list.append(path)
                    photobox_start_iter.save(path)
                    break

                for _ in range(step - 1):
                    frame_row = only_person_df.loc[only_person_df.box_square == only_person_df.box_square.max()]
                    frame_row_idx = frame_row.index
                    only_person_df = only_person_df.drop(index=frame_row_idx)

    logger.info('Photoboxes are saved to path: %s', dir_to_save)
    return photoboxes_paths_list


def cut_photobox(video_clip, frame_number, box):
    fps = video_clip.fps
    frame_sec = (1 / fps) * frame_number
    frame = video_clip.get_frame(frame_sec)
    pil_im = Image.fromarray(frame)
    photobox = pil_im.crop(box)
    return photobox


def clip_video_fragment(video_path, person_id, tracker_id):
    videonameext = video_path.split('/')[-1]
    videoname = videonameext.split('.')[0]

    yolo_df_path = os.path.join('data', videoname, 'detections.csv')
    yolo_df = pd.read_csv(yolo_df_path)

    only_tracker_df = yolo_df.loc[yolo_df.tracker_id == tracker_id]
    only_tracker_df.reset_index(drop=True, inplace=True)

    logger.info('Needs processing %s frames', len(only_tracker_df))

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.error("Video Capture is not opened")

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    out_path = os.path.join('data', videoname, 'videoclips', f'person{tracker_id}.mp4')
    out_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    out_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    out_fps = int(cap.get(cv.CAP_PROP_FPS))
    out_fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out_cap = cv.VideoWriter(out_path, out_fourcc, out_fps, (out_width, out_height), isColor=True)

    prev_frame_number = 0
    for index, row in only_tracker_df.iterrows():
        frame_number = int(row.frame)
        x1 = 0 if int(row.x1) < 0 else int(row.x1)
        y1 = 0 if int(row.y1) < 0 else int(row.y1)
        x2 = width if int(row.x2) > width else int(row.x2)
        y2 = height if int(row.y2) > height else int(row.y2)

        if index == 0:
            cap.set(cv.CAP_PROP_POS_FRAMES, frame_number)

        if index != 0 and frame_number - 1 != prev_frame_number:
            cap.set(cv.CAP_PROP_POS_FRAMES, frame_number)

        ret, frame = cap.read()
        if not ret:
            logger.error("Read frame error")

        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        out_cap.write(frame)
        prev_frame_number = frame_number

    cap.release()
    out_cap.release()
    cv.destroyAllWindows()

    insert_to_videoclip_table(person_id, out_path)


def increase_box(box, max_width, max_height):
    box_width = box[2] - box[0]
    box_height = box[3] - box[1]
    if box_width != max_width:
        diff = max_width - box_width
        diff = diff / 2
        x1 = box[0] - diff
        x2 = box[2] + diff
    else:
        x1 = box[0]
        x2 = box[2]

    if box_height != max_height:
        diff = max_height - box_height
        diff = diff / 2
        y1 = box[1] - diff
        y2 = box[3] + diff
    else:
        y1 = box[1]
        y2 = box[2]

    new_box = (x1, y1, x2, y2)

    return new_box


def get_video_fps(video_path):
    video = VideoFileClip(video_path)
    return video.fps
