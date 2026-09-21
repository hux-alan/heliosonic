from dataclasses import dataclass

import numpy as np
import numpy.testing as npt

from heliosonic.data import apply_mask_as_nan, clean_variable, find_boolean_segments
from heliosonic.mapping import (
    PitchMappingConfig,
    min_max_normalize,
    normalized_to_midi_note,
    normalized_to_pitch,
)
from heliosonic.midi import clip_g_midi_events
from heliosonic.synthesis import (
    aggregate_values_to_bins,
    merge_identical_pitch_events,
    synthesize_event_audio,
)


def test_invalid_cdf_samples_become_nan_and_alignment_is_preserved():
    raw = np.array([350.0, -1.0e31, 365.0, 999.0])
    cleaned = clean_variable(raw, {"FILLVAL": -1.0e31, "VALIDMIN": 300.0, "VALIDMAX": 800.0})
    assert len(cleaned["values"]) == len(raw)
    assert cleaned["mask"].tolist() == [True, False, True, False]
    assert np.isnan(cleaned["values"][1])
    assert np.isnan(cleaned["values"][3])
    npt.assert_allclose(cleaned["values"][[0, 2]], [350.0, 365.0])


def test_missing_gaps_are_not_filled_or_merged():
    values = np.array([1.0, 2.0, np.nan, np.nan, 5.0])
    mask = np.isfinite(values)
    cleaned = apply_mask_as_nan(values, mask)
    assert np.isnan(cleaned[2])
    assert np.isnan(cleaned[3])
    assert find_boolean_segments(mask, False) == [(2, 3)]
    assert find_boolean_segments(mask, True) == [(0, 1), (4, 4)]


def test_normalization_preserves_invalid_positions():
    normalized = min_max_normalize(np.array([10.0, np.nan, 20.0, 30.0]))
    npt.assert_allclose(normalized[[0, 2, 3]], [0.0, 0.5, 1.0])
    assert np.isnan(normalized[1])


def test_pitch_mapping_respects_configured_bounds():
    pitch = normalized_to_pitch(
        np.array([0.0, 0.5, 1.0, np.nan]),
        PitchMappingConfig(min_frequency_hz=220.0, max_frequency_hz=880.0, scale="log"),
    )
    npt.assert_allclose(pitch[:3], [220.0, 440.0, 880.0])
    assert np.isnan(pitch[3])


@dataclass(frozen=True)
class BinConfig:
    note_count: int = 2
    playback_duration_seconds: float = 2.0
    minimum_valid_fraction: float = 0.75


def test_aggregation_rejects_bins_below_valid_fraction():
    values = np.array([1.0, np.nan, 3.0, 4.0])
    normalized = np.array([0.0, np.nan, 0.5, 1.0])
    rows = aggregate_values_to_bins(values, np.arange(len(values)), normalized, BinConfig())
    assert rows[0]["accepted"] is False
    assert rows[0]["valid_data_fraction"] == 0.5
    assert rows[1]["accepted"] is True
    assert rows[1]["valid_data_fraction"] == 1.0


def test_repeated_identical_pitch_states_merge():
    rows = [
        {"accepted": True, "bin_index": 0, "audio_start_seconds": 0.0, "audio_end_seconds": 1.0, "midi_note": 64, "frequency_hz": 329.63},
        {"accepted": True, "bin_index": 1, "audio_start_seconds": 1.0, "audio_end_seconds": 2.0, "midi_note": 64, "frequency_hz": 329.63},
        {"accepted": True, "bin_index": 2, "audio_start_seconds": 2.0, "audio_end_seconds": 3.0, "midi_note": 65, "frequency_hz": 349.23},
    ]
    events = merge_identical_pitch_events(rows)
    assert len(events) == 2
    assert events[0]["audio_end_seconds"] == 2.0
    assert events[0]["source_bin_indices"] == [0, 1]


def test_generated_audio_duration_and_amplitude_bound():
    events = [{"audio_start_seconds": 0.0, "audio_end_seconds": 1.0, "frequency_hz": 440.0}]
    audio = synthesize_event_audio(events, sample_rate=1000, duration_seconds=2.0, amplitude=0.18, attack_seconds=0.01, release_seconds=0.01)
    assert len(audio) == 2000
    assert np.max(np.abs(audio)) <= 0.1800000001
    npt.assert_allclose(audio[1000:], 0.0)


def test_midi_export_preserves_timing_and_notes():
    events = [
        {"audio_start_seconds": 0.0, "audio_end_seconds": 0.5, "midi_note": 66},
        {"audio_start_seconds": 0.5, "audio_end_seconds": 1.0, "midi_note": 67},
    ]
    midi_events = clip_g_midi_events(events)
    assert midi_events == [
        (0, 0, 0x90, [66, 72]),
        (480, 0, 0x90, [67, 72]),
        (480, 1, 0x80, [66, 0]),
        (960, 1, 0x80, [67, 0]),
    ]


def test_midi_note_mapping_bounds():
    notes = normalized_to_midi_note(np.array([0.0, 0.5, 1.0, np.nan]), 64, 70)
    npt.assert_allclose(notes[:3], [64, 67, 70])
    assert np.isnan(notes[3])
