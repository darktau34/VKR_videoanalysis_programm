import argparse
import os
import logging
import torch
import pandas as pd

from yolo_detection import detect_peoples
from photobox import save_photoboxes_from_yolo

LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(name)s -- %(funcName)s  %(lineno)d: %(message)s'
DATE_FORMAT = '%H:%M:%S'
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def create_data_dirs(video_path):
    file = os.path.basename(video_path)
    file = os.path.splitext(file)
    filename = file[0]

    data_dir = 'data/' + filename
    to_csv_path = data_dir + '/' + filename + '.csv'
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
        LOGGER.info('Directory %s was created', data_dir)
    else:
        LOGGER.info('Directory %s already exists', data_dir)

    photoboxes_dir = data_dir + '/' + 'photoboxes'
    if not os.path.isdir(photoboxes_dir):
        os.makedirs(photoboxes_dir)
        LOGGER.info('Directory %s was created', photoboxes_dir)
    else:
        LOGGER.info('Directory %s already exists', photoboxes_dir)

    photoboxes_dir += '/'

    return to_csv_path, photoboxes_dir


def main():
    if torch.cuda.is_available():
        LOGGER.info("CUDA device's count: %s", torch.cuda.device_count())
        LOGGER.info("CUDA current device: %s", torch.cuda.get_device_name(torch.cuda.current_device()))

    parser = argparse.ArgumentParser(description="Mp4 yolo detection")
    parser.add_argument("video_path", type=str, help="Path to video file")
    parser.add_argument("--show_results", action='store_true', default=False, help="Detection results be shown or not")
    args = parser.parse_args()

    to_csv_path, photoboxes_dir = create_data_dirs(args.video_path)

    detect_peoples(args.video_path, args.show_results, to_csv_path)
    yolo_df = pd.read_csv(to_csv_path)
    save_photoboxes_from_yolo(args.video_path, yolo_df, photoboxes_dir)


if __name__ == '__main__':
    main()
