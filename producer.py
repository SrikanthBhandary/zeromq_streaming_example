import cv2
import zmq
from time import time

cap = cv2.VideoCapture(0)

context = zmq.Context()
dst = context.socket(zmq.PUSH)
dst.bind("tcp://192.168.43.191:5557")

while True:
    ret, frame = cap.read()
    dst.send_pyobj(dict(frame=frame, ts=time()))