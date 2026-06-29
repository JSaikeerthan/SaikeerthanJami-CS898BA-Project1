import cv2
import numpy as np


def kmeans_segmentation(image, k=4):

    """
    Perform K-Means clustering in HSV color space.

    Parameters:
        image (numpy.ndarray): Normalized image.
        k (int): Number of clusters.

    Returns:
        mask (numpy.ndarray): Binary mask of selected cluster.
    """

    # Convert image to HSV color space
    hsv = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2HSV
    )
    
    # Reshape image into pixel vectors
    pixels = hsv.reshape((-1, 3))
    pixels = np.float32(pixels)
    
    # Set K-Means termination criteria
    criteria = (
        cv2.TERM_CRITERIA_EPS +
        cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2
    )

    # Perform clustering
    _, labels, centers = cv2.kmeans(
        pixels,
        k,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    # Flatten cluster labels
    labels = labels.flatten()

    # Select darkest cluster as figure candidate
    cluster = np.argmin(
        np.sum(centers, axis=1)
    )

    # Create binary mask
    mask = np.uint8(
        labels == cluster
    ) * 255

    mask = mask.reshape(
        image.shape[:2]
    )

    # Extract segmented foreground
    foreground = cv2.bitwise_and(
        image,
        image,
        mask=mask
    )

    # Save results
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