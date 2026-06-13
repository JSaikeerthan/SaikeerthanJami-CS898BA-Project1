import cv2
import numpy as np
import os


def generate_conversions(image_path, output_dir):
    image = cv2.imread(image_path)

    os.makedirs(output_dir, exist_ok=True)

    # Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{output_dir}/grayscale.png", gray)

    # Binary
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f"{output_dir}/binary.png", binary)

    # HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite(f"{output_dir}/hsv.png", hsv)

    # LAB
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imwrite(f"{output_dir}/lab.png", lab)

    # HLS
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    cv2.imwrite(f"{output_dir}/hls.png", hls)

    # Histogram Equalization on V channel
    hsv_norm = hsv.copy()
    hsv_norm[:, :, 2] = cv2.equalizeHist(hsv_norm[:, :, 2])

    normalized_rgb = cv2.cvtColor(hsv_norm, cv2.COLOR_HSV2BGR)

    cv2.imwrite(
        f"{output_dir}/normalized_rgb.png",
        normalized_rgb
    )

    print("Conversion images saved.")