import cv2

# Read Image
image = cv2.imread("dragon.jpg")

# Resize Image
resized = cv2.resize(image, (250,350))
cv2.putText(resized, "Original", (15,25), cv2.FONT_HERSHEY_DUPLEX, 0.7, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)
# Show Original Image
cv2.imshow("Original", resized)

flip_v = cv2.flip(resized, 0)
cv2.putText(flip_v, "Vertical", (150,20), cv2.FONT_HERSHEY_DUPLEX, 0.7, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)
# Show Vertical Flip Image
cv2.imshow("Vertical Flip", flip_v)
flip_h = cv2.flip(resized, 1)
cv2.putText(flip_h, "Horizontal", (15,25), cv2.FONT_HERSHEY_DUPLEX, 0.7, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)
# Show Horizontal Flip Image
cv2.imshow("Horizontal Flip", flip_h)
flip_hv = cv2.flip(resized, -1)
cv2.putText(flip_hv, "Horizontal & Vertical", (5,15), cv2.FONT_HERSHEY_DUPLEX, 0.7, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)
# Show Horizontal & Vertical Flip Image
cv2.imshow("Horizontal & Vertical Flip", flip_hv)

cv2.waitKey(0)
cv2.destroyAllWindows()