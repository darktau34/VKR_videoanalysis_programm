from facenet_pytorch import MTCNN
import cv2 as cv
from PIL import Image
import numpy as np
import os
import sys
from tqdm import tqdm
from datetime import datetime
import pandas as pd
import argparse
import os


def main(video_path):
    file = os.path.basename(video_path)
    file = os.path.splitext(file)
    filename = file[0]
    ext = file[1]

    if ext != '.mp4':
        print('Video is not mp4')
        return

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print('Cap is not opened')
        return
    video_fps = cap.get(cv.CAP_PROP_FPS)
    video_length_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    video_bitrate = int(cap.get(cv.CAP_PROP_BITRATE))
    video_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    print(f'FPS: {video_fps}')
    print(f'Length Frames: {video_length_frames}')
    print(f'Length Seconds: {video_length_frames / video_fps}')
    print(f'Bitrate: {video_bitrate}')
    print(f'Width: {video_width}')
    print(f'Height: {video_height}')

    mtcnn = MTCNN(select_largest=True, device='cuda:0')
    pbar = tqdm(total=video_length_frames, ncols=80)

    out = cv.VideoWriter('test/face_censored.mp4',
                         cv.VideoWriter_fourcc(*'mp4v'),
                         video_fps, (video_width, video_height),
                         isColor=True)

    frame_counter = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print(f'\t NOT RET')
            break

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image = Image.fromarray(rgb_frame)
        boxes, probs = mtcnn.detect(image)

        if boxes is None:
            continue

        for box in boxes:
            # box = boxes[0]
            x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])

            if x1 < 0:
                x1 = 0
            elif x1 > video_width:
                x1 = video_width

            if x2 < 0:
                x2 = 0
            elif x2 > video_width:
                x2 = video_width

            if y1 < 0:
                y1 = 0
            elif y1 > video_height:
                y1 = video_height

            if y2 < 0:
                y2 = 0
            elif y2 > video_height:
                y2 = video_height

            face = frame[y1:y2, x1:x2]
            blur_face = cv.blur(face, (25, 25))
            frame[y1:y2, x1:x2] = blur_face

        out.write(frame)
        pbar.update(1)
        frame_counter += 1

    cap.release()
    out.release()
    cv.destroyAllWindows()
    pbar.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("video_path", type=str, help="Path to video")
    args = parser.parse_args()
    try:
        main(args.video_path)
    except KeyboardInterrupt:
        print('Video processing ended forcibly')
