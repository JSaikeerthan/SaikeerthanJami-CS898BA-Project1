import cv2
from image_statistics import print_channel_statistics
from conversions import generate_conversions
from affine_transforms import create_affine_transformations
from gaussian_blur import apply_gaussian_blurs
from create_subsets import create_subsets
from edge_detection import detect_edges
from plot_results import generate_plots
from normalization import normalize_channels
from threshold_segmentation import threshold_segmentation

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

detect_edges()

generate_plots()

normalized = normalize_channels(
    "images/HW1_IMG.png",
    "results/segmentation/normalized.png"
)

otsu_mask, adaptive_mask = threshold_segmentation(
    normalized
)