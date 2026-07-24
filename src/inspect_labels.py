import numpy as np
import cv2
import os

mask = np.load("outputs/masks/channel_a_labels.npy")

os.makedirs("outputs/debug_classes", exist_ok=True)

for cls in np.unique(mask):
    binary = np.where(mask == cls, 255, 0).astype(np.uint8)
    cv2.imwrite(f"outputs/debug_classes/class_{cls}.png", binary)
    print(f"Saved class_{cls}.png")