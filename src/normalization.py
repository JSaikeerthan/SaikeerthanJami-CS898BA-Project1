import cv2


def normalize_channels(image_path, output_path):

    """
    Apply histogram equalization independently to
    each RGB channel to improve image contrast.

    Parameters:
        image_path (str): Path to input image.
        output_path (str): Path to save normalized image.

    Returns:
        normalized (numpy.ndarray): Equalized color image.
    """
# Load original image
    image = cv2.imread(image_path)

    if image is None:
        raise Exception("Image not found.")
    
# Split image into individual color channels
    blue, green, red = cv2.split(image)

# Perform histogram equalization on each channel
    blue_eq = cv2.equalizeHist(blue)
    green_eq = cv2.equalizeHist(green)
    red_eq = cv2.equalizeHist(red)

 # Merge equalized channels
    normalized = cv2.merge(
        [blue_eq, green_eq, red_eq]
    )

 # Save normalized image
    cv2.imwrite(
        output_path,
        normalized
    )

    print("Normalized image saved.")

    return normalized