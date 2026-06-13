import cv2
import numpy as np

# Original Image
img= cv2.imread("dragon.jpg")
cv2.imshow("Original", img)

# Column & Row
column = img.shape[1]
row = img.shape[0]

# Shifting Cords
shift= np.float32([(1,0,50),(0,1,70)])

# Rotation Settings
centre = (column/2, row/2)
angle = 180
rotate = cv2.getRotationMatrix2D(centre, angle , 1)

# Shifted Image
shifted = cv2.warpAffine(img, shift, (column, row))
cv2.imshow("Shifted", shifted)

# Rotate Image
rotated = cv2.warpAffine(img, rotate, (column, row))
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()