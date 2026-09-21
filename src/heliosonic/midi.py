"""Minimal MIDI writing helpers for Clip G-style event exports."""

from __future__ import annotations

import numpy as np


def write_variable_length_quantity(value):
    """Encode an integer as a MIDI variable-length quantity."""
    value = int(value)
    if value < 0:
        raise ValueError("MIDI delta times must be non-negative")
    bytes_out = [value & 0x7F]
    value >>= 7
    while value:
        bytes_out.insert(0, (value & 0x7F) | 0x80)
        value >>= 7
    return bytes(bytes_out)


def midi_event(delta_ticks, status_byte, data_bytes):
    """Create one MIDI channel event with a variable-length delta time."""
    return write_variable_length_quantity(delta_ticks) + bytes([status_byte]) + bytes(data_bytes)


def midi_meta_event(delta_ticks, meta_type, data_bytes):
    """Create one MIDI meta event with a variable-length delta time."""
    return (
        write_variable_length_quantity(delta_ticks)
        + bytes([0xFF, meta_type])
        + write_variable_length_quantity(len(data_bytes))
        + bytes(data_bytes)
    )


def clip_g_midi_events(event_rows, ticks_per_quarter=480, tempo_microseconds_per_quarter=500_000):
    """Return MIDI note events using the current Clip G timing behavior."""
    ticks_per_second = ticks_per_quarter * 1_000_000 / tempo_microseconds_per_quarter
    midi_events = []
    velocity = 72
    channel = 0
    for event in event_rows:
        midi_note = event["midi_note"]
        if midi_note == "" or not np.isfinite(float(midi_note)):
            continue
        start_tick = int(round(event["audio_start_seconds"] * ticks_per_second))
        end_tick = int(round(event["audio_end_seconds"] * ticks_per_second))
        if end_tick <= start_tick:
            continue
        note = int(midi_note)
        midi_events.append((start_tick, 0, 0x90 | channel, [note, velocity]))
        midi_events.append((end_tick, 1, 0x80 | channel, [note, 0]))
    return sorted(midi_events, key=lambda item: (item[0], item[1]))
