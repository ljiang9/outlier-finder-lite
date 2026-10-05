"""outlier-finder-lite — 异常检测。

z-score / IQR / MAD 三种方法标记异常点。零第三方依赖。
"""
from __future__ import annotations

import statistics as st


def zscore_outliers(series: list[float], z: float = 1.5) -> list[int]:
    """|z| > 阈值视为异常。"""
    if len(series) < 2:
        return []
    mu = st.mean(series)
    sd = st.pstdev(series) or 1e-9
    return [i for i, x in enumerate(series) if abs((x - mu) / sd) > z]


def _percentile(sorted_vals: list[float], q: float) -> float:
    if not sorted_vals:
        return 0.0
    k = (len(sorted_vals) - 1) * q
    lo = int(k)
    hi = min(lo + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (k - lo)


def iqr_outliers(series: list[float], k: float = 1.5) -> list[int]:
    """IQR 法则：超出 [Q1-k*IQR, Q3+k*IQR] 为异常。"""
    if len(series) < 4:
        return []
    s = sorted(series)
    q1 = _percentile(s, 0.25)
    q3 = _percentile(s, 0.75)
    iqr = q3 - q1
    lo, hi = q1 - k * iqr, q3 + k * iqr
    return [i for i, x in enumerate(series) if x < lo or x > hi]


def mad_outliers(series: list[float], z: float = 3.5) -> list[int]:
    """中位数绝对偏差（稳健）。"""
    if len(series) < 2:
        return []
    med = st.median(series)
    mad = st.median([abs(x - med) for x in series]) or 1e-9
    return [i for i, x in enumerate(series) if 0.6745 * abs(x - med) / mad > z]


def find(series: list[float]) -> dict:
    return {
        "series": series,
        "zscore": zscore_outliers(series),
        "iqr": iqr_outliers(series),
        "mad": mad_outliers(series),
    }
