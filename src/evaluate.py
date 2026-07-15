"""
evaluate.py

Evaluates trained CNN models on the test dataset.
"""

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


def evaluate_model(model, test_ds):
    """
    Evaluate a trained model on the test dataset.

    Parameters
    ----------
    model : tf.keras.Model
    test_ds : tf.data.Dataset

    Returns
    -------
    metrics : dict
    """

    y_true = []
    y_pred = []

    for images, labels in test_ds:

        predictions = model.predict(
            images,
            verbose=0
        )

        predicted = np.argmax(
            predictions,
            axis=1
        )

        y_true.extend(labels.numpy())
        y_pred.extend(predicted)

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        average="weighted"
    )

    recall = recall_score(
        y_true,
        y_pred,
        average="weighted"
    )

    f1 = f1_score(
        y_true,
        y_pred,
        average="weighted"
    )

    matrix = confusion_matrix(
        y_true,
        y_pred
    )

    print("\nClassification Report")
    print(classification_report(
        y_true,
        y_pred
    ))

    print("\nAccuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "matrix": matrix,
    }