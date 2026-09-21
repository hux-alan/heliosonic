"""Normalization and pitch-mapping helpers."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class PitchMappingConfig:
    """Parameters for mapping normalized data values to pitch in Hz."""

    min_frequency_hz: float = 220.0
    max_frequency_hz: float = 880.0
    scale: str = "log"
    invert: bool = False
    label: str = "220-880 Hz log baseline"


def min_max_normalize(values):
    """Normalize finite values to 0-1 while preserving invalid positions."""
    data = np.asarray(values, dtype=float)
    normalized = np.full_like(data, np.nan, dtype=float)
    finite = np.isfinite(data)
    if not np.any(finite):
        return normalized
    min_value = np.nanmin(data)
    max_value = np.nanmax(data)
    if max_value == min_value:
        normalized[finite] = 0.0
        return normalized
    normalized[finite] = (data[finite] - min_value) / (max_value - min_value)
    return normalized


def normalize_with_reference(values, reference_min, reference_max):
    """Normalize to a fixed reference range and preserve NaN positions."""
    if reference_max <= reference_min:
        raise ValueError("reference_max must be greater than reference_min")
    data = np.asarray(values, dtype=float)
    normalized = np.full_like(data, np.nan, dtype=float)
    finite = np.isfinite(data)
    clipped = np.clip(data[finite], reference_min, reference_max)
    normalized[finite] = (clipped - reference_min) / (reference_max - reference_min)
    return normalized


def normalized_to_pitch(normalized_values, config=PitchMappingConfig()):
    """Map normalized 0-1 values to pitch frequencies in Hz."""
    if config.min_frequency_hz <= 0 or config.max_frequency_hz <= 0:
        raise ValueError("Frequencies must be positive for pitch mapping")
    if config.max_frequency_hz <= config.min_frequency_hz:
        raise ValueError("max_frequency_hz must be greater than min_frequency_hz")
    if config.scale not in {"linear", "log"}:
        raise ValueError("scale must be either 'linear' or 'log'")
    values = np.asarray(normalized_values, dtype=float)
    finite = np.isfinite(values)
    if np.any((values[finite] < 0) | (values[finite] > 1)):
        raise ValueError("Finite normalized values must be between 0 and 1")
    mapped = values.copy()
    if config.invert:
        mapped[finite] = 1.0 - mapped[finite]
    pitch = np.full_like(values, np.nan, dtype=float)
    if config.scale == "linear":
        pitch[finite] = config.min_frequency_hz + mapped[finite] * (
            config.max_frequency_hz - config.min_frequency_hz
        )
    else:
        ratio = config.max_frequency_hz / config.min_frequency_hz
        pitch[finite] = config.min_frequency_hz * (ratio ** mapped[finite])
    return pitch


def midi_to_frequency(midi_notes):
    """Convert MIDI notes to equal-tempered frequencies."""
    notes = np.asarray(midi_notes, dtype=float)
    frequencies = np.full_like(notes, np.nan, dtype=float)
    finite = np.isfinite(notes)
    frequencies[finite] = 440.0 * (2.0 ** ((notes[finite] - 69.0) / 12.0))
    return frequencies


def normalized_to_midi_note(normalized_values, min_midi_note, max_midi_note):
    """Map normalized values to rounded MIDI notes within configured bounds."""
    values = np.asarray(normalized_values, dtype=float)
    midi_notes = np.full_like(values, np.nan, dtype=float)
    finite = np.isfinite(values)
    if np.any((values[finite] < 0) | (values[finite] > 1)):
        raise ValueError("Finite normalized values must be between 0 and 1")
    mapped = min_midi_note + values[finite] * (max_midi_note - min_midi_note)
    midi_notes[finite] = np.rint(mapped)
    midi_notes[finite] = np.clip(midi_notes[finite], min_midi_note, max_midi_note)
    return midi_notes.astype(float)

