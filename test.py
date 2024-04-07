"""
Скрипт для теста анализа настроений
"""


def deepface_main():
    import cv2 as cv
    from deepface import DeepFace
    img = cv.imread('data/aquarel_2/photoboxes/person16.png')

    backends = [
        'opencv',
        'ssd',
        'dlib',
        'mtcnn',
        'retinaface',
        'mediapipe',
        'yolov8',
        'yunet',
        'fastmtcnn',
    ]

    analysis = DeepFace.analyze(img, detector_backend=backends[3], actions=['emotion'])
    print(analysis)


def fer_main():
    from fer import FER
    import time
    import cv2 as cv
    import matplotlib.pyplot as plt

    img = cv.imread('test/phbox/person16.png')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
    fer_detector_mtcnn = FER(mtcnn=True)
    fer_detector = FER()
    emotions_mtcnn = fer_detector_mtcnn.detect_emotions(img)
    emotions = fer_detector.detect_emotions(img)
    print(emotions_mtcnn)
    print(emotions)

    time.sleep(1)
    print('')
    start_time = time.time()
    emotions_mtcnn = fer_detector_mtcnn.detect_emotions(img)
    end_time = time.time()
    print(emotions_mtcnn)
    print(f'Execute time: {end_time - start_time}')

    print(emotions_mtcnn[0]['emotions'])
    print(type(emotions_mtcnn[0]['emotions']))
    plt.imshow(img)
    plt.show()


def yolo():
    import pandas as pd
    import time
    from yolo_detection import detect_peoples
    from videoprocessing import save_photoboxes_from_yolo
    from videoprocessing import detect_fer

    video_path = 'videos/aquarel_2.mp4'
    show_results = False
    to_csv_path = 'test/test_'

    # start_time = time.time()
    # detect_peoples(video_path, show_results, to_csv_path)
    # end_time = time.time()
    # print(f'Execute time: {end_time - start_time}')

    yolo_df = pd.read_csv(to_csv_path + 'detections.csv')
    print(yolo_df)

    photoboxes_dir = 'test/phbox/'
    start_time = time.time()
    photoboxes_paths = save_photoboxes_from_yolo(video_path, yolo_df, photoboxes_dir)
    end_time = time.time()
    print(f'Execute time: {end_time - start_time}')

    start_time = time.time()
    photoboxes_emotions = detect_fer(photoboxes_paths)
    end_time = time.time()
    print(f'Execute time: {end_time - start_time}')
    print('')
    print(photoboxes_emotions)

    for ph_emotion in photoboxes_emotions:
        is_recognized = ph_emotion['recognized']
        photobox = ph_emotion['photobox_path']
        if is_recognized:
            del ph_emotion['recognized']
            del ph_emotion['photobox_path']
            display_str = f'{photobox} --'

            for _ in range(3):
                top_key = max(ph_emotion, key=ph_emotion.get)
                top_value = ph_emotion.get(top_key)
                display_str += f' {top_key}: {top_value} '

                del ph_emotion[top_key]
        else:
            display_str = f'{photobox} -- {is_recognized}'

        print(display_str)

def test_mtcnn():
    from facenet_pytorch import MTCNN
    import time
    import cv2 as cv
    import matplotlib.pyplot as plt

    img = cv.imread('test/phbox/person16.png')
    mtcnn = MTCNN(select_largest=True, device='cuda:0')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
    # почему использование mtcnn здесь отличается от использования в videoprocessing (там находит лицо, здесь нет)
    # попробовать не через cv а так же как в videoprocessing -- Решение: cvtcolor
    start_time = time.time()
    boxes, probs = mtcnn.detect(img)
    print(boxes)
    print(probs)
    end_time = time.time()
    print(f'Execute time: {end_time - start_time}')
    plt.imshow(img)
    plt.show()


def yolo_deepsort():
    import cv2 as cv
    import pandas as pd
    from ultralytics import YOLO
    import matplotlib.pyplot as plt
    import supervision as sv
    from deep_sort_realtime.deepsort_tracker import DeepSort
    from showing_yolo import add_yolo_detections
    import numpy as np

    video_path = 'videos/1min20sec.mkv'
    yolo_model = YOLO('data/models/yolov8l.pt')
    tracker = DeepSort(max_age=20, embedder='torchreid')
    bounding_box_annotator = sv.BoundingBoxAnnotator(color_map='track')

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print("Video Capture is not opened")

    out_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    out_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    out_fps = int(cap.get(cv.CAP_PROP_FPS))
    out_fourcc = cv.VideoWriter_fourcc(*'mp4v')

    # out = cv.VideoWriter('test/deepsort.mp4',
    #                      out_fourcc,
    #                      out_fps, (out_width, out_height),
    #                      isColor=True)

    fps = cap.get(cv.CAP_PROP_FPS)
    frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
    frames_counter = 0
    while cap.isOpened():
        try:
            # if frames_counter >= 30:
            #     break
            ret, frame = cap.read()
            if not ret:
                break

            # results = yolo_model.predict(source=frame, classes=[0], verbose=False)[0]
            results = yolo_model.track(source=frame,
                                       tracker='bytetrack.yaml',
                                       classes=[0],
                                       persist=True,
                                       verbose=False)[0]
            xyxy = results.boxes.xyxy.cpu().numpy()
            confidence = results.boxes.conf.cpu().numpy()
            class_id = results.boxes.cls.cpu().numpy().astype(int)

            detections = []
            for i in range(len(xyxy)):
                left = xyxy[i][0]
                top = xyxy[i][1]
                w = xyxy[i][2] - xyxy[i][0]
                h = xyxy[i][3] - xyxy[i][1]
                conf = confidence[i]
                detection_class = class_id[i]
                detections.append(([left, top, w, h], conf, detection_class))

            # print(detections)

            frame_df = pd.DataFrame(columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class_id', 'tracker_id'])

            tracks = tracker.update_tracks(detections, frame=frame)
            # print(tracks)
            for track in tracks:
                if not track.is_confirmed():
                    continue

                ltrb = track.to_ltrb()
                # print(track_id, ltrb, sep='\n\n')
                conf = 0.0 if track.det_conf is None else track.det_conf
                frame_dict = {
                    'x1': ltrb[0],
                    'y1': ltrb[1],
                    'x2': ltrb[2],
                    'y2': ltrb[3],
                    'confidence': conf,
                    'class_id': track.det_class,
                    'tracker_id': track.track_id
                }
                frame_dict_df = pd.DataFrame([frame_dict])

                if frame_df.empty:
                    frame_df = frame_dict_df.copy()
                else:
                    frame_df = pd.concat([frame_df, frame_dict_df], ignore_index=True)


                # print(frame_df)

            # print(frame_df)
            if not frame_df.empty:
                frame = add_yolo_detections(frame, frame_df, bounding_box_annotator, ['person'])

            cv.imshow('Result Video', frame)
            key = cv.waitKey(1)
            if key == ord('q'):
                break
            # out.write(frame)

            frames_counter += 1

        except KeyboardInterrupt:
            print("Video processing ended forcibly")
            break

    cap.release()
    # out.release()
    cv.destroyAllWindows()




if __name__ == '__main__':
    import logging
    LOG_FORMAT = '%(asctime)s   [%(levelname)s] %(name)s -- %(funcName)s  %(lineno)d: %(message)s'
    DATE_FORMAT = '%H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    # deepface_main()
    # fer_main()
    # yolo()
    # test_mtcnn()
    yolo_deepsort()
