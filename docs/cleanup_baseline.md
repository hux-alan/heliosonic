# Cleanup Baseline

Baseline captured on branch `cleanup/pre-share` before notebook cleanup or refactoring.

## Git and Environment

- `main` was confirmed clean before creating `cleanup/pre-share`.
- Existing README changes from the previous documentation update were restored on this branch.
- Notebook 4 was executed from a fresh Jupyter kernel with the `heliosonic` kernel.
- The available source file was `data/ac_h0_swe_20240709_v11.cdf`.

## Notebook Sizes and Cell Counts

| Notebook | Size | Markdown cells | Code cells | Total cells |
| --- | ---: | ---: | ---: | ---: |
| `01_explore_CDF.ipynb` | 114,606 bytes | 0 | 4 | 4 |
| `02_understand_variables.ipynb` | 475,450 bytes | 9 | 33 | 42 |
| `03_normalize_variables.ipynb` | 1,053,988 bytes | 8 | 9 | 17 |
| `04_sonification_mapping.ipynb` | 65,444,494 bytes | 41 | 36 | 77 |

## Notebook 4 Functions and Configuration Classes

Configuration classes:

- `PitchMappingConfig`
- `PitchSmoothingConfig`
- `ClipConfig`
- `DiscreteEventConfig`
- `SustainedPitchConfig`
- `NarrowPitchConfig`

Functions:

- `format_table_value`
- `display_markdown_table`
- `clean_variable`
- `apply_mask_as_nan`
- `min_max_normalize`
- `normalized_to_pitch`
- `find_boolean_segments`
- `summarize_segments`
- `smooth_pitch_by_valid_segment`
- `interpolate_pitch_control_to_audio_grid`
- `synthesize_sine_from_interpolated_pitch`
- `audio_transition_diagnostics`
- `summarize_audio_clip`
- `midi_to_frequency`
- `midi_to_note_name`
- `normalized_to_midi_note`
- `aggregate_vp_to_bins`
- `fixed_attack_release_envelope`
- `synthesize_discrete_event_audio`
- `plot_discrete_event_summary`
- `normalize_with_reference`
- `aggregate_vp_with_reference`
- `apply_pitch_mapping_to_bins`
- `cents_between`
- `should_merge_with_event`
- `merge_bins_to_audible_events`
- `event_pitch_trajectory`
- `synthesize_sustained_events`
- `plot_sustained_config`
- `map_normalized_to_log_frequency`
- `prepare_narrow_bin_rows`
- `apply_continuous_change_threshold`
- `merge_narrow_rows_to_events`
- `narrow_event_pitch_trajectory`
- `synthesize_narrow_events`
- `plot_narrow_config`
- `write_variable_length_quantity`
- `midi_event`
- `midi_meta_event`
- `write_clip_g_midi`

## Major Generated Clips and Comparison Groups

- Continuous sine-wave comparison clips:
  - 60 seconds, no smoothing, hard gaps
  - 60 seconds, light smoothing, hard gaps
  - 60 seconds, moderate smoothing, hard gaps
  - 30 seconds, light smoothing, hard gaps
  - 120 seconds, light smoothing, hard gaps
  - 60 seconds, light smoothing, phase reset at valid-segment starts
- Discrete event prototypes:
  - 60 notes over 60 seconds
  - 90 notes over 60 seconds
  - 120 notes over 60 seconds
- Sustained-state comparisons:
  - Clip A: 120 bins, MIDI 60-76, merged, no glide
  - Clip B: 240 bins, MIDI 60-76, merged, short glide
  - Clip C: 240 bins, MIDI 48-84, merged, short glide
  - Clip D: 240 bins, microtonal targets, short glide
- Narrow-range comparisons:
  - Clip E: continuous sine, 240 bins, 330-440 Hz
  - Clip F: continuous harmonic, 240 bins, 330-440 Hz
  - Clip G: chromatic harmonic, 240 bins, MIDI 64-70
  - Clip H: continuous harmonic, 240 bins, 300-500 Hz
- MIDI side experiment:
  - Clip G exported to `media/clip_g_vp_sustained_midi_64_70.mid`

## Largest Serialized Outputs

The largest Notebook 4 outputs were confirmed by serialized output size:

| Cell index before cleanup | Approx. output size | Output type |
| ---: | ---: | --- |
| 24 | 21.87 MiB | embedded audio display output |
| 68 | 13.46 MiB | embedded audio display output |
| 52 | 13.46 MiB | embedded audio display output |
| 37 | 10.10 MiB | embedded audio display output |
| 72 | 0.90 MiB | repeated plots |
| 56 | 0.86 MiB | repeated plots |
| 39 | 0.50 MiB | repeated plots |
| 22 | 0.25 MiB | plot |

