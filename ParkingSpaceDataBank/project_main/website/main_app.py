import cv2
import pickle
import cvzone
import numpy as np

class VideoCamera(object):

    def __init__(self):
        #video feed
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        with open("website/CarParkPos", "rb") as f:
            posList = pickle.load(f)

        width, height = 100, 50

        success, frame = self.video.read()

        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameBlur = cv2.GaussianBlur(frameGray, (3, 3), 1)
        frameThreshold = cv2.adaptiveThreshold(frameBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                               cv2.THRESH_BINARY_INV, 25, 16)
        frameMedian = cv2.medianBlur(frameThreshold, 5)
        kernel = np.ones((1, 1), np.uint8)
        frameDilate = cv2.dilate(frameMedian, kernel, iterations=1)

        for pos in posList:
            x, y = pos

            frameCrop = frameDilate[y:y + height, x:x + width]
            # cv2.imshow(str(x * y), frameCrop)
            count = cv2.countNonZero(cv2.Canny(frameCrop, 100, 200))
            cvzone.putTextRect(frame, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0)

            if count < 600:
                color = (0, 255, 0)
                thickness = 3
            else:
                color = (0, 0, 255)
                thickness = 2

            cv2.rectangle(frame, pos, (pos[0] + width, pos[1] + height), color, thickness)
        
        cvzone.putTextRect(frame, f'Free: {count}/{len(posList)}', (250, 40), scale=2, thickness=2, offset=20, colorR = (0, 200, 0))

        #cv2.imshow("Frame", frame)
        #cv2.waitKey(1)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()