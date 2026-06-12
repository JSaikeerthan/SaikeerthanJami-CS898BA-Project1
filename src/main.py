import cv2
from image_statistics import print_channel_statistics

IMAGE_PATH = "images/HW1_IMG.png"

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

blue, green, red = cv2.split(image)

print_channel_statistics(red, "Red")
print_channel_statistics(green, "Green")
print_channel_statistics(blue, "Blue")