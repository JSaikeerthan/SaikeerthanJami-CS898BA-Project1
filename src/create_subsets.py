import os
import random
import shutil


def create_subsets():

    all_images = []

    for root, dirs, files in os.walk("results"):

        if "subsets" in root:
            continue

        for file in files:

            if file.endswith(".png"):

                all_images.append(
                    os.path.join(root, file)
                )

    print(f"Found {len(all_images)} images")

    random.seed(42)

    random.shuffle(all_images)

    subset_size = 42

    subset_folders = [
        "results/subsets/subset1",
        "results/subsets/subset2",
        "results/subsets/subset3",
        "results/subsets/subset4"
    ]

    for i, folder in enumerate(subset_folders):

        subset = all_images[
            i * subset_size:
            (i + 1) * subset_size
        ]

        for image_path in subset:

            shutil.copy(
                image_path,
                folder
            )

    print("Subsets created successfully.")