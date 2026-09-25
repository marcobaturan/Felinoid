# Interface Contracts - FELYNOYD Project (Phases 1 and 2 - Minimum Scope)

This document contains the minimum subset strictly necessary to validate the isolated symbolic body infrastructure (Phase 1) and the pipeline for a sensor with its complete binarization (Phase 2).

## 1. Temporal Lifecycle (Tick)

* **Main Loop Frequency:** 10 Hz (1 tick = 100 ms).
* **Behavior:** Every 100 ms, the visceral metabolic state is updated (Phase 1), the tactile sensor is read (Phase 2), the data is binarized in an SDR, and sent to the basic classifier.

---

## 2. Body/Visceral State Interface (Phase 1)

* Reduced to the two critical, continuous metabolic variables that interact as drivers of basal motivation.
* The dataclass remains mutable because is more flexible and the code is more simple and clean.
* I add Ctrl + C to cut the visceral integration cycle to maintain a simple code.

### A. Internal Sensory Input

```python
from dataclasses import dataclass
from typing import Tuple, List

@dataclass()
class VisceralStateF1:
    blood_glucose: float       # Range [0.0, 1.0]. 1.0 = Satiated, 0.0 = Starvation (Critical hunger)
    accumulated_adenosine: float  # Range [0.0, 1.0]. 0.0 = Awake/Alert, 1.0 = Extreme Fatigue

```

### B. SDR Encoder Specification

To transform `blood_glucose` into a binary vector, we will use a scalar encoder from `htm.core`

* **Encoder Type:** `htm.bindings.encoders.ScalarEncoder`
* **Contract Design Parameters:**
* **Cube Width (`w`):** 21 active bits (I’m choosing these parameters because they’re the only ones I know).
* **Total Size (`n`):** 112 bits ("I wanted 5 buckets: stuffed, full, normal, hungry, and critical. The theoretical formula for 5 buckets gave n=25. However, n=112 was decided empirically, not by direct formula, to resolve a bug where adjacent buckets (like 0.4 and 0.6) were producing identical SDRs.").
* **Input range:** `[0.0, 1.0]`
* **Periodicity:** False ([detached]:I contradicted myself because I forgot the first argument).



To transform `accumulated_adenosine` into a binary vector, we’ll use a scalar encoder from `htm.core`

* **Encoder Type:** `htm.bindings.encoders.ScalarEncoder`
* **Contract Design Parameters:**
* **Cube Width (`w`):** 21 active bits (I’m choosing these parameters because they’re the only ones I know).
* **Total Size (`n`):** 120 bits (11 states).
* **Input range:** `[0.0, 1.0]`
* **Periodicity:** False (This does not signify cycles but rather a reset as soon as sleep is entered. Do not add a ‘time’ variable because a non-sentient animal does not understand time, but rather events/conditioning/internal states).
* **Granularity:** Pass from 5 to 11 buckets because after read about relation of sleep pressure and adenosine concentration in the brain, I decide more fine grain representation biochemistry of brain dynamics.



### C. SDR Output Structure

```python
@dataclass(frozen=True)
class VisceralSDRF1:
    dimensions: Tuple[int] = (232,)  # 112 (glucose) + 120 (adenosine)
    sparse_indices: List[int]

```

---

## 3. Raw Sensory Interface and Full Binarization (Phase 2)

**Touch** (Back Pressure Sensor) is selected as the sole sense for initial validation.

### A. Raw Sensory Input (Phase 1 / Input to Perception)

```python
@dataclass(frozen=True)
class TactileInputF1:
    back_pressure: float  # Range [0.0, 1.0]. 0.0 = No contact, 1.0 = Maximum (painful) pressure

```

### B. Encoder Specification (SDR Encoder)

To transform `back_pressure` (a continuous floating-point value from 0.0 to 1.0) into a sparse binary vector, we will use a **Scalar Encoder** from `htm.core`.

* **Encoder Type:** `htm.bindings.encoders.ScalarEncoder`
* **Contract Design Parameters:**
* **Cube Width (`w`):** 21 active bits (number of bits set to `1` that will represent the value).
* **Total Size (`n`):** 50 bits (Vector space dimension. 5 levels. I discarded medical pressure tests used on mammals because they rely on subjective evaluation from the doctor and the animal cannot communicate the exact threshold).
* **Input Range:** `[0.0, 1.0]`
* **Periodicity:** False (Non-cyclic).



### C. SDR Output Structure (Perception → Memory/Classifier Contract)

The output format strictly complies with the C++ requirement of `htm.core`: an indexed and sorted list of active bits.

```python
@dataclass(frozen=True)
class SpatialRepresentationF1:
    dimensions: Tuple[int] = (50,)
    sparse_indices: List[int]  # Sorted list of exactly 21 integers (positions of the bits set to 1)

```

---

## 4. Minimum Decision Vector Interface

A reduced motor command that allows the cognitive layer to feed back into the simulation or metabolism (e.g., triggering a reflex action in response to pain caused by excessive pressure).

```python
@dataclass(frozen=True)
class MotorActuatorsF1:
    alert_reaction: bool  # True if the pressure/pain level triggers an evasive response

```