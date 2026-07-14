"""
data_loader.py

Loads the fish dataset, applies preprocessing and data augmentation,
and creates TensorFlow datasets for training, validation, and testing.
"""

import tensorflow as tf
from sklearn.model_selection import train_test_split
from pathlib import Path


IMG_SIZE = (128, 128)
BATCH_SIZE = 32
SEED = 42


def load_datasets(dataset_path):
    """
    Load the fish dataset and split it into training,
    validation, and testing datasets.

    Parameters
    ----------
    dataset_path : str
        Path to the fish dataset.

    Returns
    -------
    train_ds
    val_ds
    test_ds
    class_names
    """

    image_paths = []
    labels = []
    class_names = sorted(
        [folder.name for folder in Path(dataset_path).iterdir() if folder.is_dir()]
    )

    # Read every image path and assign its class label
    for label, class_name in enumerate(class_names):

        class_folder = Path(dataset_path) / class_name

        for image in class_folder.glob("*"):

            image_paths.append(str(image))
            labels.append(label)

    # 70% train / 30% temporary
    train_paths, temp_paths, train_labels, temp_labels = train_test_split(
        image_paths,
        labels,
        test_size=0.30,
        stratify=labels,
        random_state=SEED,
    )

    # Split remaining 30% into validation and testing
    val_paths, test_paths, val_labels, test_labels = train_test_split(
        temp_paths,
        temp_labels,
        test_size=0.50,
        stratify=temp_labels,
        random_state=SEED,
    )

    print(f"Training Images: {len(train_paths)}")
    print(f"Validation Images: {len(val_paths)}")
    print(f"Testing Images: {len(test_paths)}")

    train_ds = create_dataset(
        train_paths,
        train_labels,
        augment=True,
    )

    val_ds = create_dataset(
        val_paths,
        val_labels,
        augment=False,
    )

    test_ds = create_dataset(
        test_paths,
        test_labels,
        augment=False,
    )

    return train_ds, val_ds, test_ds, class_names


def preprocess_image(image_path, label):
    """
    Read, resize, and normalize an image.
    """

    image = tf.io.read_file(image_path)

    image = tf.image.decode_jpeg(
        image,
        channels=3,
    )

    image = tf.image.resize(
        image,
        IMG_SIZE,
    )

    image = image / 255.0

    return image, label


def augment_image(image, label):
    """
    Apply data augmentation to training images.
    """

    image = tf.image.random_flip_left_right(image)

    image = tf.image.random_brightness(
        image,
        max_delta=0.20,
    )

    image = tf.image.random_contrast(
        image,
        lower=0.8,
        upper=1.2,
    )

    return image, label


def create_dataset(paths, labels, augment=False):
    """
    Create a TensorFlow dataset.
    """

    dataset = tf.data.Dataset.from_tensor_slices(
        (paths, labels)
    )

    dataset = dataset.map(
        preprocess_image,
        num_parallel_calls=tf.data.AUTOTUNE,
    )

    if augment:

        dataset = dataset.map(
            augment_image,
            num_parallel_calls=tf.data.AUTOTUNE,
        )

    dataset = dataset.shuffle(1000)

    dataset = dataset.batch(BATCH_SIZE)

    dataset = dataset.prefetch(
        tf.data.AUTOTUNE
    )

    return dataset