import cv2
import numpy as np

# Original Image
img = cv2.imread('dragon.jpg')
cv2.imshow("Original", img)

kernel = np.ones((5,5), dtype='uint8')

# Erosion & Dilation Block
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erosion", erosion)
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilation", dilation)

# Opening & Closing Block
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)

# Gradient Block
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)

# Top Hat & Black Hat Block
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Top Hat", top_hat)
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Black Hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()