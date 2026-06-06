# Hardware + AI Project Menu

Choose projects that produce physical evidence, measured results, and useful
engineering tradeoffs. Avoid projects where the AI is only a chat interface
wrapped around an API.

## Recommended Sequence

### 1. Edge Vibration Anomaly Monitor

**Build:** Mount an accelerometer to a small motor or fan, collect vibration
signals, extract DSP features, and detect abnormal operation on an ESP32-S3.

**Why it is strong:** It combines sensor selection, sampling, embedded firmware,
signal processing, model evaluation, and edge deployment. A live demo is easy to
understand.

**Portfolio evidence:** Confusion matrix, false-alarm rate, inference latency,
memory use, power draw, sensor mounting experiments, and a real-time demo.

**Estimated budget:** USD 30-70.

### 2. Battery Health and Load-Test Station

**Build:** Create a safe low-voltage battery characterization rig that logs
voltage, current, temperature, and discharge curves. Predict capacity or flag
degrading cells.

**Why it is strong:** It demonstrates power measurement, calibration, safe test
design, data pipelines, and regression/anomaly models.

**Portfolio evidence:** Calibration report, repeatability study, prediction error,
thermal limits, and safety controls.

**Important:** Start with protected, low-energy cells or supervised lab
equipment. Do not improvise around damaged lithium batteries.

### 3. PCB Visual Inspection Assistant

**Build:** Use a fixed camera and controlled lighting to detect missing,
misaligned, or incorrectly oriented components on a small PCB.

**Why it is strong:** The hard parts are hardware-friendly: fixture design,
lighting, image repeatability, dataset quality, and measurable defect detection.

**Portfolio evidence:** Fixture CAD, image dataset, defect taxonomy, precision and
recall, and examples of false positives.

**Estimated budget:** USD 40-120, depending on the camera and lighting.

### 4. AI-Assisted Bench Instrument

**Build:** Connect to an oscilloscope, logic analyzer, or programmable supply via
SCPI or its API. Automatically run tests, analyze captures, and draft a report
that links every claim to measured data.

**Why it is strong:** It shows test engineering, automation, trustworthy AI use,
and good human approval boundaries.

**Portfolio evidence:** Reproducible test plans, generated plots, cited
measurements, guardrails, and a sample failure investigation.

### 5. FPGA Streaming Signal Classifier

**Build:** Implement a small classifier or anomaly detector in fixed-point RTL
and compare it with a Python reference.

**Why it is strong:** It demonstrates that you understand where AI meets actual
hardware constraints.

**Portfolio evidence:** Cycle latency, maximum clock rate, resource use, power
estimate, fixed-point error, and hardware/software comparison.

## Selection Rule

Build the vibration monitor first unless another project matches equipment you
already own or a problem from your work. Finish it through a measured demo before
starting the next project.

