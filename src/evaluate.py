"""
evaluate.py

Evaluates SegFormer segmentation results using
IoU and Dice Coefficient against the HW2 ground truth.
"""

import os
import cv2
import numpy as np

# -------------------------------------------------
# Configuration
# -------------------------------------------------

GROUND_TRUTH = "images/ground_truth.png"

# Class corresponding to the person in the SegFormer output
PERSON_CLASS = 12


# -------------------------------------------------
# Load Ground Truth
# -------------------------------------------------

def load_ground_truth():
    """
    Load the binary ground truth mask.
    """

    gt = cv2.imread(GROUND_TRUTH, cv2.IMREAD_GRAYSCALE)

    if gt is None:
        raise FileNotFoundError(
            f"Ground truth not found: {GROUND_TRUTH}"
        )

    _, gt = cv2.threshold(
        gt,
        127,
        255,
        cv2.THRESH_BINARY
    )

    return gt > 0


# -------------------------------------------------
# Load Prediction
# -------------------------------------------------

def load_prediction(label_path):
    """
    Convert SegFormer class labels into
    a binary mask representing the person.
    """

    labels = np.load(label_path)

    prediction = (labels == PERSON_CLASS)

    return prediction


# -------------------------------------------------
# Metrics
# -------------------------------------------------

def iou(prediction, ground_truth):
    """
    Compute Intersection over Union.
    """

    intersection = np.logical_and(
        prediction,
        ground_truth
    ).sum()

    union = np.logical_or(
        prediction,
        ground_truth
    ).sum()

    if union == 0:
        return 0.0

    return intersection / union


def dice(prediction, ground_truth):
    """
    Compute Dice Coefficient.
    """

    intersection = np.logical_and(
        prediction,
        ground_truth
    ).sum()

    denominator = prediction.sum() + ground_truth.sum()

    if denominator == 0:
        return 0.0

    return (2 * intersection) / denominator


# -------------------------------------------------
# Evaluate
# -------------------------------------------------

def evaluate(label_path):
    """
    Evaluate one prediction.
    """

    prediction = load_prediction(label_path)

    ground_truth = load_ground_truth()

    return (
        iou(prediction, ground_truth),
        dice(prediction, ground_truth),
    )


# -------------------------------------------------
# Main
# -------------------------------------------------

if __name__ == "__main__":

    os.makedirs(
        "outputs/metrics",
        exist_ok=True
    )

    channels = [
        "channel_a",
        "channel_b",
        "channel_c",
    ]

    output_file = "outputs/metrics/results.txt"

    with open(output_file, "w") as f:

        for channel in channels:

            label_path = (
                f"outputs/masks/{channel}_labels.npy"
            )

            iou_score, dice_score = evaluate(label_path)

            print(channel)
            print(f"IoU : {iou_score:.4f}")
            print(f"Dice: {dice_score:.4f}")
            print()

            f.write(f"{channel}\n")
            f.write(f"IoU : {iou_score:.4f}\n")
            f.write(f"Dice: {dice_score:.4f}\n\n")

    print("Evaluation complete.")