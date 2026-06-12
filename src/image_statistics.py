import numpy as np
from scipy import stats


def print_channel_statistics(channel, channel_name):
    pixels = channel.flatten()

    mode_result = stats.mode(pixels, keepdims=False)

    print(f"\n{'=' * 50}")
    print(f"{channel_name} Channel Statistics")
    print(f"{'=' * 50}")

    print(f"Min: {np.min(pixels)}")
    print(f"Max: {np.max(pixels)}")
    print(f"Average: {np.mean(pixels):.2f}")
    print(f"Median: {np.median(pixels):.2f}")
    print(f"Mode: {mode_result.mode}")
    print(f"Skew: {stats.skew(pixels):.4f}")
    print(f"Range: {np.ptp(pixels)}")
    print(f"Standard Deviation: {np.std(pixels):.2f}")
    print(f"Variance: {np.var(pixels):.2f}")