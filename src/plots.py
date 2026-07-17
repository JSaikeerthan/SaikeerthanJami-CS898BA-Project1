"""
plots.py

Creates plots for training history and confusion matrix.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay


def plot_history(history, filename, title):
    """
    Plot training and validation accuracy/loss.
    """

    Path("outputs/plots").mkdir(parents=True, exist_ok=True)

    # Accuracy
    plt.figure(figsize=(8,5))
    plt.plot(history.history["accuracy"], label="Training")
    plt.plot(history.history["val_accuracy"], label="Validation")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title(title + " Accuracy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"outputs/plots/{filename}_accuracy.png")
    plt.close()

    # Loss
    plt.figure(figsize=(8,5))
    plt.plot(history.history["loss"], label="Training")
    plt.plot(history.history["val_loss"], label="Validation")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title(title + " Loss")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"outputs/plots/{filename}_loss.png")
    plt.close()


def plot_confusion_matrix(matrix, class_names, filename):
    """
    Save confusion matrix figure.
    """

    plt.figure(figsize=(8,8))

    ConfusionMatrixDisplay(
        confusion_matrix=np.array(matrix),
        display_labels=class_names
    ).plot(cmap="Blues", values_format="d")

    plt.title("Confusion Matrix")

    plt.tight_layout()

    plt.savefig(f"outputs/plots/{filename}.png")

    plt.close()