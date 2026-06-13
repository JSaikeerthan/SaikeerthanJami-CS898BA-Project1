import cv2
import os


SIGMAS = [
    0.5,
    1.0,
    1.5,
    2.0,
    2.5,
    3.0,
    3.5
]


def apply_gaussian_blurs(
    input_dirs,
    output_dir
):
    os.makedirs(output_dir, exist_ok=True)

    image_paths = []

    for directory in input_dirs:

        for filename in os.listdir(directory):

            if filename.endswith(".png"):

                image_paths.append(
                    os.path.join(
                        directory,
                        filename
                    )
                )

    for image_path in image_paths:

        image = cv2.imread(image_path)

        if image is None:
            continue

        base_name = os.path.splitext(
            os.path.basename(image_path)
        )[0]

        for sigma in SIGMAS:

            blurred = cv2.GaussianBlur(
                image,
                (0, 0),
                sigma
            )

            output_file = (
                f"{base_name}_sigma_{sigma}.png"
            )

            cv2.imwrite(
                os.path.join(
                    output_dir,
                    output_file
                ),
                blurred
            )

    print("Gaussian blur generation complete.")