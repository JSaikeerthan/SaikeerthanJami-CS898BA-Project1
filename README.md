# Homework 2: Image Segmentation

**Course:** CS 898BA – Image Analysis and Computer Vision
**Student:** Saikeerthan Jami
**Repository:** SaikeerthanJami-CS898BA-Project1
**Branch:** Feature-Segmentation

---

# Project Overview

The objective of Homework 2 is to investigate several classical image segmentation techniques to isolate the unknown figure present in the original low-light doorbell camera image.

The assignment focuses on:

* Multi-channel color normalization
* Threshold-based segmentation
* Color-space clustering
* Quantitative evaluation
* Qualitative analysis

The final objective is to isolate the figure from the background and compare segmentation performance using both visual analysis and numerical evaluation metrics.

---

# Repository Structure

```text
images/
src/
results/
    segmentation/
        masks/
        foregrounds/
    evaluation/

README.md
AI_Log.md
requirements.txt
```

---

# Software Requirements

* Python 3.13
* OpenCV
* NumPy
* Matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Execute the program:

```bash
python src/main.py
```

The program performs:

1. Multi-channel normalization
2. Otsu thresholding
3. Adaptive thresholding
4. K-Means clustering
5. Quantitative evaluation
6. Visualization generation

---

# Part 1: Multi-Channel Color Normalization

Histogram equalization was independently applied to each RGB channel to improve image contrast and normalize illumination.

This process increased the visibility of dark regions and improved the distinction between the figure and the surrounding environment.

The normalized image served as the input for all segmentation methods.

---

# Part 2: Otsu Thresholding

Otsu thresholding computes a single global threshold value.

### Advantages

* Computationally efficient
* Simple implementation
* Produces relatively clean segmentation

### Disadvantages

* Assumes a bimodal intensity distribution
* Performs poorly under varying illumination
* Loses portions of the figure in darker regions

---

# Part 3: Adaptive Thresholding

Adaptive thresholding computes local thresholds for different image regions.

### Advantages

* Preserves local details
* Handles varying illumination conditions

### Disadvantages

* Highly sensitive to image texture
* Introduces substantial background noise
* Misclassifies grass and surrounding objects

The grass, houses, and trees produced significant noise due to local intensity variations.

---

# Part 4: K-Means Segmentation

K-Means clustering was performed in HSV color space using K = 4.

The algorithm groups pixels according to color similarity rather than grayscale intensity.

### Advantages

* Uses color information
* Preserves figure shape
* Removes large portions of the sky

### Disadvantages

* Requires selection of K value
* Some grass and driveway regions remain within the figure cluster

---

# Quantitative Evaluation

A manually created binary mask was used as pseudo-ground truth.

Two evaluation metrics were calculated:

### Intersection over Union (IoU)

[
IoU = \frac{|A \cap B|}{|A \cup B|}
]

### Dice Coefficient

[
Dice = \frac{2|A \cap B|}{|A| + |B|}
]

| Method   |    IoU |   Dice |
| -------- | -----: | -----: |
| Otsu     | 0.0311 | 0.0603 |
| Adaptive | 0.0615 | 0.1159 |
| K-Means  | 0.0203 | 0.0398 |

---

# Discussion of Results

The quantitative evaluation indicates that Adaptive Thresholding achieved the highest IoU and Dice values.

However, visual inspection shows that Adaptive Thresholding introduced substantial background noise throughout the image.

K-Means clustering produced the most visually appealing segmentation by preserving the figure shape and reducing portions of the background. Despite this, the overlap with the manually generated ground truth was low because portions of the grass and driveway remained in the selected cluster.

These results demonstrate that visual quality does not necessarily correspond to quantitative accuracy.

---

# Effect of Multi-Channel Normalization

Applying histogram equalization independently to all three RGB channels improved overall contrast and enhanced darker image regions.

Compared to the original image from Homework One:

* Figure visibility improved.
* Contrast increased.
* Segmentation algorithms performed more consistently.

The normalization stage significantly affected the quality of all subsequent segmentation methods.

---

# Comparison Visualization

<p align="center">
    <img src="results/evaluation/comparison_plot.png" width="1000">
</p>

The comparison plot displays:

1. Original image
2. Normalized image
3. Otsu segmentation
4. Adaptive thresholding
5. K-Means clustering
6. Ground truth mask

---

# Conclusion

This assignment demonstrates the challenges associated with segmenting low-light outdoor images.

No single segmentation technique performed perfectly.

* Otsu produced cleaner but incomplete segmentation.
* Adaptive thresholding achieved the best numerical metrics.
* K-Means produced the strongest visual segmentation.

The disagreement between visual appearance and quantitative metrics highlights the importance of evaluating segmentation methods using multiple criteria rather than relying solely on visual inspection.

---

## Author

**Sai Keerthan Jami (Q459V832)**

---
