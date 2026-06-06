"""Generate synthetic normal and fault-like windows and compare their features."""

from __future__ import annotations

import json
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from features import extract_features


def make_window(*, fault: bool, sample_count: int = 1024) -> list[float]:
    random_generator = random.Random(42)
    samples = []

    for index in range(sample_count):
        time_seconds = index / 1024
        sample = math.sin(2 * math.pi * 60 * time_seconds)
        sample += random_generator.gauss(0, 0.08)

        if fault and index % 128 == 0:
            sample += 4.0

        samples.append(sample)

    return samples


def main() -> None:
    result = {
        "normal": extract_features(make_window(fault=False)),
        "fault_like": extract_features(make_window(fault=True)),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

