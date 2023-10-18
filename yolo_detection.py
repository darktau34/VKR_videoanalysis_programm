import argparse
import logging
import cv2 as cv
import pandas as pd
from ultralytics import YOLO

LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(funcName)s  %(lineno)d: %(message)s'
DATE_FORMAT = '%H:%M:%S'
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def detect_peoples(video_path, show_results, to_csv_path):
    model = YOLO('data/models/yolov8l.pt')
    yolo_df = video_processing(model, video_path)


def video_processing(yolo, video_path):
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        LOGGER.critical("Video Capture is not opened")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Mp4 yolo detection")
    parser.add_argument("video_path", type=str, help="Path to video file")
    parser.add_argument("show_results", type=bool, help="Will detection results be shown or not")
    parser.add_argument("to_csv_path", type=str, help="Path to csv file which will be consist detection results")
    args = parser.parse_args()
    detect_peoples(args.video_path, args.show_results, args.to_csv_path)
