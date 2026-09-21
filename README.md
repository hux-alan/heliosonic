# HelioSonic

HelioSonic is an open-source project exploring how heliophysics data can be represented through sound for scientific research and accessibility.

Most spacecraft data is studied through plots. Sonification offers another way to notice changes, patterns, gaps, and short events within the same data. The goal of HelioSonic is not to turn space data into music, but to test which sound mappings are clear, useful, and still accurate to the original measurements.

**Status:** Active development  
**Current focus:** Sonifying solar-wind speed through pitch

## Current Progress

The project currently uses ACE SWEPAM Level 2 data from NASA CDAWeb. The first three notebooks established the data workflow by loading CDF files, checking metadata and missing values, comparing variables, and testing normalization methods.

Notebook 4 begins the actual sonification work. So far, I have:

- created the first reusable pitch-mapping and audio-synthesis framework;
- generated continuous and discrete-pitch versions of solar-wind speed (`Vp`);
- compared different playback speeds, pitch ranges, note densities, and normalization methods;
- preserved missing measurements instead of interpolating across them;
- exported one prototype as MIDI and tested different instruments; and
- recorded listening observations in the notebook and development logs.

The discrete-note prototypes have been easier to follow than the original continuous sine-wave versions. Changing the instrument also made the audio much more comfortable to hear, but it did not fix the large jumps between some pitches. Wider pitch ranges made changes clearer, although they also created accidental melodies that could distract from the data.

## Current Experiment

The next experiment will focus on transitions between sustained pitches.

An immediate jump between two distant pitches can sound jarring. A short glide may make the change easier to follow, but it could also blur a spike that lasts only a fraction of a second. I plan to compare hard transitions, fixed glides, and glides that adjust to the duration of each event while keeping the other audio settings the same.

## Notebooks

| Notebook | Focus |
| --- | --- |
| `01_explore_CDF.ipynb` | Load and inspect NASA CDF data |
| `02_understand_variables.ipynb` | Study data quality, distributions, and possible variables |
| `03_normalize_variables.ipynb` | Compare normalization methods before sonification |
| `04_sonification_mapping.ipynb` | Build and listen to the first sonification prototypes |

## Working Principles

- Preserve gaps and scientifically meaningful changes in the data.
- Change one part of the mapping at a time so comparisons remain useful.
- Do not make the audio smoother or more musical unless the effect on the data is understood.
- Keep pitch, volume, rhythm, duration, timbre, and stereo position available as possible ways to represent different variables.
- Document unsuccessful experiments as well as successful ones.

## Repository Structure

```text
heliosonic/
|-- notebooks/       # Data exploration and sonification experiments
|-- docs/devlog/     # Dated development notes
|-- media/           # Audio and MIDI examples
|-- examples/        # Example workflows and outputs
|-- src/             # Reusable code as the project develops
|-- tests/           # Future automated tests
|-- AGENTS.md
|-- requirements.txt
`-- LICENSE
```

## Setup

```bash
git clone https://github.com/hux-alan/heliosonic.git
cd heliosonic
python -m pip install -r requirements.txt
```

The source CDF files are not stored in the repository, so the notebooks may require a local ACE SWEPAM file and an updated data path.

## Collaborating

I am currently looking for people interested in helping with heliophysics, audio and signal processing, accessibility, human-computer interaction, Python development, or documentation.

Before changing a sonification method, please look through the related notebook and recent development logs. New experiments should make clear what is being changed, what is being held constant, and what information the change could hide or distort.

Some of the main areas I hope to work on next are:

- testing pitch-transition methods without losing short events;
- moving stable notebook code into reusable modules;
- connecting sounds back to exact spacecraft times and measurements;
- developing better ways to evaluate clarity and listening fatigue;
- exploring additional variables after the first pitch framework is stronger; and
- eventually working with blind and low-vision users to evaluate accessibility.

## Long-Term Direction

I hope to develop HelioSonic into a tool where researchers can load a heliophysics dataset, inspect its variables, choose how they are mapped to sound, compare different sonifications, and connect what they hear back to the original measurements.

Sonification would not replace plots. It would give researchers another way to explore the same data and make that data usable by more people.

## License

Licensed under the Apache License 2.0. See `LICENSE` for details.
