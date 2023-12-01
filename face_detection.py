import logging
import cv2 as cv

logger = logging.getLogger(__name__)


def detect_faces(haarcascade_path):
    face_cascade_model = cv.CascadeClassifier(haarcascade_path)

    img = cv.imread('data/1min20sec/photoboxes/person13.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade_model.detectMultiScale(img_gray, 1.3, 2)
    print(faces)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    detect_faces('data/models/haarcascade_frontalface_default.xml')
