"""
Скрипт основных действий и логики работы анализа
"""


import time
import argparse
import os
import logging
import torch
import shutil
import pandas as pd

from yolo_detection import detect_peoples
from yolo_detection import detect_items
from videoprocessing import save_photoboxes_from_yolo
from videoprocessing import clip_video_fragment
from videoprocessing import get_video_fps
from appear_time import calculate_appear_time
from db_processing import insert_to_video_table
from db_processing import insert_to_person_table
from db_processing import check_video_db_exists_bypath
from db_processing import delete_rows_about_video
from db_processing import insert_to_items_table

logger = logging.getLogger(__name__)


def create_data_dirs(video_path):
    file = os.path.basename(video_path)
    file = os.path.splitext(file)
    filename = file[0]

    # data dir
    data_dir = 'data/'
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
        logger.info('Directory %s was created', data_dir)
    else:
        logger.info('Directory %s already exists', data_dir)

    # models dir
    models_dir = data_dir + 'models'
    if not os.path.isdir(models_dir):
        os.makedirs(models_dir)
        logger.info('Directory %s was created', models_dir)
    else:
        logger.info('Directory %s already exists', models_dir)

    # video data dir
    data_dir = 'data/' + filename
    detections_csv_path = data_dir + '/'
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
        logger.info('Directory %s was created', data_dir)
    else:
        logger.info('Directory %s already exists', data_dir)

    # photoboxes dir
    photoboxes_dir = create_sub_dir(data_dir, 'photoboxes')

    # items dir
    items_dir = create_sub_dir(data_dir, 'items')

    # emotions dir
    emotions_dir = create_sub_dir(data_dir, 'emotions')

    # diagramms dir
    diagramms_dir = create_sub_dir(data_dir, 'diagramms')

    # videoclips dir
    videoclips_dir = create_sub_dir(data_dir, 'videoclips')

    time_csv_path = data_dir + '/' + 'time.csv'

    return {
        'data_dir': data_dir,
        'detections_csv_path': detections_csv_path,
        'photoboxes_dir': photoboxes_dir,
        'time_csv_path': time_csv_path,
        'items_dir': items_dir,
        'emotions_dir': emotions_dir,
        'diagramms_dir': diagramms_dir,
        'videoclips_dir': videoclips_dir
    }


def create_sub_dir(data_dir, name_sub_dir):
    if data_dir[-1] == '/':
        data_dir = data_dir[:-1]

    sub_dir = data_dir + '/' + name_sub_dir
    if not os.path.isdir(sub_dir):
        os.makedirs(sub_dir)
        logger.info('Directory %s was created', sub_dir)
    else:
        logger.info('Directory %s already exists', sub_dir)

    sub_dir += '/'
    return sub_dir


def checking_required_files():
    class_items = 'data/class_items.csv'
    class_names = 'data/class_names.csv'
    yolov8l = 'data/models/yolov8l.pt'
    yolov8x = 'data/models/yolov8x.pt'

    if os.path.isfile(class_items) and os.path.isfile(class_names):
        logger.info("All .csv required files exists")
    else:
        logger.warning("CSV required files doesn't exists")

    if os.path.isfile(yolov8l) and os.path.isfile(yolov8x):
        logger.info("All models required files exists")
    else:
        logger.warning("MODELS required files doesn't exists")


def sort_items_list(items_list):
    # [ [tracker_id, item_name, confidence, item_photo], [...]]
    sorted_items = []

    for i in range(len(items_list)):
        for j in range(len(items_list[i][0])):
            elem_arr = [
                int(items_list[i][0][j]),
                items_list[i][1][j],
                int(items_list[i][2][j]),
                items_list[i][3][j]
            ]
            sorted_items.append(elem_arr)

    return sorted_items


def console_analyze():
    if torch.cuda.is_available():
        logger.info("CUDA device's count: %s", torch.cuda.device_count())
        logger.info("CUDA current device: %s", torch.cuda.get_device_name(torch.cuda.current_device()))

    parser = argparse.ArgumentParser(description="Mp4 yolo detection")
    parser.add_argument("video_path", type=str, help="Path to video file")
    parser.add_argument("begin_video_time", type=str, help="Time hh:mm:ss of video begin, in 24h format")
    parser.add_argument("--show_results", action='store_true', default=False, help="Detection results be shown or not")
    parser.add_argument("--detect_items", action='store_true', default=False, help="Detection items or not")
    parser.add_argument("--clip_sec", type=int, default=5, help="Number of seconds for walking video fragment")
    args = parser.parse_args()

    video_path = args.video_path
    begin_video_time = args.begin_video_time
    show_results = args.show_results
    need_detection_items = args.detect_items
    max_clip_seconds = min(args.clip_sec, 15)

    dirs_dict = create_data_dirs(video_path)
    checking_required_files()

    to_csv_path = dirs_dict['detections_csv_path']
    photoboxes_dir = dirs_dict['photoboxes_dir']
    videoclips_begin = dirs_dict['videoclips_begin_dir']
    videoclips_middle = dirs_dict['videoclips_middle_dir']
    videoclips_end = dirs_dict['videoclips_end_dir']
    time_csv_path = dirs_dict['time_csv_path']
    videoclip_dirs = [videoclips_begin, videoclips_middle, videoclips_end]
    items_dir = dirs_dict['items_dir']

    video_id, data_path = check_video_db_exists_bypath(video_path)
    if video_id:
        delete_rows_about_video(video_id)

    items_list = []

    detect_peoples(video_path, show_results, to_csv_path)
    yolo_df = pd.read_csv(to_csv_path)
    tracker_list = yolo_df.tracker_id.unique().astype(int)
    photoboxes_paths = save_photoboxes_from_yolo(video_path, yolo_df, photoboxes_dir)
    videoclips_paths = clip_video_fragment(video_path, yolo_df, videoclip_dirs, max_clip_seconds)
    video_fps = get_video_fps(video_path)
    time_df = calculate_appear_time(yolo_df, begin_video_time, video_fps)
    time_df.to_csv(time_csv_path)
    time_list = time_df['appear_time'].values

    if need_detection_items:
        items_list = detect_items(yolo_df, video_path, items_dir)
        items_list = sort_items_list(items_list)

    insert_to_video_table(video_path)
    insert_to_person_table(video_path, photoboxes_paths, videoclips_paths, time_list, tracker_list)
    if len(items_list) != 0:
        insert_to_items_table(items_list, video_path)


