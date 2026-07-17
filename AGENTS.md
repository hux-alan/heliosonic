# HelioSonic Development Instructions

## Project Overview

HelioSonic is a research-oriented heliophysics sonification project.

The goal is to transform spacecraft measurements into meaningful auditory representations for:
- scientific exploration
- accessibility applications
- understanding complex space physics phenomena

This is not primarily a music composition project. Scientific interpretation and preservation of physical meaning are priorities.

---

## Current Development Phase

The project is currently in the data exploration phase.

Current focus:
- Understanding CDAWeb spacecraft datasets
- Loading CDF files
- Exploring variables
- Determining meaningful sonification mappings

Do not prematurely build the audio synthesis pipeline before validating the scientific variables.

---

## Technical Stack

Language:
- Python

Environment:
- Jupyter notebooks
- VS Code
- Conda environment: heliosonic

Libraries currently used:
- spacepy
- cdflib
- numpy
- pandas
- matplotlib

---

## Repository Structure

notebooks/
- exploratory analysis
- data investigation

src/
- reusable Python modules

docs/
- documentation and project notes

tests/
- automated tests

data/
- local datasets (do not commit large files)

---

## Coding Style

When writing code:
- Prefer modular functions over notebook-only code
- Add comments explaining scientific reasoning
- Use clear variable names
- Avoid unnecessary complexity
- Preserve reproducibility

---

## Scientific Considerations

When implementing sonification:
- Physical interpretation matters more than aesthetics
- Document why variables are mapped to sound parameters
- Avoid transformations that hide meaningful scientific signals

---

## Current Dataset

Primary exploration:
- ACE spacecraft data
- CDAWeb CDF format

Important variables may include:
- magnetic field components
- plasma density
- solar wind velocity

Always verify variable meaning before using it.