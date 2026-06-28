import cv2
import matplotlib.pyplot as plt


def create_plot(original,
                normalized,
                otsu,
                adaptive,
                kmeans,
                ground_truth):

    images = [
        cv2.cvtColor(original, cv2.COLOR_BGR2RGB),
        cv2.cvtColor(normalized, cv2.COLOR_BGR2RGB),
        otsu,
        adaptive,
        kmeans,
        ground_truth
    ]

    titles = [
        "Original",
        "Normalized",
        "Otsu",
        "Adaptive",
        "KMeans",
        "Ground Truth"
    ]

    plt.figure(figsize=(18, 10))

    for i in range(6):

        plt.subplot(2, 3, i + 1)

        if i < 2:
            plt.imshow(images[i])
        else:
            plt.imshow(images[i], cmap="gray")

        plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        "results/evaluation/comparison_plot.png"
    )

    plt.close()