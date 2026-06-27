import numpy as np


def evaluate(mask, ground_truth):

    mask = mask > 0
    ground_truth = ground_truth > 0

    intersection = np.logical_and(mask,ground_truth)

    union = np.logical_or(mask,ground_truth)

    iou = np.sum(intersection) / np.sum(union)

    dice = (
        2 * np.sum(intersection)
    ) / (
        np.sum(mask) + np.sum(ground_truth)
    )

    return iou, dice