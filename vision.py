import cv2

# Load an image
image = cv2.imread("speedometer.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect the speedometer
speedometer_x = 0  # Adjust this to match the actual location of the speedometer
speedometer_y = 0  # Adjust this to match the actual location of the speedometer
speedometer_width = 100  # Adjust this to match the actual width of the speedometer
speedometer_height = 100  # Adjust this to match the actual height of the speedometer
speedometer_threshold = 128  # Adjust this to match the actual threshold for detecting the speedometer

count = 0
for y in range(speedometer_y, speedometer_y + speedometer_height):
    for x in range(speedometer_x, speedometer_x + speedometer_width):
        gray_value = gray_image[y, x]
        if gray_value > speedometer_threshold:
            count += 1

print("Count: " + str(count))
