import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("myimg.jpeg", cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1, IMREAD_UNCHANGED = -1, IMREAD_GRAYSCALE = 0

cv2.imshow("image", img)  # title name, image
cv2.waitKey(0)  # before closing, 0 means open until we press a button, otherwise the value is the delay (ms)
cv2.destroyAllWindows()

#plt.imshow(img, cmap="gray", interpolation="bicubic")  # show in matplotlib window
#plt.plot([500, 750], [600, 700], "c", linewidth=10)  # writing on image
#plt.show()

cv2.imwrite("myimggrey.png", img)  # to save what we did
