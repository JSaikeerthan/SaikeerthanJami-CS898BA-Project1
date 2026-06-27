import cv2
from normalization import normalize_channels
from threshold_segmentation import threshold_segmentation
from kmeans_segmentation import kmeans_segmentation
from metrics import evaluate


normalized = normalize_channels(
    "images/HW1_IMG.png",
    "results/segmentation/normalized.png"
)

otsu_mask, adaptive_mask = threshold_segmentation(
    normalized
)

kmeans_mask = kmeans_segmentation(
    normalized,
    k=4
)

ground_truth = cv2.imread(
    "results/evaluation/ground_truth.png",
    cv2.IMREAD_GRAYSCALE
)

iou, dice = evaluate(
    kmeans_mask,
    ground_truth
)

print(f"KMeans IoU: {iou:.4f}")
print(f"KMeans Dice: {dice:.4f}")