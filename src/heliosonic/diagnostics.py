"""Diagnostic helpers for audio and segment checks."""

from __future__ import annotations

import numpy as np

from .data import find_boolean_segments


def audio_summary(audio, valid_mask=None):
    """Return simple audio diagnostics used by notebook comparisons."""
    audio = np.asarray(audio, dtype=float)
    summary = {
        "sample_count": int(len(audio)),
        "peak_amplitude": float(np.max(np.abs(audio))) if len(audio) else 0.0,
        "clipping_occurred": bool(np.any(np.abs(audio) > 1.0)),
    }
    if valid_mask is not None:
        mask = np.asarray(valid_mask, dtype=bool)
        summary["audio_valid_segments"] = len(find_boolean_segments(mask, True))
        summary["audio_silent_segments"] = len(find_boolean_segments(mask, False))
    return summary

