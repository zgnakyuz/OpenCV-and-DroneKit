import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([160, 40, 80])
    upper_red = np.array([200, 255, 255])

    lower_green = np.array([50, 60, 60])
    upper_green = np.array([100, 255, 255])

    lower_blue = np.array([100, 100, 35])
    upper_blue = np.array([120, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((5, 5), np.uint8)
    mask1 = cv2.erode(mask1, kernel)
    mask2 = cv2.erode(mask2, kernel)
    mask3 = cv2.erode(mask3, kernel)

    laplacian = cv2.Laplacian(mask1, cv2.CV_64F)
    sobelx = cv2.Sobel(mask3, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(mask3, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(mask3, 100, 100)  # If 100 and 100 get smaller, the edges will increase

    cv2.imshow("original", frame)
    cv2.imshow("laplacian", laplacian)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("sobely", sobely)
    cv2.imshow("edges", edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
