import cv2


def threshold_segmentation(image):
    """
     Perform Otsu and Adaptive threshold segmentation.

     Parameters:
           image (numpy.ndarray): Normalized color image.

    Returns:
           otsu (numpy.ndarray): Otsu binary mask.
           adaptive (numpy.ndarray): Adaptive binary mask. 
    """

    # Convert image to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Otsu Threshold
    
    _, otsu = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY +
        cv2.THRESH_OTSU
    )

    # Adaptive Gaussian Threshold

    adaptive = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        51,
        2
    )

     # Save binary masks

    cv2.imwrite(
        "results/segmentation/masks/otsu.png",
        otsu
    )

    cv2.imwrite(
        "results/segmentation/masks/adaptive.png",
        adaptive
    )

# Extract foreground regions
    foreground_otsu = cv2.bitwise_and(
        image,
        image,
        mask=otsu
    )

    foreground_adaptive = cv2.bitwise_and(
        image,
        image,
        mask=adaptive
    )

# Save extracted foreground images
    cv2.imwrite(
        "results/segmentation/foregrounds/otsu_foreground.png",
        foreground_otsu
    )

    cv2.imwrite(
        "results/segmentation/foregrounds/adaptive_foreground.png",
        foreground_adaptive
    )

    print("Threshold segmentation complete.")

    return otsu, adaptive