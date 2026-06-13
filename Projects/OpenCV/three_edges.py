import cv2

img = cv2.imread("dragon.jpg")

# Binary Threshold
threshold_value = 100
_,thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Edge Detection
min_thresh = 100
max_thresh = 200
edge = cv2.Canny(img, min_thresh, max_thresh)

cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Canny Edge", edge)

cv2.waitKey(0)
cv2.destroyAllWindows()