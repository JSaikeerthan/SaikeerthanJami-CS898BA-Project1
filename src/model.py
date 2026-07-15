"""
model.py

Defines the baseline CNN architecture for fish classification.
"""

import tensorflow as tf


def build_model(num_classes):
    """
    Build and compile the baseline CNN.

    Parameters
    ----------
    num_classes : int
        Number of fish classes.

    Returns
    -------
    tf.keras.Model
        Compiled CNN model.
    """

    model = tf.keras.Sequential(

        [

            tf.keras.layers.Input(shape=(128, 128, 3)),

            # Block 1
            tf.keras.layers.Conv2D(
                32,
                (3, 3),
                activation="relu",
                padding="same"
            ),

            tf.keras.layers.MaxPooling2D(),

            # Block 2
            tf.keras.layers.Conv2D(
                64,
                (3, 3),
                activation="relu",
                padding="same"
            ),

            tf.keras.layers.MaxPooling2D(),

            # Block 3
            tf.keras.layers.Conv2D(
                128,
                (3, 3),
                activation="relu",
                padding="same"
            ),

            tf.keras.layers.MaxPooling2D(),

            # Flatten feature maps
            tf.keras.layers.Flatten(),

            # Fully connected layer
            tf.keras.layers.Dense(
                128,
                activation="relu"
            ),

            # Dropout helps reduce overfitting
            tf.keras.layers.Dropout(0.30),

            # Output layer
            tf.keras.layers.Dense(
                num_classes,
                activation="softmax"
            )

        ]

    )

    model.compile(

        optimizer=tf.keras.optimizers.Adam(
            learning_rate=0.001
        ),

        loss="sparse_categorical_crossentropy",

        metrics=["accuracy"]

    )

    return model