def app_analyze(video_path, begin_video_time, progress_bar):
    """
    Вызывается в app.py при старте анализа
    :param video_path: путь к видео
    :param begin_video_time: время начала видео для расчета времени появления людей
    :param progress_bar: для изменения прогресс бара в ui
    """
    logger = logging.getLogger(__name__)
    if torch.cuda.is_available():
        logger.info("CUDA device's count: %s", torch.cuda.device_count())
        logger.info("CUDA current device: %s", torch.cuda.get_device_name(torch.cuda.current_device()))
    show_results = False  # Хардкод, пока это не нужно

    video_id, data_path = check_video_db_exists_bypath(video_path)
    if video_id:
        shutil.rmtree(data_path)
        delete_rows_about_video(video_id)
        logger.info("Data dir %s was deleted", data_path)

    dirs_dict = create_data_dirs(video_path)
    checking_required_files()

    data_dir = dirs_dict['data_dir']
    to_csv_path = dirs_dict['detections_csv_path']
    photoboxes_dir = dirs_dict['photoboxes_dir']
    time_csv_path = dirs_dict['time_csv_path']

    progress_bar.setValue(10)

    start_time = time.time()
    detect_peoples(video_path, show_results, to_csv_path, progress_bar)
    end_time = time.time()
    logger.info('Detection time: %s sec.', end_time - start_time)
    yolo_df = pd.read_csv(to_csv_path + 'detections.csv')

    tracker_list = yolo_df.tracker_id.unique().astype(int)
    tracker_list.sort()
    ui_tracker_list = [i+1 for i in range(len(tracker_list))]

    start_time = time.time()
    photoboxes_paths = save_photoboxes_from_yolo(video_path, yolo_df, photoboxes_dir, tracker_list, progress_bar)
    end_time = time.time()
    logger.info('Save photoboxes time: %s sec.', end_time - start_time)

    start_time = time.time()
    video_fps = get_video_fps(video_path)
    time_df = calculate_appear_time(yolo_df, begin_video_time, video_fps, tracker_list)
    time_df.to_csv(time_csv_path)
    time_list = time_df['appear_time'].values
    end_time = time.time()
    logger.info('Calculate appear time, time: %s sec.', end_time - start_time)

    start_time = time.time()
    insert_to_video_table(video_path, data_dir)
    insert_to_person_table(video_path, photoboxes_paths, time_list, tracker_list, ui_tracker_list)

    end_time = time.time()
    logger.info('Insert to DataBase time: %s sec.', end_time - start_time)
    progress_bar.setValue(100)


def app_items_detect(person_db_df, video_path):
    logger = logging.getLogger(__name__)
    if torch.cuda.is_available():
        logger.info("CUDA device's count: %s", torch.cuda.device_count())
        logger.info("CUDA current device: %s", torch.cuda.get_device_name(torch.cuda.current_device()))

    tracker_id = person_db_df.tracker_id
    photobox_path = person_db_df.photobox

    photobox_path = photobox_path.split('/')
    yolo_df_path = os.path.join(photobox_path[0], photobox_path[1], 'detections.csv')
    items_dir = os.path.join(photobox_path[0], photobox_path[1], 'items') + '/'
    to_csv_path = os.path.join(items_dir, f'{tracker_id}-items.csv')

    yolo_df = pd.read_csv(yolo_df_path)

    start_time = time.time()
    items_list = detect_items(yolo_df, video_path, items_dir, to_csv_path, [tracker_id])
    items_list = sort_items_list(items_list)
    end_time = time.time()
    logger.info('Items detection time: %s sec.', end_time - start_time)

    if len(items_list) != 0:
        insert_to_items_table(items_list, video_path)


if __name__ == '__main__':
    LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(name)s -- %(funcName)s  %(lineno)d: %(message)s'
    DATE_FORMAT = '%H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    console_analyze()
