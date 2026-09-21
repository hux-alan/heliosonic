"""Data cleaning helpers that preserve spacecraft sample alignment."""

from __future__ import annotations

import numpy as np


def validation_mask(values, fill_value=None, valid_min=None, valid_max=None):
    """Return a boolean mask using CDF fill and valid-range metadata."""
    data = np.asarray(values, dtype=float)
    mask = np.isfinite(data)
    if fill_value is not None:
        mask &= data != float(fill_value)
    if valid_min is not None:
        mask &= data >= float(valid_min)
    if valid_max is not None:
        mask &= data <= float(valid_max)
    return mask


def apply_mask_as_nan(values, valid_mask):
    """Return a float copy where invalid positions are NaN."""
    data = np.asarray(values, dtype=float)
    mask = np.asarray(valid_mask, dtype=bool)
    if data.shape != mask.shape:
        raise ValueError("values and valid_mask must have the same shape")
    cleaned = data.copy()
    cleaned[~mask] = np.nan
    return cleaned


def clean_variable(values, attrs):
    """Apply CDF FILLVAL, VALIDMIN, and VALIDMAX rules without changing length."""
    fill_value = attrs.get("FILLVAL")
    valid_min = attrs.get("VALIDMIN")
    valid_max = attrs.get("VALIDMAX")
    mask = validation_mask(values, fill_value, valid_min, valid_max)
    return {
        "values": apply_mask_as_nan(values, mask),
        "mask": mask,
        "fill_value": fill_value,
        "valid_min": valid_min,
        "valid_max": valid_max,
    }


def find_boolean_segments(mask, value=True):
    """Return inclusive index ranges where a boolean mask equals value."""
    mask = np.asarray(mask, dtype=bool)
    target = mask == value
    segments = []
    start = None
    for index, is_target in enumerate(target):
        if is_target and start is None:
            start = index
        elif not is_target and start is not None:
            segments.append((start, index - 1))
            start = None
    if start is not None:
        segments.append((start, len(mask) - 1))
    return segments

