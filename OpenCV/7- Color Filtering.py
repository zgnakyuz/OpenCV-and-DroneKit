import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # A way to define colors
    # hsv = hue sat val
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([255, 180, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)  # It is 0 or 1, if it's in range it will be 1 (white)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
