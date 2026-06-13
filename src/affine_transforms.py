import cv2
import numpy as np
import os


def rotate_image(image, angle):
    h, w = image.shape[:2]

    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    return cv2.warpAffine(
        image,
        matrix,
        (w, h)
    )


def translate_image(image, tx, ty):
    h, w = image.shape[:2]

    matrix = np.float32([
        [1, 0, tx],
        [0, 1, ty]
    ])

    return cv2.warpAffine(
        image,
        matrix,
        (w, h)
    )


def create_affine_transformations(
    input_dir,
    output_dir
):
    os.makedirs(output_dir, exist_ok=True)

    image_files = [
        f for f in os.listdir(input_dir)
        if f.endswith(".png")
    ]

    for index, filename in enumerate(image_files):

        path = os.path.join(
            input_dir,
            filename
        )

        image = cv2.imread(path)

        if image is None:
            continue

        # Unique rotation
        angle = 15 + (index * 23)

        rotated = rotate_image(
            image,
            angle
        )

        cv2.imwrite(
            os.path.join(
                output_dir,
                f"{filename[:-4]}_rotated.png"
            ),
            rotated
        )

        # Unique translation
        tx = 10 + (index * 5)
        ty = 15 + (index * 7)

        translated = translate_image(
            image,
            tx,
            ty
        )

        cv2.imwrite(
            os.path.join(
                output_dir,
                f"{filename[:-4]}_translated.png"
            ),
            translated
        )

    print("Affine transformations complete.")