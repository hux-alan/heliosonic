# HelioSonic Development Instructions

## Project Overview

HelioSonic is a research-oriented heliophysics sonification project. It transforms spacecraft measurements into auditory representations for scientific exploration, accessibility work, and understanding space physics data.

This is not primarily a music-composition project. Preserve physical meaning and scientific traceability over musical polish.

## Current Stage

The project has moved from initial data loading into experimental sonification.

Established work:

- ACE SWEPAM Level 2 CDF loading
- `Vp` cleaning with CDF `FILLVAL`, `VALIDMIN`, and `VALIDMAX`
- preservation of invalid samples as `NaN`
- min-max normalization experiments for candidate variables

Active work:

- mapping solar-wind speed (`Vp`) to pitch
- comparing continuous, discrete, sustained, and narrow-range pitch mappings
- testing timbre and sustained-state behavior
- understanding discontinuities, missing-data gaps, pitch jumps, and duration-aware pitch transitions

## Technical Stack

- Python
- Jupyter notebooks
- VS Code
- Conda environment: `heliosonic`
- Current libraries include `cdflib`, `numpy`, `matplotlib`, and related scientific Python tools.

## Repository Structure

- `notebooks/`: exploratory analysis and sonification experiments
- `src/`: reusable Python modules
- `docs/`: documentation, experiment summaries, and development notes
- `tests/`: automated tests
- `data/`: local datasets; do not commit large source data files
- `media/`: selected generated audio or MIDI examples

## Working Rules

- The user directs the scientific questions, listening judgments, and final experiment decisions.
- Do not make scientific, perceptual, or musical design decisions silently.
- Change one experimental dimension at a time unless the user explicitly asks for a broader comparison.
- Do not smooth, interpolate, fill gaps, remove outliers, change pitch ranges, change instruments, or optimize audio for pleasantness without explicit approval.
- Preserve `NaN` gaps and never interpolate across missing-data intervals.
- Document why a variable is mapped to an audio parameter.
- Prefer modular helper functions when behavior is stable, but keep experiment-specific configuration in notebooks.
- Keep development notes and failed experiments when they are part of the research record.
