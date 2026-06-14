import cv2
import numpy as np
import os


INPUT_FOLDER = "results/subsets/subset1"


def detect_edges():

    methods = {
        "sobel": "results/edges/sobel",
        "laplacian": "results/edges/laplacian",
        "canny": "results/edges/canny",
        "prewitt": "results/edges/prewitt"
    }

    for folder in methods.values():
        os.makedirs(folder, exist_ok=True)

    for filename in os.listdir(INPUT_FOLDER):

        if not filename.endswith(".png"):
            continue

        path = os.path.join(
            INPUT_FOLDER,
            filename
        )

        image = cv2.imread(path)

        if image is None:
            continue

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )


        # Sobel edge detection

        sx = cv2.Sobel(
            gray,
            cv2.CV_64F,
            1,
            0,
            ksize=3
        )

        sy = cv2.Sobel(
            gray,
            cv2.CV_64F,
            0,
            1,
            ksize=3
        )

        sobel = cv2.magnitude(
            sx,
            sy
        )

        sobel = np.uint8(
            np.clip(sobel, 0, 255)
        )

        cv2.imwrite(
            os.path.join(
                methods["sobel"],
                filename
            ),
            sobel
        )


        # Laplacian edge detection

        laplacian = cv2.Laplacian(
            gray,
            cv2.CV_64F
        )

        laplacian = np.uint8(
            np.absolute(laplacian)
        )

        cv2.imwrite(
            os.path.join(
                methods["laplacian"],
                filename
            ),
            laplacian
        )


        # Canny edge detection

        canny = cv2.Canny(
            gray,
            100,
            200
        )

        cv2.imwrite(
            os.path.join(
                methods["canny"],
                filename
            ),
            canny
        )


        # Prewitt edge detection

        kernelx = np.array([
            [1, 0, -1],
            [1, 0, -1],
            [1, 0, -1]
        ])

        kernely = np.array([
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1]
        ])

        px = cv2.filter2D(
            gray,
            -1,
            kernelx
        )

        py = cv2.filter2D(
            gray,
            -1,
            kernely
        )

        prewitt = cv2.addWeighted(
            px,
            0.5,
            py,
            0.5,
            0
        )

        cv2.imwrite(
            os.path.join(
                methods["prewitt"],
                filename
            ),
            prewitt
        )

    print("Edge detection complete.")