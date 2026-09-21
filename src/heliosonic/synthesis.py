"""Synthesis helpers for current Vp pitch experiments."""

from __future__ import annotations

import numpy as np


def aggregate_values_to_bins(values, times, normalized, config):
    """Aggregate samples into fixed-count audio bins without filling gaps."""
    values = np.asarray(values, dtype=float)
    times = np.asarray(times)
    normalized = np.asarray(normalized, dtype=float)
    if not (len(values) == len(times) == len(normalized)):
        raise ValueError("values, times, and normalized must have the same length")

    source_positions = np.linspace(0, len(values), config.note_count + 1)
    rows = []
    for bin_index in range(config.note_count):
        start = int(np.floor(source_positions[bin_index]))
        end = int(np.floor(source_positions[bin_index + 1]))
        if bin_index == config.note_count - 1:
            end = len(values)
        bin_values = values[start:end]
        valid = np.isfinite(bin_values)
        valid_fraction = float(np.sum(valid) / len(bin_values)) if len(bin_values) else 0.0
        accepted = valid_fraction >= config.minimum_valid_fraction and np.any(valid)
        representative = float(np.nanmedian(bin_values)) if accepted else np.nan
        normalized_value = float(np.nanmedian(normalized[start:end][valid])) if accepted else np.nan
        rows.append({
            "bin_index": bin_index,
            "source_start_index": start,
            "source_end_index": end - 1,
            "spacecraft_start_time": times[start] if len(times) else None,
            "spacecraft_end_time": times[end - 1] if end > start else None,
            "audio_start_seconds": bin_index * config.playback_duration_seconds / config.note_count,
            "audio_end_seconds": (bin_index + 1) * config.playback_duration_seconds / config.note_count,
            "valid_data_fraction": valid_fraction,
            "accepted": bool(accepted),
            "representative_vp": representative,
            "normalized_vp": normalized_value,
        })
    return rows


def fixed_attack_release_envelope(sample_count, sample_rate, attack_seconds, release_seconds):
    """Create a fixed attack/release envelope for one event."""
    envelope = np.ones(sample_count, dtype=float)
    attack_samples = min(int(round(attack_seconds * sample_rate)), sample_count)
    release_samples = min(int(round(release_seconds * sample_rate)), sample_count)
    if attack_samples > 0:
        envelope[:attack_samples] *= np.linspace(0.0, 1.0, attack_samples, endpoint=True)
    if release_samples > 0:
        envelope[-release_samples:] *= np.linspace(1.0, 0.0, release_samples, endpoint=True)
    return envelope


def merge_identical_pitch_events(rows):
    """Merge consecutive accepted rows with the same MIDI note."""
    events = []
    current = None
    for row in rows:
        if not row.get("accepted") or not np.isfinite(float(row.get("midi_note", np.nan))):
            if current is not None:
                events.append(current)
                current = None
            continue
        if current is not None and row["midi_note"] == current["midi_note"]:
            current["audio_end_seconds"] = row["audio_end_seconds"]
            current["source_bin_count"] += 1
            current["source_bin_indices"].append(row["bin_index"])
        else:
            if current is not None:
                events.append(current)
            current = {
                "audio_start_seconds": row["audio_start_seconds"],
                "audio_end_seconds": row["audio_end_seconds"],
                "midi_note": row["midi_note"],
                "frequency_hz": row.get("frequency_hz", np.nan),
                "source_bin_count": 1,
                "source_bin_indices": [row["bin_index"]],
            }
    if current is not None:
        events.append(current)
    return events


def synthesize_event_audio(events, sample_rate, duration_seconds, amplitude, attack_seconds, release_seconds):
    """Synthesize fixed-amplitude sine events with exact silence elsewhere."""
    total_samples = int(round(duration_seconds * sample_rate))
    audio = np.zeros(total_samples, dtype=float)
    for event in events:
        frequency = float(event["frequency_hz"])
        if not np.isfinite(frequency):
            continue
        start = int(round(event["audio_start_seconds"] * sample_rate))
        end = int(round(event["audio_end_seconds"] * sample_rate))
        start = max(0, min(start, total_samples))
        end = max(start, min(end, total_samples))
        sample_count = end - start
        if sample_count == 0:
            continue
        t = np.arange(sample_count, dtype=float) / sample_rate
        tone = np.sin(2.0 * np.pi * frequency * t)
        envelope = fixed_attack_release_envelope(sample_count, sample_rate, attack_seconds, release_seconds)
        audio[start:end] += amplitude * tone * envelope
    return audio

