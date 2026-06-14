import cv2
import os
import random
import shutil
import matplotlib.pyplot as plt


INPUT_FOLDER = "results/subsets/subset1"

SOBEL_FOLDER = "results/edges/sobel"
LAPLACIAN_FOLDER = "results/edges/laplacian"
CANNY_FOLDER = "results/edges/canny"
PREWITT_FOLDER = "results/edges/prewitt"

PLOT_FOLDER = "results/plots"
README_FOLDER = "results/plots/readme_plots"


def generate_plots():

    os.makedirs(PLOT_FOLDER, exist_ok=True)
    os.makedirs(README_FOLDER, exist_ok=True)

    image_files = sorted(
        [
            f for f in os.listdir(INPUT_FOLDER)
            if f.endswith(".png")
        ]
    )

    plot_files = []

    for filename in image_files:

        original = cv2.imread(
            os.path.join(INPUT_FOLDER, filename)
        )
        original = cv2.cvtColor(
            original,
            cv2.COLOR_BGR2RGB
        )

        sobel = cv2.imread(
            os.path.join(SOBEL_FOLDER, filename),
            cv2.IMREAD_GRAYSCALE
        )

        laplacian = cv2.imread(
            os.path.join(LAPLACIAN_FOLDER, filename),
            cv2.IMREAD_GRAYSCALE
        )

        canny = cv2.imread(
            os.path.join(CANNY_FOLDER, filename),
            cv2.IMREAD_GRAYSCALE
        )

        prewitt = cv2.imread(
            os.path.join(PREWITT_FOLDER, filename),
            cv2.IMREAD_GRAYSCALE
        )

        fig, ax = plt.subplots(
            1,
            5,
            figsize=(20, 5)
        )

        ax[0].imshow(original)
        ax[0].set_title("Original")

        ax[1].imshow(sobel, cmap="gray")
        ax[1].set_title("Sobel")

        ax[2].imshow(laplacian, cmap="gray")
        ax[2].set_title("Laplacian")

        ax[3].imshow(canny, cmap="gray")
        ax[3].set_title("Canny")

        ax[4].imshow(prewitt, cmap="gray")
        ax[4].set_title("Prewitt")

        for a in ax:
            a.axis("off")

        plt.tight_layout()

        plot_name = (
            filename.replace(".png", "_plot.png")
        )

        plot_path = os.path.join(
            PLOT_FOLDER,
            plot_name
        )

        plt.savefig(plot_path)
        plt.close()

        plot_files.append(plot_path)

    # Choosing 6 random plots for README

    random.seed(42)

    selected = random.sample(
        plot_files,
        6
    )

    for plot in selected:
        shutil.copy(
            plot,
            README_FOLDER
        )

    print("Plots generated successfully.")