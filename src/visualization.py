"""
visualization.py

Creates the comparison figure required for the
Advanced Segmentation extra credit assignment.
"""

import os
import cv2
import matplotlib.pyplot as plt

# -------------------------------------------------
# Create output directory
# -------------------------------------------------

os.makedirs("outputs", exist_ok=True)

# -------------------------------------------------
# Image information
# -------------------------------------------------

images = [
    ("Original RGB", "outputs/channel_a_original.png"),
    ("HSV V Normalized", "outputs/channel_b_hsv.png"),
    ("RGB Normalized", "outputs/channel_c_rgb.png"),
    ("Segmentation A\nIoU: 0.6221\nDice: 0.7670",
     "outputs/overlays/channel_a_overlay.png"),
    ("Segmentation B\nIoU: 0.6218\nDice: 0.7668",
     "outputs/overlays/channel_b_overlay.png"),
    ("Segmentation C\nIoU: 0.6221\nDice: 0.7670",
     "outputs/overlays/channel_c_overlay.png"),
    ("Ground Truth", "images/ground_truth.png"),
]

# -------------------------------------------------
# Create figure
# -------------------------------------------------

plt.figure(figsize=(28, 5))

for i, (title, path) in enumerate(images):

    image = cv2.imread(path)

    if image is None:
        print(f"Unable to load {path}")
        continue

    # Convert color images
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 7, i + 1)

    if len(image.shape) == 2:
        plt.imshow(image, cmap="gray")
    else:
        plt.imshow(image)

    plt.title(title, fontsize=11)
    plt.axis("off")

# -------------------------------------------------
# Save figure
# -------------------------------------------------

plt.tight_layout()

plt.savefig(
    "outputs/comparison_plot.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()

print("\nComparison figure saved to:")
print("outputs/comparison_plot.png")