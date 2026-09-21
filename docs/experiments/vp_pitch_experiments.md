# Vp Pitch Experiments

This file summarizes the completed `Vp -> pitch` experiments from Notebook 4. It preserves the practical sequence of what changed, what stayed fixed, what was heard, and why the next experiment followed.

## First Continuous Pitch Prototype

What changed:

- `Vp` was mapped directly to continuous sine-wave pitch.
- Early comparisons tried different pitch ranges, logarithmic versus linear mapping, inversion, and short playback durations.

What stayed constant:

- Only ACE SWEPAM `Vp` was used.
- Invalid samples and gaps remained explicit.
- The goal was to test whether pitch could carry solar-wind speed structure.

What I heard:

- The 12-second playback was too fast for detailed analysis.
- The broad pitch contour was difficult to follow and sounded somewhat random or noise-like.
- A larger missing-data gap was audible near seven seconds.
- Smaller gaps may have contributed to a busy or fragmented sound.
- Audible pops, buzzing, or gain-like peaks were present.
- The 300-600 Hz logarithmic mapping was more comfortable and wind-like but had less perceptible pitch variation.
- The 220-880 Hz logarithmic mapping produced clearer pitch contrast than the linear version.
- The inverted logarithmic version was recognizable as reversing the pitch direction.

What did not work:

- None of the first outputs were comfortable or interpretable enough for scientific listening.

Decision:

- Keep the 220-880 Hz non-inverted logarithmic mapping as a baseline for the next controlled comparison.
- Test playback duration and segment-aware pitch-control smoothing without changing the source data.

Open problem:

- The audio still had harsh transitions and was hard to follow.

## Controlled Continuous Pitch Comparison

What changed:

- Playback duration, smoothing window, and optional oscillator phase reset were compared.
- The baseline mapping stayed non-inverted, logarithmic, and 220-880 Hz.

What stayed constant:

- `Vp` remained the only mapped variable.
- Missing samples stayed silent.
- Smoothing affected only the pitch-control signal inside valid segments.
- No smoothing crossed missing-data gaps.
- Amplitude stayed constant and data-independent.

What I heard:

- 60 seconds was a reasonable playback duration.
- Continuous sine-wave pitch sounded robotic, harsh, and unpleasant.
- All smoothing levels preserved audible variation but remained unsuitable for sustained analysis.
- Pops were still audible.

What did not work:

- Comparing the continuous sine-wave clips in finer detail was not useful because the overall approach performed poorly perceptually.

Decision:

- Stop treating sample-by-sample continuous `Vp -> frequency` synthesis as the main candidate.
- Try temporal aggregation and discrete pitch events.

Open problem:

- The sound needed to be more listenable without hiding gaps or data changes.

## Discrete Pitch Event Prototype

What changed:

- `Vp` samples were aggregated into fixed-count temporal bins.
- Each sufficiently valid bin became a constant-amplitude chromatic note.
- Bins with insufficient valid data became silence.
- Comparisons used 60, 90, and 120 notes over 60 seconds.

What stayed constant:

- Only `Vp` was used.
- Playback duration stayed 60 seconds.
- Each bin used median valid `Vp`.
- The valid-data fraction threshold stayed explicit.
- Amplitude stayed constant.
- Attack and release were fixed rendering behavior, not data-driven loudness.

What I heard and saw:

- The discrete-note approach was much less robotic and more listenable than the continuous-frequency prototype.
- Flat sections in the MIDI-note plot were largely caused by different `Vp` bin medians being quantized to the same chromatic note.
- Re-triggering identical consecutive notes created repeated attacks that falsely implied new activity.
- Sudden note jumps came from both real aggregated `Vp` changes and semitone-boundary quantization.
- The MIDI 60-76 range compressed the physical range into too few pitch levels.
- Increasing the number of temporal bins alone would not solve the problem if pitch resolution stayed coarse.
- Familiar musical intervals and progressions could distract from scientific interpretation.

What did not work:

- Repeated attacks for unchanged pitch states made the sound misleading.
- Coarse chromatic quantization made some changes hard to judge.

Decision:

- Separate temporal aggregation, pitch quantization, and synthesis retriggering.
- Test sustained states and higher pitch resolution.

Open problem:

- Preserve continuity when the mapped state has not changed, while keeping real changes audible.

## Sustained Aggregated Pitch

What changed:

- Consecutive bins that mapped to the same state could be merged into one sustained event.
- Four clips compared sustained chromatic states, increased temporal resolution, wider pitch span, and aggregated microtonal pitch targets:
  - Clip A: 120 bins, MIDI 60-76, merged, no glide.
  - Clip B: 240 bins, MIDI 60-76, merged, short glide.
  - Clip C: 240 bins, MIDI 48-84, merged, short glide.
  - Clip D: 240 bins, microtonal targets, short glide.

What stayed constant:

- Playback duration stayed 60 seconds.
- Median `Vp` per bin was used.
- The minimum valid-data fraction threshold stayed at 0.5.
- Missing or rejected bins stayed silent.
- The normalization reference was fixed across clips.
- Amplitude remained data-independent.

What I heard:

- Sustained-state behavior was a major improvement because identical consecutive values remained continuous instead of being retriggered.
- This reduced popping and false rhythmic activity.
- Both the wide chromatic clip and the continuous microtonal clip still sounded too musical.
- The wider pitch span made familiar intervals and melodic patterns more noticeable.
- In the MIDI 48-84 clip, the first four audible notes were perceived as the first four notes of a minor scale.
- Musical training made recognizable scales, intervals, and progressions distracting.

What did not work:

- Wider pitch range improved contrast but also increased musical distraction.

Decision:

- Try a narrower sustained pitch range.
- Keep the continuity benefits of sustained states.

Open problem:

- Make meaningful `Vp` changes audible without pulling attention toward accidental melody.

## Narrow-Range Sustained Pitch

What changed:

- The comparison used 240 bins, sustained states, and a narrower pitch range.
- Clips E, F, G, and H compared continuous versus chromatic targets, sine versus modest-harmonic timbre, and 330-440 Hz versus 300-500 Hz continuous ranges.
- Clip G used chromatic MIDI 64-70 with sustained repeated notes.

What stayed constant:

- The source data, normalization reference, playback duration, valid-data threshold, constant amplitude, and fixed attack/release behavior stayed the same.
- Missing or rejected bins stayed silent.
- Glides never crossed missing-data gaps.

What I heard:

- Clip G was exported to MIDI and tested in a DAW with a different instrument.
- Hearing the notes as strings was much more pleasant than the original notebook audio.
- Changing instrument improved comfort, but it did not fix the large pitch jumps.
- The remaining gaps and jumps still sounded jarring.

What did not work:

- Timbre alone did not solve transition problems.
- Immediate jumps between distant notes remained a problem.

Decision:

- The next experiment should focus on pitch transitions between sustained states.

Open problem:

- A short glide may make large jumps easier to follow, but it could blur short events. Duration-aware transitions need to be tested without changing the underlying `Vp` mapping or hiding brief spikes.
