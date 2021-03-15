import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("myimg.jpeg")

px = img[55, 55]  # a pixel
img[55, 55] = [255, 255, 255]  # [b, g, r] values
cv2.imshow("img", img)
# Region of Image = sub-image of an image

roi = img[0: 100, 50: 75]  # y-axis: 0 to 100, x-axis: 50 to 75

# showing in pyplot
"""b1, g1, r1 = cv2.split(roi)
b2, g2, r2 = cv2.split(roi2)
plt.subplot(2, 2, 1)
plt.imshow(cv2.merge([r1, g1, b1]), interpolation="bicubic")
plt.subplot(2, 2, 2)
plt.imshow(cv2.merge([r2, g2, b2]), interpolation="bicubic")
plt.show()"""

img[0: 100, 50: 75] = [255, 255, 255]  # changes the color of the area to white (roi = [255, 255, 255] doesn't work)
copied_img = img[250: 375, 295: 399]
img[500: 625, 550: 654] = copied_img  # the determined area must equal to the area of the copied_img
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
