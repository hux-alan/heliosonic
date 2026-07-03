# HelioSonic

> An open-source project exploring the use of data sonification for heliophysics research.

**Status:** Early Development (Summer 2026)

---

## Overview

HelioSonic is an independent software project investigating how spacecraft telemetry can be translated into sound to complement traditional visual analysis.

The project explores whether parameter-mapping sonification can help researchers better identify patterns, transitions, and transient events within heliophysics datasets while also improving the accessibility of scientific data.

Rather than replacing existing visualization tools, HelioSonic aims to provide an additional way of interacting with complex time-series data.

---

## Motivation

Space physics datasets often contain millions of measurements collected over long periods of time. Researchers typically identify events by visually inspecting plots of magnetic field, plasma, and particle measurements.

Human hearing is naturally sensitive to changes in rhythm, pitch, and timbre. HelioSonic explores whether those perceptual strengths can complement traditional visualization techniques when exploring spacecraft observations.

The project is inspired by three interests:

- Heliophysics research
- Music and audio engineering
- Scientific software development

---

## Current Goals

This summer, the project focuses on building a reliable engineering foundation before investigating research questions.

Current objectives include:

- Build a reproducible pipeline for reading NASA CDF files
- Develop a modular sonification engine
- Explore multiple parameter-to-audio mapping strategies
- Compare different normalization methods
- Produce reproducible audio demonstrations

Future work may investigate:

- Scientific event exploration
- Accessibility for blind and low-vision researchers
- Human-computer interaction
- AI-assisted scientific workflows

---

# Development Roadmap

## Phase 1 — Data Pipeline

**Status:** In Progress

Objectives:

- Read Level-2 spacecraft CDF files
- Extract selected physical variables
- Handle missing values and metadata
- Normalize physical units
- Build reusable preprocessing functions

Planned libraries:

- Python
- NumPy
- SciPy
- cdflib
- SpacePy

---

## Phase 2 — Sonification Engine

**Status:** Planned

The first prototype will investigate simple parameter-mapping sonification.

Example mappings under consideration:

| Physical Quantity | Audio Property |
|------------------|---------------|
| Magnetic field magnitude | Pitch |
| Plasma density | Timbre |
| Solar wind speed | Tempo |
| Magnetic field direction | Stereo position |

These mappings are experimental and will likely evolve throughout development.

---

## Phase 3 — Prototype Evaluation

Once the initial prototype is functional, the project will compare different sonification approaches by asking questions such as:

- Which mappings are easiest to distinguish?
- Which preserve meaningful physical structure?
- Which become fatiguing over long listening sessions?
- How should multiple variables be represented simultaneously?

---

# Repository Structure

```
heliosonic/

├── README.md
├── LICENSE
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── mapping.py
│   └── sonification.py
│
├── notebooks/
│   └── prototype.ipynb
│
├── examples/
│
├── docs/
│   ├── roadmap.md
│   ├── design_notes.md
│   └── devlog.md
│
├── media/
│
└── tests/
```

---

# Engineering Philosophy

This repository is intended to document the engineering process rather than only the finished software.

Development emphasizes:

- Small, testable milestones
- Reproducible experiments
- Iterative design
- Open documentation
- Clear engineering decisions

Both successful prototypes and failed experiments will be documented as the project evolves.

---

# Development Log

Major milestones will be tracked in `docs/devlog.md`.

Example entries include:

- Prototype updates
- Architecture decisions
- Audio mapping experiments
- Performance improvements
- Research discussions
- Lessons learned

---

# Current Progress

## Completed

- Project planning
- Initial architecture
- Repository setup
- Licensing
- Literature review on sonification
- Preliminary software design

## In Progress

- Data ingestion pipeline
- Parameter normalization
- First prototype

## Planned

- Audio synthesis engine
- Demonstration notebooks
- Example audio outputs
- Validation experiments
- Documentation website

---

# Long-Term Vision

HelioSonic is intended to become an open-source platform for exploring sonification within heliophysics.

Possible future directions include:

- Support for additional NASA missions
- Interactive visualization interfaces
- AI-assisted event exploration
- Educational demonstrations
- Community contributions

As the project matures, documentation and code examples will expand alongside new functionality.

---

# Acknowledgments

This project is developed independently while drawing inspiration from ongoing heliophysics research and open scientific software communities.

The project benefits from discussions with researchers working in space physics and scientific computing.

---

# License

Licensed under the Apache License 2.0.

See the `LICENSE` file for details.