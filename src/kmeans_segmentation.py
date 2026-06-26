import cv2
import numpy as np


def kmeans_segmentation(image, k=4):

    hsv = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2HSV
    )

    pixels = hsv.reshape((-1, 3))
    pixels = np.float32(pixels)

    criteria = (
        cv2.TERM_CRITERIA_EPS +
        cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2
    )

    _, labels, centers = cv2.kmeans(
        pixels,
        k,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    labels = labels.flatten()

    cluster = np.argmin(
        np.sum(centers, axis=1)
    )

    mask = np.uint8(
        labels == cluster
    ) * 255

    mask = mask.reshape(
        image.shape[:2]
    )

    foreground = cv2.bitwise_and(
        image,
        image,
        mask=mask
    )

    cv2.imwrite(
        "results/segmentation/masks/kmeans.png",
        mask
    )

    cv2.imwrite(
        "results/segmentation/foregrounds/kmeans_foreground.png",
        foreground
    )

    print("K-means segmentation complete.")

    return mask