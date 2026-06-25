import cv2


def normalize_channels(image_path, output_path):

    image = cv2.imread(image_path)

    if image is None:
        raise Exception("Image not found.")

    blue, green, red = cv2.split(image)

    blue_eq = cv2.equalizeHist(blue)
    green_eq = cv2.equalizeHist(green)
    red_eq = cv2.equalizeHist(red)

    normalized = cv2.merge(
        [blue_eq, green_eq, red_eq]
    )

    cv2.imwrite(
        output_path,
        normalized
    )

    print("Normalized image saved.")

    return normalized