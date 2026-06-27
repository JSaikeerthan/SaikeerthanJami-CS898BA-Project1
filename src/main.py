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

otsu_iou, otsu_dice = evaluate(
    otsu_mask,
    ground_truth
)

adaptive_iou, adaptive_dice = evaluate(
    adaptive_mask,
    ground_truth
)

kmeans_iou, kmeans_dice = evaluate(
    kmeans_mask,
    ground_truth
)

print("\nSegmentation Evaluation")
print("-" * 40)

print(f"Otsu IoU: {otsu_iou:.4f}")
print(f"Otsu Dice: {otsu_dice:.4f}")

print(f"Adaptive IoU: {adaptive_iou:.4f}")
print(f"Adaptive Dice: {adaptive_dice:.4f}")

print(f"KMeans IoU: {kmeans_iou:.4f}")
print(f"KMeans Dice: {kmeans_dice:.4f}")