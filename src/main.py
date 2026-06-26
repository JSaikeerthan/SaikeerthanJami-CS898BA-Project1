import cv2
from normalization import normalize_channels
from threshold_segmentation import threshold_segmentation
from kmeans_segmentation import kmeans_segmentation


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