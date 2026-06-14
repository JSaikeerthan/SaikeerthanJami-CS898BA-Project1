# SaikeerthanJami-CS898BA-Project1

## CS 898BA – Image Analysis and Computer Vision

**Homework 1**

---

## Overview

This project explores fundamental image processing and computer vision techniques using Python and OpenCV. The assignment includes:

* Basic image statistics
* Color space conversions
* Histogram equalization
* Affine transformations
* Gaussian blurring
* Edge detection
* Visualization and comparison of edge detection methods

The project was developed incrementally using Git with meaningful commits and all AI assistance was documented in `AI_Log.md`.

---

## Project Structure

```text
SaikeerthanJami-CS898BA-Project1
│
├── images
│   └── HW1_IMG.png
│
├── results
│   ├── converted
│   ├── transformed
│   ├── blurred
│   ├── subsets
│   ├── edges
│   └── plots
│
├── src
│   ├── main.py
│   ├── image_statistics.py
│   ├── conversions.py
│   ├── affine_transforms.py
│   ├── gaussian_blur.py
│   ├── create_subsets.py
│   ├── edge_detection.py
│   └── plot_results.py
│
├── README.md
├── AI_Log.md
├── requirements.txt
└── .gitignore
```

---

## Requirements

* Python 3.13
* OpenCV
* NumPy
* SciPy
* Matplotlib
* Pandas

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JSaikeerthan/SaikeerthanJami-CS898BA-Project1.git
cd SaikeerthanJami-CS898BA-Project1
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute:

```bash
python src/main.py
```

---

# Part 2: Image Processing

## Basic Image Statistics

For each RGB channel, the following statistics were computed:

* Minimum
* Maximum
* Average
* Median
* Mode
* Skew
* Range
* Standard Deviation
* Variance

### Results

| Channel | Mean  | Median | Mode | Std Dev | Variance |
| ------- | ----- | ------ | ---- | ------- | -------- |
| Red     | 20.61 | 12     | 4    | 22.46   | 504.26   |
| Green   | 24.64 | 16     | 10   | 22.23   | 493.96   |
| Blue    | 21.83 | 10     | 4    | 26.23   | 687.99   |

The relatively low mean intensity values indicate that the image is generally dark with a few bright regions.

---

## Color Space Conversions

The following image representations were generated:

1. Original RGB Image
2. Grayscale Image
3. Binary Image
4. HSV Image
5. CIELAB Image
6. HLS Image
7. Histogram Equalized HSV Image converted back to RGB

Total images:

```text
7 images
```

---

## Histogram Equalization

Histogram equalization was applied to the Value (V) channel of the HSV image.

### Observations

* Increased overall contrast
* Improved visibility in darker regions
* Enhanced object details
* Better illumination normalization

---

## Affine Transformations

Two unique affine transformations were applied to each of the seven images.

Examples:

* Rotation
* Translation
* Scaling
* Shearing

Total images after transformation:

```text
21 images
```

---

## Gaussian Blur

Gaussian blur was applied using the following sigma values:

```text
0.5
1.0
1.5
2.0
2.5
3.0
3.5
```

Total images:

```text
168 images
```

### Discussion

As sigma increased:

* Noise reduction improved.
* Fine textures disappeared.
* Edges became softer.
* High-frequency information was gradually removed.

Small sigma values preserved image details, while large sigma values produced heavy smoothing and loss of detail.

---

# Part 3: Edge Detection

The dataset of 168 images was randomly divided into four equally sized subsets.

Each subset contained:

```text
42 images
```

One subset was selected for edge detection experiments.

---

## Edge Detection Methods

### Sobel

#### Advantages

* Fast computation
* Provides gradient direction information

#### Disadvantages

* Produces thick edges
* Sensitive to noise

---

### Laplacian

#### Advantages

* Detects edges in all directions
* Highlights fine detail

#### Disadvantages

* Extremely sensitive to noise
* Amplifies artifacts

---

### Canny

#### Advantages

* Produces thin and continuous edges
* Excellent noise suppression
* Strong edge localization

#### Disadvantages

* Requires threshold tuning
* Computationally more expensive

---

### Prewitt

#### Advantages

* Simple implementation
* Computationally inexpensive

#### Disadvantages

* Less accurate than Sobel
* More susceptible to noise

---

## Edge Detection Analysis

Among the four methods, Canny generally produced the cleanest and most continuous object boundaries while suppressing noise effectively.

Sobel and Prewitt successfully detected major structures but generated thicker edges.

Laplacian highlighted many fine details but also amplified image noise and artifacts, especially in heavily blurred images.

For this dataset, Canny provided the best balance between noise suppression and edge localization.

---

# Comparison Plots

The project generated:

```text
42 comparison plots
```

Six representative plots were selected for this report.

## Plot 1


<img src="results/plots/readme_plots/original_rotated_sigma_3.0_plot.png" width="900">

<p><b>Processing Applied:</b> Original image → Rotation affine transformation → Gaussian blur (σ = 3.0).</p>


## Plot 2


<img src="results/plots/readme_plots/binary_rotated_sigma_0.5_plot.png" width="900">

<p><b>Processing Applied:</b> Binary image → Rotation affine transformation → Gaussian blur (σ = 0.5).</p>


## Plot 3


<img src="results/plots/readme_plots/binary_translated_sigma_2.0_plot.png" width="900">

<p><b>Processing Applied:</b> Binary image → Translation affine transformation → Gaussian blur (σ = 2.0).</p>


## Plot 4


<img src="results/plots/readme_plots/grayscale_translated_sigma_1.5_plot.png" width="900">

<p><b>Processing Applied:</b> Grayscale image → Translation affine transformation → Gaussian blur (σ = 1.5).</p>



## Plot 5


<img src="results/plots/readme_plots/hls_plot.png" width="900">

<p><b>Processing Applied:</b> HLS color space conversion.</p>

## Plot 6


<img src="results/plots/readme_plots/normalized_rgb_rotated_sigma_0.5_plot.png" width="900">

<p><b>Processing Applied:</b> HSV histogram equalization followed by conversion back to RGB → Rotation affine transformation → Gaussian blur (σ = 0.5).</p>

---

# Final Image Counts

| Stage                        | Number of Images |
| ---------------------------- | ---------------- |
| Original + Conversions       | 7                |
| After Affine Transformations | 21               |
| After Gaussian Blur          | 168              |
| Selected Subset              | 42               |
| Edge Detection Outputs       | 210              |
| Comparison Plots             | 42               |
| README Sample Plots          | 6                |

---

# Conclusion

This project demonstrated a complete image processing pipeline using OpenCV and Python. Multiple image transformations, filtering techniques, and edge detection algorithms were evaluated and compared.

The experiments showed that increasing Gaussian blur reduces noise at the cost of image detail and that Canny edge detection generally provides the most accurate and visually appealing edge maps for this image dataset.

---

## Author

**Sai Keerthan Jami (Q459V832)**



