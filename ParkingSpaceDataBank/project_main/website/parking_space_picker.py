import cv2
import pickle
import cvzone
import numpy as np


#video feed
cap = cv2.VideoCapture(0)

try:
    with open("CarParkPos", "rb") as f:
        posList = pickle.load(f)
except:
    posList = []

width, height = 100, 50


def mouseClick(events, x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos  in enumerate (posList):
            x1, y1 = pos
            if x1 < x < x1+width and y1 < y <y1+height:
                posList.pop(i)

    with open("CarParkPos", "wb") as f:
        pickle.dump(posList, f)


while True:
    ret, frame = cap.read()

    for pos in posList:
        cv2.rectangle(frame, pos, (pos[0] + width, pos[1]+height), (0,200,0), 2)

    cv2.imshow("frame", frame)
    cv2.setMouseCallback("frame", mouseClick)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()