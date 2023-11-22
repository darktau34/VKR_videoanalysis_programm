import argparse
import os
import logging
import torch
import pandas as pd

from yolo_detection import detect_peoples
from yolo_detection import detect_items
from videoprocessing import save_photoboxes_from_yolo
from videoprocessing import clip_video_fragment
from videoprocessing import get_video_fps
from appear_time import calculate_appear_time


LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(name)s -- %(funcName)s  %(lineno)d: %(message)s'
DATE_FORMAT = '%H:%M:%S'
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def create_data_dirs(video_path):
    file = os.path.basename(video_path)
    file = os.path.splitext(file)
    filename = file[0]

    # data dir
    data_dir = 'data/'
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
        LOGGER.info('Directory %s was created', data_dir)
    else:
        LOGGER.info('Directory %s already exists', data_dir)

    # models dir
    models_dir = data_dir + 'models'
    if not os.path.isdir(models_dir):
        os.makedirs(models_dir)
        LOGGER.info('Directory %s was created', models_dir)
    else:
        LOGGER.info('Directory %s already exists', models_dir)

    # video data dir
    data_dir = 'data/' + filename
    detections_csv_path = data_dir + '/' + 'detections.csv'
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
        LOGGER.info('Directory %s was created', data_dir)
    else:
        LOGGER.info('Directory %s already exists', data_dir)

    # photoboxes dir
    photoboxes_dir = create_sub_dir(data_dir, 'photoboxes')

    # videoclips dir
    videoclips_dir = create_sub_dir(data_dir, 'videoclips')

    # videoclips begin, middle, end
    videoclips_begin_dir = create_sub_dir(videoclips_dir, 'begin')
    videoclips_middle_dir = create_sub_dir(videoclips_dir, 'middle')
    videoclips_end_dir = create_sub_dir(videoclips_dir, 'end')

    # items dir
    items_dir = create_sub_dir(data_dir, 'items')

    time_csv_path = data_dir + '/' + 'time.csv'

    return {
        'detections_csv_path': detections_csv_path,
        'photoboxes_dir': photoboxes_dir,
        'videoclips_begin_dir': videoclips_begin_dir,
        'videoclips_middle_dir': videoclips_middle_dir,
        'videoclips_end_dir': videoclips_end_dir,
        'time_csv_path': time_csv_path,
        'items_dir': items_dir
    }


def create_sub_dir(data_dir, name_sub_dir):
    if data_dir[-1] == '/':
        data_dir = data_dir[:-1]

    sub_dir = data_dir + '/' + name_sub_dir
    if not os.path.isdir(sub_dir):
        os.makedirs(sub_dir)
        LOGGER.info('Directory %s was created', sub_dir)
    else:
        LOGGER.info('Directory %s already exists', sub_dir)

    sub_dir += '/'
    return sub_dir


def checking_required_files():
    class_items = 'data/class_items.csv'
    class_names = 'data/class_names.csv'
    yolov8l = 'data/models/yolov8l.pt'
    yolov8x = 'data/models/yolov8x.pt'

    if os.path.isfile(class_items) and os.path.isfile(class_names):
        LOGGER.info("All .csv required files exists")
    else:
        LOGGER.warning("CSV required files doesn't exists")

    if os.path.isfile(yolov8l) and os.path.isfile(yolov8x):
        LOGGER.info("All models required files exists")
    else:
        LOGGER.warning("MODELS required files doesn't exists")


def main():
    if torch.cuda.is_available():
        LOGGER.info("CUDA device's count: %s", torch.cuda.device_count())
        LOGGER.info("CUDA current device: %s", torch.cuda.get_device_name(torch.cuda.current_device()))

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

    detect_peoples(video_path, show_results, to_csv_path)
    yolo_df = pd.read_csv(to_csv_path)
    save_photoboxes_from_yolo(video_path, yolo_df, photoboxes_dir)
    clip_video_fragment(video_path, yolo_df, videoclip_dirs, max_clip_seconds)
    video_fps = get_video_fps(video_path)
    time_df = calculate_appear_time(yolo_df, begin_video_time, video_fps)
    time_df.to_csv(time_csv_path)
    if need_detection_items:
        detect_items(yolo_df, video_path, items_dir)


if __name__ == '__main__':
    main()
