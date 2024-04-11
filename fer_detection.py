import time
import os
import cv2 as cv
import logging
from fer import FER
from db_processing import insert_to_emotions_table


def fer_photobox_main(photobox_path, person_id):
    logger = logging.getLogger(__name__)

    start_time = time.time()
    results = fer_detect_photoboxes([photobox_path])
    end_time = time.time()
    logger.info('Emotion recognition time: %s', str(end_time - start_time))
    print(results)

    facebox = cv.imread(photobox_path)

    is_recognized = results[0]['recognized']
    if is_recognized:
        x1 = results[0]['box'][0]
        y1 = results[0]['box'][1]
        x2 = x1 + results[0]['box'][2]
        y2 = y1 + results[0]['box'][3]
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
    fer_detector = FER(mtcnn=True)

    ph_emotions = []
    for ph_path in photoboxes_paths:
        ph = cv.imread(ph_path)
        ph = cv.cvtColor(ph, cv.COLOR_BGR2RGB)

        fer_result = fer_detector.detect_emotions(ph)

        if len(fer_result) != 0:
            result_emotions = fer_result[0]
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
