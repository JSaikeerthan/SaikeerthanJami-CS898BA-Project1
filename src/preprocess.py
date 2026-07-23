"""
preprocess.py

Generates the three input channels required for the
Advanced Segmentation extra credit assignment.

Channel A:
    Original RGB image

Channel B:
    HSV V-channel normalized image

Channel C:
    RGB image with each channel independently normalized
"""

import cv2
import numpy as np


def load_image(path):
    """
    Load image in RGB format.
    """
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Cannot load image: {path}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


def channel_a(image):
    """
    Channel A

    Return original RGB image.
    """
    return image.copy()


def channel_b(image):
    """
    Channel B

    Normalize only the V channel in HSV.
    """

    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    h, s, v = cv2.split(hsv)

    v = cv2.normalize(v, None, 0, 255, cv2.NORM_MINMAX)

    hsv = cv2.merge([h, s, v])

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)


def channel_c(image):
    """
    Channel C

    Normalize each RGB channel independently.
    """

    channels = cv2.split(image)

    normalized = []

    for c in channels:
        c = cv2.normalize(
            c,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        )

        normalized.append(c)

    return cv2.merge(normalized)


def save_outputs(original, hsv_image, rgb_image):
    """
    Save preprocessing outputs.
    """

    cv2.imwrite(
        "outputs/channel_a_original.png",
        cv2.cvtColor(original, cv2.COLOR_RGB2BGR)
    )

    cv2.imwrite(
        "outputs/channel_b_hsv.png",
        cv2.cvtColor(hsv_image, cv2.COLOR_RGB2BGR)
    )

    cv2.imwrite(
        "outputs/channel_c_rgb.png",
        cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    )


if __name__ == "__main__":

    image = load_image("images/HW1_IMG.png")

    original = channel_a(image)

    hsv_image = channel_b(image)

    rgb_image = channel_c(image)

    save_outputs(
        original,
        hsv_image,
        rgb_image
    )

    print("Preprocessing complete.")