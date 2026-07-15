"""
tuner.py

Hyperparameter tuning using KerasTuner Random Search.
"""

import keras_tuner as kt
import tensorflow as tf
from pathlib import Path


def build_hypermodel(hp, num_classes):
    """
    Build a CNN model with tunable hyperparameters.

    Parameters
    ----------
    hp : HyperParameters
    num_classes : int

    Returns
    -------
    tf.keras.Model
    """

    model = tf.keras.Sequential([

        tf.keras.layers.Input(shape=(128, 128, 3)),

        tf.keras.layers.Conv2D(
            32,
            (3,3),
            activation="relu",
            padding="same"
        ),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Conv2D(
            64,
            (3,3),
            activation="relu",
            padding="same"
        ),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Conv2D(
            128,
            (3,3),
            activation="relu",
            padding="same"
        ),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(

            units=hp.Choice(
                "dense_units",
                values=[128,256]
            ),

            activation="relu"

        ),

        tf.keras.layers.Dropout(

            hp.Choice(
                "dropout",
                values=[0.3,0.5]
            )

        ),

        tf.keras.layers.Dense(
            num_classes,
            activation="softmax"
        )

    ])

    learning_rate = hp.Choice(
        "learning_rate",
        values=[0.01,0.001,0.0001]
    )

    model.compile(

        optimizer=tf.keras.optimizers.Adam(
            learning_rate=learning_rate
        ),

        loss="sparse_categorical_crossentropy",

        metrics=["accuracy"]

    )

    return model


def tune_model(train_ds, val_ds, num_classes):

    Path("outputs/models").mkdir(
        parents=True,
        exist_ok=True
    )

    tuner = kt.RandomSearch(

        lambda hp: build_hypermodel(
            hp,
            num_classes
        ),

        objective="val_loss",

        max_trials=6,

        overwrite=True,

        directory="outputs",

        project_name="keras_tuner"

    )

    tuner.search(

        train_ds,

        validation_data=val_ds,

        epochs=8

    )

    best_hp = tuner.get_best_hyperparameters(1)[0]

    print("\nBest Hyperparameters")

    print(best_hp.values)

    model = tuner.hypermodel.build(
        best_hp
    )

    history = model.fit(

        train_ds,

        validation_data=val_ds,

        epochs=20

    )

    model.save(
        "outputs/models/best_model.keras"
    )

    return model, history, best_hp