import numpy as np


def evaluate(mask, ground_truth):

    """
    Calculate IoU and Dice Coefficient.

    Parameters:
        mask (numpy.ndarray): Segmentation mask.
        ground_truth (numpy.ndarray): Reference mask.

    Returns:
        iou (float): Intersection over Union.
        dice (float): Dice coefficient.
    """

    # Convert masks to boolean values
    mask = mask > 0
    ground_truth = ground_truth > 0

    # Compute intersection and union
    intersection = np.logical_and(mask,ground_truth)

    union = np.logical_or(mask,ground_truth)

    # Calculate IoU
    iou = np.sum(intersection) / np.sum(union)

    # Calculate Dice coefficient
    dice = (
        2 * np.sum(intersection)
    ) / (
        np.sum(mask) + np.sum(ground_truth)
    )

    return iou, dice