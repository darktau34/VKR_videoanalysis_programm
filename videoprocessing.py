import logging
import numpy as np
from moviepy.editor import VideoFileClip, ImageSequenceClip
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
        while frame_row.empty:
            mean_frame += 1
            frame_row = only_person_df.loc[only_person_df.frame == mean_frame]
        frame_row.reset_index(drop=True, inplace=True)
        x1 = frame_row.x1.values[0]
        y1 = frame_row.y1.values[0]
        x2 = frame_row.x2.values[0]
        y2 = frame_row.y2.values[0]
        box = (x1, y1, x2, y2)
        photobox = cut_photobox(video, mean_frame, box)
        photobox.save(dir_to_save + 'person' + str(person) + '.png')

    logger.info('Photoboxes are saved to path: %s', dir_to_save)


def cut_photobox(video_clip, frame_number, box):
    fps = video_clip.fps
    frame_sec = (1 / fps) * frame_number
    frame = video_clip.get_frame(frame_sec)
    pil_im = Image.fromarray(frame)
    photobox = pil_im.crop(box)
    return photobox


def clip_video_fragment(video_path, yolo_df, dirs_to_save, max_clip_seconds):
    video = VideoFileClip(video_path)
    fps = video.fps
    max_clip_frames = int(max_clip_seconds * fps)
    person_arr = yolo_df.tracker_id.unique().astype(int)
    logger.info('Video fps: %s', str(fps))
    logger.info('Video fragment in seconds: %s', str(max_clip_seconds))
    logger.info('Video fragment in frames: %s', str(max_clip_frames))
    for person in person_arr:
        only_person_df = yolo_df.loc[yolo_df.tracker_id == person]
        only_person_df.reset_index(drop=True, inplace=True)
        # print(only_person_df)
        for i in range(len(dirs_to_save)):
            if i == 0:
                video_clip_df = only_person_df[:max_clip_frames]
            elif i == 1:
                center_df = int(len(only_person_df) / 2)
                half_clip_frames = int(max_clip_frames / 2)
                video_clip_df = only_person_df[center_df - half_clip_frames:center_df + half_clip_frames]
            else:
                start = int(len(only_person_df) - max_clip_frames)
                video_clip_df = only_person_df[start:]

            # print(video_clip_df)

            max_width = 0.0
            max_height = 0.0
            for index, row in video_clip_df.iterrows():
                x1 = row['x1']
                y1 = row['y1']
                x2 = row['x2']
                y2 = row['y2']
                cur_width = x2 - x1
                cur_height = y2 - y1
                if cur_width > max_width:
                    max_width = cur_width
                if cur_height > max_height:
                    max_height = cur_height

            max_width = round(max_width)
            max_height = round(max_height)
            # print(f'W: {max_width} \t H: {max_height}')
            images = []
            for index, row in video_clip_df.iterrows():
                frame_num = int(row['frame'])
                x1 = row['x1']
                y1 = row['y1']
                x2 = row['x2']
                y2 = row['y2']
                box = (x1, y1, x2, y2)
                box = increase_box(box, max_width, max_height)
                img = cut_photobox(video, frame_num, box)
                # print(img)
                img = np.asarray(img)
                images.append(img)
            clip = ImageSequenceClip(images, fps=fps)
            # clip.write_videofile('test' + str(person) + '.mp4', fps=fps)
            clip.write_gif(dirs_to_save[i] + 'person' + str(person) + '.gif', fps=fps, program='ffmpeg', logger=None)


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
