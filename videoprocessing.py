import logging
import numpy as np
import cv2 as cv
from moviepy.editor import VideoFileClip, ImageSequenceClip
from PIL import Image
from facenet_pytorch import MTCNN
from fer import FER

logger = logging.getLogger(__name__)


def detect_fer(photoboxes_paths):
    fer_detector = FER(mtcnn=True)
    ph_emotions = []
    for ph_path in photoboxes_paths:
        ph = cv.imread(ph_path)
        ph = cv.cvtColor(ph, cv.COLOR_BGR2RGB)

        fer_result = fer_detector.detect_emotions(ph)
        if len(fer_result) != 0:
            result_emotions = fer_result[0]['emotions']
            result_emotions['photobox_path'] = ph_path
            result_emotions['recognized'] = True
        else:
            result_emotions = {
                'photobox_path': ph_path,
                'recognized': False
            }

        ph_emotions.append(result_emotions)

    return ph_emotions


def save_photoboxes_from_yolo(video_path, yolo_df, dir_to_save):
    """
    анализируем боксы людей, берем наибольший бокс, проверяем чтоб лицо нахоидилось и сохраняем
    """
    video = VideoFileClip(video_path)
    mtcnn = MTCNN(select_largest=True, device='cuda:0')
    step = 5  # каждый 5 кадр берем и смотрим бокс лица
    person_arr = yolo_df.tracker_id.unique().astype(int)
    photoboxes_paths_list = []
    person_counter = 0
    logger.info('Persons number: %s', len(person_arr))
    for person in person_arr:
        person_counter += 1
        logger.info('Person  %s / %s', person_counter, len(person_arr))
        only_person_df = yolo_df.loc[yolo_df.tracker_id == person]

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

            boxes, probs = mtcnn.detect(photobox)
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
                if i >= 40:  # i >= x,  x -- const.  (x / step) + 1 -- столько кадров максимум анализируется
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


def clip_video_fragment(video_path, yolo_df, dirs_to_save, max_clip_seconds):
    video = VideoFileClip(video_path)
    fps = video.fps
    max_clip_frames = int(max_clip_seconds * fps)
    person_arr = yolo_df.tracker_id.unique().astype(int)
    videoclips_paths = [[], [], []]
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

                # размер ставится для UI!!!
                fixed_width = 200
                fixed_height = 400
                img = img.resize((fixed_width, fixed_height))

                img = np.asarray(img)
                images.append(img)
            clip = ImageSequenceClip(images, fps=fps)
            # clip.write_videofile('test' + str(person) + '.mp4', fps=fps)
            path = dirs_to_save[i] + 'person' + str(person) + '.gif'
            videoclips_paths[i].append(path)
            clip.write_gif(path, fps=fps, program='ffmpeg', logger=None)

    return videoclips_paths


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