## Values That Must Remain Unchanged

- ACE SWEPAM Level 2 source data and `Vp` target variable.
- Cleaning rules based on CDF `FILLVAL`, `VALIDMIN`, and `VALIDMAX`.
- Invalid samples represented as `NaN`.
- Original sample count and time alignment preserved.
- Missing intervals preserved as gaps; no interpolation across missing source data.
- Normalization references and current observed valid `Vp` range.
- Pitch ranges, MIDI note ranges, note counts, playback durations, valid-data thresholds, amplitude, timbre settings, attack and release values, glide settings, and MIDI timing/velocity behavior.
- Existing listening observations and experimental history.

## Executed Notebook 4 Metrics

- `Vp` total samples: 1350
- valid `Vp` samples: 1257
- invalid `Vp` samples: 93
- valid `Vp` range: 352.8299865722656 to 396.55999755859375 km/s
- normalized range: 0.0 to 1.0
- valid segments: 56
- missing gaps: 56
- baseline pitch range: 220.0 to 880.0 Hz
- normalized checksum: `962f5cf73046b473`
- baseline pitch checksum: `2ed84b37ca0c755e`
- pitch-control checksums:
  - none: `2ed84b37ca0c755e`
  - light: `97de84aa68d4db75`
  - moderate: `0ffe72ecd44cc130`

Continuous clips:

| Clip | Samples | Duration | Peak amplitude | Valid audio segments | Silent segments |
| --- | ---: | ---: | ---: | ---: | ---: |
| 60 seconds - no smoothing - interpolated pitch - hard gaps | 1,323,000 | 60.0 | 0.19999999999980753 | 55 | 55 |
| 60 seconds - light smoothing - interpolated pitch - hard gaps | 1,323,000 | 60.0 | 0.1999999999982194 | 55 | 55 |
| 60 seconds - moderate smoothing - interpolated pitch - hard gaps | 1,323,000 | 60.0 | 0.19999999999957532 | 55 | 55 |
| 30 seconds - light smoothing - interpolated pitch - hard gaps | 661,500 | 30.0 | 0.1999999999999184 | 55 | 55 |
| 120 seconds - light smoothing - interpolated pitch - hard gaps | 2,646,000 | 120.0 | 0.19999999999999876 | 55 | 55 |
| 60 seconds - light smoothing - interpolated pitch - hard gaps - phase reset at valid-segment starts | 1,323,000 | 60.0 | 0.19999999999968823 | 55 | 55 |

Discrete event clips:

| Clip | Accepted bins/events | MIDI note range | Samples | Duration | Peak amplitude |
| --- | ---: | --- | ---: | ---: | ---: |
| 60 notes over 60 seconds | 59 | 60-76 | 1,323,000 | 60.0 | 0.18 |
| 90 notes over 60 seconds | 88 | 60-76 | 1,323,000 | 60.0 | 0.18 |
| 120 notes over 60 seconds | 117 | 60-76 | 1,323,000 | 60.0 | 0.18 |

Sustained-state clips:

| Clip | Accepted bins | Audible events | Samples | Duration | Peak amplitude |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 117 | 87 | 1,323,000 | 60.0 | 0.18 |
| B | 234 | 163 | 1,323,000 | 60.0 | 0.18 |
| C | 234 | 195 | 1,323,000 | 60.0 | 0.18 |
| D | 234 | 221 | 1,323,000 | 60.0 | 0.18 |

Narrow-range clips:

| Clip | Accepted bins | Audible attacks/events | Samples | Duration | Peak amplitude |
| --- | ---: | ---: | ---: | ---: | ---: |
| E | 234 | 2 | 1,323,000 | 60.0 | 0.17999999999995764 |
| F | 234 | 2 | 1,323,000 | 60.0 | 0.18 |
| G | 234 | 70 | 1,323,000 | 60.0 | 0.18 |
| H | 234 | 2 | 1,323,000 | 60.0 | 0.18 |

Clip G MIDI:

- event count: 70
- first 12 MIDI notes: 66, 67, 66, 65, 68, 67, 66, 65, 66, 65, 66, 67
- first 12 starts in seconds: 0.0, 0.5, 2.0, 2.5, 2.75, 4.75, 7.25, 7.5, 7.75, 9.5, 11.0, 13.0
