import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)  # 0 --> default webcam, 1 --> other webcam etc...
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # codec
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()  # ret(return) will be True or False - frame will be frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # press q to quit
        break


cv2.destroyAllWindows()
cap.release()
out.release()

