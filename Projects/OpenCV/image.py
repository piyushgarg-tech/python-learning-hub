import cv2

# Read Image
image = cv2.imread('/home/akuma/Pictures/dragon.jpg')

# Resizing According to aspect ratio
scale = 50
width = int(image.shape[1]*scale/100)
height = int(image.shape[0]*scale/100)
dim = (width,height)

resized = cv2.resize(image,dim, interpolation=cv2.INTER_AREA)

# Show Both Images
cv2.imshow("Image Window", image)
cv2.imshow("Resized Image", resized)

# Write Image
cv2.imwrite("dragon.jpg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()