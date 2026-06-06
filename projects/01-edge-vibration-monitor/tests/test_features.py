import math
import sys
import unittest
from pathlib import Path

ANALYSIS_DIRECTORY = Path(__file__).parents[1] / "analysis"
sys.path.insert(0, str(ANALYSIS_DIRECTORY))

from demo import make_window
from features import extract_features


class ExtractFeaturesTests(unittest.TestCase):
    def test_constant_signal_has_no_vibration_energy(self) -> None:
        features = extract_features([2.0, 2.0, 2.0, 2.0])

        self.assertEqual(features["rms"], 0.0)
        self.assertEqual(features["peak_to_peak"], 0.0)
        self.assertEqual(features["crest_factor"], 0.0)

    def test_sine_wave_rms_is_correct(self) -> None:
        samples = [math.sin(2 * math.pi * index / 100) for index in range(100)]

        features = extract_features(samples)

        self.assertAlmostEqual(features["rms"], 1 / math.sqrt(2), places=6)

    def test_fault_like_impulses_raise_crest_factor_and_kurtosis(self) -> None:
        normal = extract_features(make_window(fault=False))
        fault_like = extract_features(make_window(fault=True))

        self.assertGreater(fault_like["crest_factor"], normal["crest_factor"])
        self.assertGreater(fault_like["kurtosis"], normal["kurtosis"])

    def test_short_window_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            extract_features([1.0, 2.0, 3.0])


if __name__ == "__main__":
    unittest.main()

