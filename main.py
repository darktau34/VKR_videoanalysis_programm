import argparse
import os
import logging
import torch
import pandas as pd

from yolo_detection import detect_peoples
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
    data_dir = 'data/' + filename
    detections_csv_path = data_dir + '/' + 'detections.csv'
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
        LOGGER.info('Directory %s was created', data_dir)
    else:
        LOGGER.info('Directory %s already exists', data_dir)

    # photoboxes dir
    photoboxes_dir = data_dir + '/' + 'photoboxes'
    if not os.path.isdir(photoboxes_dir):
        os.makedirs(photoboxes_dir)
        LOGGER.info('Directory %s was created', photoboxes_dir)
    else:
        LOGGER.info('Directory %s already exists', photoboxes_dir)

    photoboxes_dir += '/'

    # videoclips dir
    videoclips_dir = data_dir + '/' + 'videoclips'
    if not os.path.isdir(videoclips_dir):
        os.makedirs(videoclips_dir)
        LOGGER.info('Directory %s was created', videoclips_dir)
    else:
        LOGGER.info('Directory %s already exists', videoclips_dir)

    videoclips_dir += '/'

    # videoclips begin, middle, end

    videoclips_begin_dir = videoclips_dir + 'begin'
    if not os.path.isdir(videoclips_begin_dir):
        os.makedirs(videoclips_begin_dir)
        LOGGER.info('Directory %s was created', videoclips_begin_dir)
    else:
        LOGGER.info('Directory %s already exists', videoclips_begin_dir)

    videoclips_begin_dir += '/'

    videoclips_middle_dir = videoclips_dir + 'middle'
    if not os.path.isdir(videoclips_middle_dir):
        os.makedirs(videoclips_middle_dir)
        LOGGER.info('Directory %s was created', videoclips_middle_dir)
    else:
        LOGGER.info('Directory %s already exists', videoclips_middle_dir)

    videoclips_middle_dir += '/'

    videoclips_end_dir = videoclips_dir + 'end'
    if not os.path.isdir(videoclips_end_dir):
        os.makedirs(videoclips_end_dir)
        LOGGER.info('Directory %s was created', videoclips_end_dir)
    else:
        LOGGER.info('Directory %s already exists', videoclips_end_dir)

    videoclips_end_dir += '/'

    time_csv_path = data_dir + '/' + 'time.csv'
    return {
        'detections_csv_path': detections_csv_path,
        'photoboxes_dir': photoboxes_dir,
        'videoclips_begin_dir': videoclips_begin_dir,
        'videoclips_middle_dir': videoclips_middle_dir,
        'videoclips_end_dir': videoclips_end_dir,
        'time_csv_path': time_csv_path
    }


def main():
    if torch.cuda.is_available():
        LOGGER.info("CUDA device's count: %s", torch.cuda.device_count())
        LOGGER.info("CUDA current device: %s", torch.cuda.get_device_name(torch.cuda.current_device()))

    parser = argparse.ArgumentParser(description="Mp4 yolo detection")
    parser.add_argument("video_path", type=str, help="Path to video file")
    parser.add_argument("begin_video_time", type=str, help="Time hh:mm:ss of video begin, in 24h format")
    parser.add_argument("--show_results", action='store_true', default=False, help="Detection results be shown or not")
    parser.add_argument("--clip_sec", type=int, default=5, help="Number of seconds for walking video fragment")
    args = parser.parse_args()

    video_path = args.video_path
    begin_video_time = args.begin_video_time
    show_results = args.show_results
    max_clip_seconds = min(args.clip_sec, 15)

    dirs_dict = create_data_dirs(video_path)

    to_csv_path = dirs_dict['detections_csv_path']
    photoboxes_dir = dirs_dict['photoboxes_dir']
    videoclips_begin = dirs_dict['videoclips_begin_dir']
    videoclips_middle = dirs_dict['videoclips_middle_dir']
    videoclips_end = dirs_dict['videoclips_end_dir']
    time_csv_path = dirs_dict['time_csv_path']
    videoclip_dirs = [videoclips_begin, videoclips_middle, videoclips_end]

    detect_peoples(video_path, show_results, to_csv_path)
    yolo_df = pd.read_csv(to_csv_path)
    save_photoboxes_from_yolo(video_path, yolo_df, photoboxes_dir)
    clip_video_fragment(video_path, yolo_df, videoclip_dirs, max_clip_seconds)
    video_fps = get_video_fps(video_path)
    time_df = calculate_appear_time(yolo_df, begin_video_time, video_fps)
    time_df.to_csv(time_csv_path)


if __name__ == '__main__':
    main()
