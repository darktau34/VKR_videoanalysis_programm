import logging
import pandas as pd
from moviepy.editor import VideoFileClip
from PIL import Image

logger = logging.getLogger(__name__)


def save_photoboxes_from_yolo(video_path, yolo_df, dir_to_save):
    video = VideoFileClip(video_path)
    person_arr = yolo_df.tracker_id.unique().astype(int)
    logger.info('Persons number: %s', len(person_arr))
    for person in person_arr:
        only_person_df = yolo_df.loc[yolo_df.tracker_id == person]
        mean_frame = only_person_df.frame.values.mean()
        mean_frame = mean_frame.round().astype(int)
        frame_row = only_person_df.loc[only_person_df.frame == mean_frame]
        x1 = frame_row.x1.values[0]
        y1 = frame_row.y1.values[0]
        x2 = frame_row.x2.values[0]
        y2 = frame_row.y2.values[0]
        box = (x1, y1, x2, y2)
        photobox = cut_photobox(video, mean_frame, box)
        photobox.save(dir_to_save + str(person) + '.png')

    logger.info('Photoboxes are saved to path: %s', dir_to_save)


def cut_photobox(video_clip, frame_number, box):
    fps = video_clip.fps
    frame_sec = (1 / fps) * frame_number
    frame = video_clip.get_frame(frame_sec)
    pil_im = Image.fromarray(frame)
    photobox = pil_im.crop(box)
    return photobox


if __name__ == '__main__':
    df = pd.read_csv('data/50sec/50sec.csv')
    save_photoboxes_from_yolo('video/50sec.mp4', df, 'data/50sec/photoboxes/')
