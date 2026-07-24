"""
segmentation.py

Runs SegFormer semantic segmentation on the three
preprocessed input channels.
"""

import os
import cv2
import numpy as np
import torch

from PIL import Image

from transformers import (
    SegformerImageProcessor,
    SegformerForSemanticSegmentation,
)

# -------------------------------------------------
# Load pretrained SegFormer
# -------------------------------------------------

processor = SegformerImageProcessor.from_pretrained(
    "nvidia/segformer-b0-finetuned-ade-512-512"
)

model = SegformerForSemanticSegmentation.from_pretrained(
    "nvidia/segformer-b0-finetuned-ade-512-512"
)

model.eval()


# -------------------------------------------------
# Run inference
# -------------------------------------------------

def segment_image(image_path):

    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits

    upsampled_logits = torch.nn.functional.interpolate(
        logits,
        size=image.size[::-1],
        mode="bilinear",
        align_corners=False,
    )

    prediction = upsampled_logits.argmax(dim=1)[0]

    return prediction.numpy()


# -------------------------------------------------
# Save mask
# -------------------------------------------------

def save_mask(mask, name):
    """
    Save both visualization and raw prediction.
    """

    # Save raw labels
    np.save(
        f"outputs/masks/{name}_labels.npy",
        mask
    )

    # Save visualization
    visualization = (
        mask * (255 // max(mask.max(), 1))
    ).astype(np.uint8)

    cv2.imwrite(
        f"outputs/masks/{name}_mask.png",
        visualization
    )


# -------------------------------------------------
# Create overlay
# -------------------------------------------------

def create_overlay(image_path, mask, output_path):

    image = cv2.imread(image_path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    color_mask = cv2.applyColorMap(
        (mask * (255 // max(mask.max(), 1))).astype(np.uint8),
        cv2.COLORMAP_JET,
    )

    overlay = cv2.addWeighted(
        image,
        0.6,
        color_mask,
        0.4,
        0,
    )

    overlay = cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR)

    cv2.imwrite(output_path, overlay)


# -------------------------------------------------
# Process all channels
# -------------------------------------------------

def process(image_path, name):

    print(f"Running SegFormer on {name}...")

    mask = segment_image(image_path)

    save_mask(mask, name)

    create_overlay(
        image_path,
        mask,
        f"outputs/overlays/{name}_overlay.png",
    )

    print(f"{name} complete.")


if __name__ == "__main__":

    os.makedirs("outputs/masks", exist_ok=True)
    os.makedirs("outputs/overlays", exist_ok=True)

    process(
        "outputs/channel_a_original.png",
        "channel_a",
    )

    process(
        "outputs/channel_b_hsv.png",
        "channel_b",
    )

    process(
        "outputs/channel_c_rgb.png",
        "channel_c",
    )

    print("\nSegmentation complete.")