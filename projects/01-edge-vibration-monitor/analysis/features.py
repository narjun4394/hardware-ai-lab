"""Explainable time-domain features for vibration signal windows."""

from __future__ import annotations

import math
from collections.abc import Sequence


def extract_features(samples: Sequence[float]) -> dict[str, float]:
    """Return basic features from a vibration window after removing DC offset."""
    if len(samples) < 4:
        raise ValueError("at least four samples are required")

    mean = sum(samples) / len(samples)
    centered = [sample - mean for sample in samples]
    mean_square = sum(sample * sample for sample in centered) / len(centered)
    rms = math.sqrt(mean_square)
    peak = max(abs(sample) for sample in centered)

    if mean_square == 0:
        kurtosis = 0.0
        crest_factor = 0.0
    else:
        fourth_moment = sum(sample**4 for sample in centered) / len(centered)
        kurtosis = fourth_moment / (mean_square**2)
        crest_factor = peak / rms

    zero_crossings = sum(
        1
        for left, right in zip(centered, centered[1:])
        if (left < 0 <= right) or (left >= 0 > right)
    )

    return {
        "mean": mean,
        "rms": rms,
        "peak_to_peak": max(centered) - min(centered),
        "crest_factor": crest_factor,
        "kurtosis": kurtosis,
        "zero_crossing_rate": zero_crossings / (len(centered) - 1),
    }

