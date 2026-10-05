"""outlier-finder-lite 单元测试。运行：python3 -m unittest discover -s tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from outlier import zscore_outliers, iqr_outliers, mad_outliers, find  # noqa: E402


class TestOutlier(unittest.TestCase):
    def test_zscore(self):
        self.assertIn(4, zscore_outliers([1, 2, 3, 4, 100]))

    def test_iqr(self):
        idx = iqr_outliers([10, 11, 10, 12, 100])
        self.assertIn(4, idx)

    def test_mad(self):
        idx = mad_outliers([10, 11, 10, 12, 100])
        self.assertIn(4, idx)

    def test_no_outlier(self):
        self.assertEqual(zscore_outliers([1, 2, 1, 2, 1, 2]), [])

    def test_find(self):
        r = find([1, 2, 100])
        self.assertTrue("zscore" in r and "iqr" in r and "mad" in r)


if __name__ == "__main__":
    unittest.main()
