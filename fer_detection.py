import time
import os
import cv2 as cv
import logging
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random

from hsemotion.facial_emotions import HSEmotionRecognizer
from facenet_pytorch import MTCNN

from db_processing import insert_to_emotions_table, insert_to_diagramm_table
from videoprocessing import cut_photobox

fer_detector = HSEmotionRecognizer(model_name='enet_b0_8_best_afew', device='cuda')
mtcnn = MTCNN(select_largest=True, min_face_size=20)

emotion_name_dict = {
    0: 'angry',
    1: 'contempt',
    2: 'disgust',
    3: 'fear',
    4: 'happy',
    5: 'neutral',
    6: 'sad',
    7: 'surprise'
}


def transform_emotions(scores_hsemotions):
    emotion_score_dict = dict()
    for i in range(len(scores_hsemotions)):
        em_name = emotion_name_dict.get(i)
        em_score = round(scores_hsemotions[i], 2)
        em_score = float(em_score)
        emotion_score_dict[em_name] = em_score

    fer_result_dict = [{
        'emotions': emotion_score_dict
    }]
    return fer_result_dict


def fer_all_frames(video_path, person_id, tracker_id):
    logger = logging.getLogger(__name__)
    logger.info('Diagramms - person id: %s', person_id)
    logger.info('Diagramms - tracker id: %s', tracker_id)

    videonameext = video_path.split('/')[-1]
    videoname = videonameext.split('.')[0]

    yolo_df_path = os.path.join('data', videoname, 'detections.csv')
    yolo_df = pd.read_csv(yolo_df_path)

    only_tracker_df = yolo_df.loc[yolo_df.tracker_id == tracker_id]

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        logger.error("Video Capture is not opened")

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    emotions_number_dict = {
        'angry': 0,
        'sad': 0,
        'fear': 0,
        'disgust': 0,
        'happy': 0,
        'surprise': 0,
        'neutral': 0,
        'not_recognized': 0
    }

    max_detection_frames = 100
    detection_step = int(len(only_tracker_df) / max_detection_frames)

    fer_detector = FER(mtcnn=True)
    frame_counter = 0
    for index, row in only_tracker_df.iterrows():
        if frame_counter >= detection_step:
            frame_counter = 0

        if frame_counter != 0:
            frame_counter += 1
            continue

        frame_number = row.frame

        x1 = 0 if int(row.x1) < 0 else int(row.x1)
        y1 = 0 if int(row.y1) < 0 else int(row.y1)
        x2 = width if int(row.x2) > width else int(row.x2)
        y2 = height if int(row.y2) > height else int(row.y2)

        cap.set(cv.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        if not ret:
            logger.error("Read frame error")

        photobox = frame[y1:y2, x1:x2]
        photobox = cv.cvtColor(photobox, cv.COLOR_BGR2RGB, photobox)

        fer_result = fer_detector.detect_emotions(photobox)

        if len(fer_result) != 0:
            top_emotion = max(fer_result[0]['emotions'], key=fer_result[0]['emotions'].get)
            emotions_number_dict[top_emotion] += 1
        else:
            emotions_number_dict['not_recognized'] += 1

        frame_counter += 1

    cap.release()

    save_path = os.path.join('data', videoname, 'diagramms', f'{tracker_id}-diag_emotions.png')
    try:
        plot_emotion_stats(emotions_number_dict, save_path)
    except Exception as e:
        logger.error('Plot emotion diagramm error')
        logger.error(e)
    else:
        insert_to_diagramm_table(person_id, save_path)


def pie_format(pct, allvals):
    # absolute = int(np.round(pct/100.*np.sum(allvals)))
    # return "{:.1f}% ({:d})".format(pct, absolute)
    return "{:.1f}%".format(pct)


def translate_emotions(emotions_list):
    translated_emotions = {
        'angry': 'Злость',
        'sad': 'Грусть',
        'fear': 'Испуг',
        'disgust': 'Отвращение',
        'happy': 'Радость',
        'surprise': 'Удивление',
        'neutral': 'Нейтрально',
        'not_recognized': 'Не обнаружено'
    }

    new_list = []
    for em in emotions_list:
        new_em = translated_emotions.get(em)
        new_list.append(new_em)

    return new_list


def plot_emotion_stats(emotions_number_dict, save_path):
    matplotlib.use('agg')

    values = list(emotions_number_dict.values())
    labels = list(emotions_number_dict.keys())

    x = []
    y = []
    for i in range(len(values)):
        if values[i] != 0:
            x.append(values[i])
            y.append(labels[i])

    y = translate_emotions(y)

    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi=80)
    wedges, texts, autotexts = ax.pie(x, autopct=lambda pct: pie_format(pct, x), textprops=dict(color="w"), startangle=270)

    ax.legend(wedges, y, title="Эмоции", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.text(0, 1.1, "Диаграмма эмоций человека на видео", horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight': 500, 'size': 12})
    plt.setp(autotexts, size=10, weight=700)

    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)


def fer_photobox_main(photobox_path, person_id):
    logger = logging.getLogger(__name__)

    start_time = time.time()
    results = fer_detect_photoboxes([photobox_path])
    end_time = time.time()
    logger.info('Emotion recognition time: %s', str(end_time - start_time))

    facebox = cv.imread(photobox_path)

    is_recognized = results[0]['recognized']
    if is_recognized:
        x1 = results[0]['box'][0]
        y1 = results[0]['box'][1]
        x2 = results[0]['box'][2]
        y2 = results[0]['box'][3]
        cv.rectangle(facebox, (x1, y1), (x2, y2), (0, 255, 0), 1)

        if (x2 - x1) * (y2 - y1) < 48 * 48:
            need_warning = True
        else:
            need_warning = False

        photobox_path = photobox_path.split('/')
        photobox_filename = photobox_path[-1].split('.')[0]

        facebox_path = os.path.join(photobox_path[0], photobox_path[1], 'emotions', f'facebox_{photobox_filename}.png')
        emotions_dict = results[0]['emotions']
        top_emotion = max(emotions_dict, key=emotions_dict.get)

        cv.imwrite(facebox_path, facebox)

        emotion_row = (person_id, facebox_path, emotions_dict, top_emotion, is_recognized, need_warning)
        insert_to_emotions_table(emotion_row)
    else:
        emotion_row = (person_id, None, None, None, is_recognized, None)
        insert_to_emotions_table(emotion_row)


def fer_detect_photoboxes(photoboxes_paths):
    ph_emotions = []
    for ph_path in photoboxes_paths:
        ph = cv.imread(ph_path)
        ph = cv.cvtColor(ph, cv.COLOR_BGR2RGB)

        boxes, _ = mtcnn.detect(ph)

        if boxes is not None:
            y1, y2, x1, x2 = int(boxes[0][1]), int(boxes[0][3]), int(boxes[0][0]), int(boxes[0][2])
            face_img = ph[y1:y2, x1:x2]

            _, scores_hsemotions = fer_detector.predict_emotions(face_img, logits=False)

            result_emotions = transform_emotions(scores_hsemotions)[0]
            result_emotions['box'] = [x1, y1, x2, y2]
            result_emotions['photobox_path'] = ph_path
            result_emotions['recognized'] = True
        else:
            result_emotions = {
                'photobox_path': ph_path,
                'recognized': False
            }

        ph_emotions.append(result_emotions)

    return ph_emotions


if __name__ == '__main__':
    LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(name)s -- %(funcName)s  %(lineno)d: %(message)s'
    DATE_FORMAT = '%H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

    # fer_photobox_main('data/mall/items/41-handbag-51.png', 877)
    # print(select_from_emotions_table(877))

    start_time = time.time()
    fer_all_frames('/home/slava/projects/nir_7sem/videos/aquarel_2.mp4', 905, 21)
    end_time = time.time()
    print(end_time - start_time)
