import cv2

img = cv2.imread("dragon.jpg")

# Gaussian Blur
kernel_size = (15,15)
sigma_x = 0
sigma_y = 0
gaussian_blur = cv2.GaussianBlur(img, kernel_size, sigma_x)

# Median Blur
kernel = 9
median_blur = cv2.medianBlur(img, kernel)

# Bilateral Filter
diameter = 11
sigma_color = 100
sigma_space = 100
bilateral_filter = cv2.bilateralFilter(img, diameter, sigma_color, sigma_space)

cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Filter", bilateral_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()