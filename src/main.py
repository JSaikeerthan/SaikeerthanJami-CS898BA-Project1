import cv2
from image_statistics import print_channel_statistics
from conversions import generate_conversions
from affine_transforms import create_affine_transformations
from gaussian_blur import apply_gaussian_blurs
from create_subsets import create_subsets

IMAGE_PATH = "images/HW1_IMG.png"

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

blue, green, red = cv2.split(image)

print_channel_statistics(red, "Red")
print_channel_statistics(green, "Green")
print_channel_statistics(blue, "Blue")

generate_conversions(
    "images/HW1_IMG.png",
    "results/converted"
)

create_affine_transformations(
    "results/converted",
    "results/transformed"
)

apply_gaussian_blurs(
    [
        "results/converted",
        "results/transformed"
    ],
    "results/blurred"
)
create_subsets()