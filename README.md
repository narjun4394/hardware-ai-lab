# Hardware AI Lab

This repository is my public build log for learning and applying AI as a hardware
engineer. Each project is designed to prove a complete engineering loop:

1. Define a real physical problem.
2. Instrument it and collect data.
3. Build a baseline before adding AI.
4. Measure accuracy, latency, power, cost, and failure cases.
5. Publish the design decisions, code, test results, and demo.

## Current Build

### Edge Vibration Anomaly Monitor

Detect unusual behavior in a small motor or fan using an accelerometer and an
ESP32-S3. The first software prototype extracts useful vibration features from
normal and fault-like signals. Later milestones move data collection and
inference onto real hardware.

- [Project brief](projects/01-edge-vibration-monitor/README.md)
- Run the first demo: `make demo`
- Run the tests: `make test`

## Project Ladder

| Stage | Project | What it proves |
| --- | --- | --- |
| 1 | Edge vibration anomaly monitor | Sensors, DSP, TinyML, validation |
| 2 | Battery health and load-test station | Power electronics, test automation, prediction |
| 3 | PCB visual inspection assistant | Computer vision, fixtures, defect datasets |
| 4 | AI-assisted bench instrument | SCPI automation, waveform analysis, human-in-the-loop AI |
| 5 | FPGA streaming signal classifier | RTL, fixed-point design, latency and resource tradeoffs |

See [PROJECTS.md](PROJECTS.md) for the detailed project menu and selection
criteria.

## Portfolio Standard

Every finished project should include:

- A 60-90 second demo video or GIF
- A block diagram and a readable schematic
- A bill of materials with total cost
- Reproducible firmware, software, and setup instructions
- Test data and quantitative results
- A short section called "What failed and what I changed"
- Issues and milestones showing how the work progressed

## Build Rhythm

- Commit small, understandable changes several times per week.
- Open an issue before each meaningful milestone.
- Write a weekly learning log, including failures and measurements.
- Tag working demos as releases.
- Keep unfinished work visible, but label it honestly.

The goal is not a wall of repositories. The goal is three finished projects that
make engineering judgment visible.

