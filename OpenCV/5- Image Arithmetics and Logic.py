import cv2
import numpy as np

img1 = cv2.imread("3D-Matplotlib.png")
# img2 = cv2.imread("mainsvmimage.png")

# add = img1 + img2  # combining images (their shapes must equal to each other's)
# add = cv2.add(img1, img2)  # adds all of the pixel values (if it is above 255, it is 255)

# weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)  # last one is brightness, other values are coefficients
# It works like img1 + img2, and it's even more functional

"""cv2.imshow("add", weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

img2 = cv2.imread("mainlogo.png")
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # To get a mask after
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)  # mask = threshold
# if the value of the pixel above 220, it is converted to 255, if it is less, converted to black (0)
mask_inv = cv2.bitwise_not(mask)  # inverse of mask
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow("res", dst)
cv2.imshow("mask", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()