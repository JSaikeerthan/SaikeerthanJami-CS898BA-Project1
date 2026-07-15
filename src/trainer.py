"""
trainer.py

Handles training and saving the CNN model.
"""

import json
from pathlib import Path


def train_model(
    model,
    train_ds,
    val_ds,
    epochs=20
):
    """
    Train the CNN model.

    Parameters
    ----------
    model : tf.keras.Model
    train_ds
    val_ds
    epochs : int

    Returns
    -------
    history
    """

    history = model.fit(

        train_ds,

        validation_data=val_ds,

        epochs=epochs

    )

    # Create output folders
    Path("outputs/models").mkdir(
        parents=True,
        exist_ok=True
    )

    Path("outputs/history").mkdir(
        parents=True,
        exist_ok=True
    )

    # Save model
    model.save(
        "outputs/models/baseline_cnn.keras"
    )

    # Save training history
    history_path = Path(
        "outputs/history/training_history.json"
    )

    with open(history_path, "w") as file:

        json.dump(
            history.history,
            file,
            indent=4
        )

    print("\nTraining complete.")

    print("Model saved.")

    return history