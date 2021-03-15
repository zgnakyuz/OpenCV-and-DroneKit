import cv2
from copy import deepcopy

img = cv2.imread("myimg.jpeg")

r, g, b = deepcopy(img), deepcopy(img), deepcopy(img)  # To keep the original img

r[:, :, 0], r[:, :, 1] = 0, 0
g[:, :, 0], g[:, :, 2] = 0, 0
b[:, :, 1], b[:, :, 2] = 0, 0

cv2.imwrite("R_of_Img.jpeg", r)
cv2.imwrite("G_of_Img.jpeg", g)
cv2.imwrite("B_of_Img.jpeg", b)
