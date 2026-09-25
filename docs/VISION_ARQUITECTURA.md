
# Interface Contracts - FELYNOYD Project (Phase 0)

## 1. Temporal Lifecycle and Environment
*   **Loop Frequency (Tick):** 10 Hz (1 tick = 100 ms).
*   **Environment Dimensions (Skinner Box):** Enclosed cube measuring \(X \times Y \times Z\) meters.
*   **Orientation of Environmental Actuators (Walls):**
    *   **North:** Feeder (Variable flavor/odor dispenser).
    *   **South:** Water dispenser (water fountain with freshness sensor).
    *   **East:** Litter box (elimination area).
    *   **West:** Interactive screen (live video/audio stream from the webcam).
    *   **Center:** Circular soft bed (rest and sleep area)
*   **Agent Morphology:** Robotic quadruped with joints in the head, neck, tail, and 4 limbs.

---

## 2. Raw Sensory Interface (Webots Output -> Perception Input)

### A. Vision (Stereoscopic Cameras)
Two independent cameras (Left Eye / Right Eye) limited to the feline spectrum (Blue, Yellow, Green).
*   **Resolution:** 100 x 100 pixels per channel.
*   **Value Range:** 0.0 (Absence) to 1.0 (Color Saturation).

```python
from dataclasses import dataclass
import numpy as np
from typing import Tuple, List

@dataclass(frozen=True)
class EyeChannels:
    blue: np.ndarray    # 100x100 array of type float32
    yellow: np.ndarray  # 100x100 array of type float32
    green: np.ndarray   # 100x100 array of type float32

@dataclass(frozen=True)
class VisionInput:
    left_eye: EyeChannels
    right_eye: EyeChannels
```

### B. Hearing (Directional and Frequency)
*   **Pitch/Frequency:** Extended range from 0.05 kHz to 64 kHz.
*   **Intensity:** Normalized decibels [0.0, 1.0].
*   **Direction:** Unit vector relative to the robot’s head.

```python
@dataclass(frozen=True)
class HearingInput:
    frequency_hz: float
    intensity: float
    relative_direction: Tuple[float, float, float]  # Vector (x, y, z)
```

### C. Touch (Collective Body Surface)
Records contact and pressure across the 7 key body zones. Pain and pleasure are calculated based on the time derivative of pressure (intensity vs. rate of impact/friction).

```python
@dataclass(frozen=True)
class TouchZone:
    pressure: float          # Range [0.0, 1.0]
    pressure_derivative: float # Rate of change (Impact vs. Caress)

@dataclass(frozen=True)
class TactileInput:
    head: TouchZone
    neck: TouchZone
    back: TouchZone
    tail: TouchZone
    front_legs: TouchZone
    hind_legs: TouchZone
    belly: TouchZone
```

### D. Taste (Lingual Receptors)
Chemical activation upon contact with colloids in the feeder/waterer.

```python
@dataclass(frozen=True)
class TasteInput:
    umami: float   # TAS1R1/TAS1R3 receptors (meat/tuna) - High sensitivity
    sour: float   # High feline tolerance
    bitter: float  # Defense mechanism (poison avoidance)
    salty: float  # Variable sensitivity
    water: float    # Specific freshness receptors on the tongue
```

### E. Sense of Smell (Volatile Compounds and Pheromones Matrix)
Classification of volatile compounds based on biological impact.

```python
@dataclass(frozen=True)
class SmellInput:
    # Biological
    tuna_food: float
    feces_urine: float
    # Emotional / Social
    known_human_pheromone: float
    alert_pheromone: float
    # Behavioral (Repellents / Attractants)
    citrus_repellent: float
    catnip_attractant: float
```

---

## 3. Bodily/Visceral State Interface (Internal Output -> Cognitive Input)
Mapping of mechanical pressure on internal organs and symbolic metabolic curves.
*   **Organic Matrix:** A \(3 \times 3\) grid that simulates the packing of the torso.

```python
@dataclass(frozen=True)
class VisceralState:
    # Symbolic metabolic curves
    blood_glucose: float       # Modulates Hunger [0.0, 1.0]
    accumulated_adenosine: float  # Modulates Sleep (Polyphasic Cycle) [0.0, 1.0]
    adrenaline: float           # Modulates the overall update rate [0.0, 1.0]
    internal_temperature: float  # Affects the respiratory rate [0.0, 1.0]

    # Organ Pressure (3x3 matrix of internal deformation)
    # [Left_Lung,  Heart,   Right_Lung]
    # [Stomach,  Liver,    Intestine]
    # [Bladder,    Sphincter,  Abdominal_Fat]
    organ_pressure_matrix: np.ndarray  # 3x3 float32 matrix
```

---

## 4. SDR / Binarized Format (Perception Contract -> HTM Memory)
Each sense mapped in step 2 will be processed through a specific encoder in `htm.core` during Phase 2. The final contract received by the HTM brain is the structured union of these sub-vectors into the **Grand Master Vector**.

| Sensory Sub-SDR | Bit Dimension (`n`) | Maximum Sparsity (`w`) |
| :--- | :--- | :--- |
| `SDR_Vision` | 4096 | 2.0% |
| `SDR_Audio` | 1024 | 2.0% |
| `SDR_Touch` | 1024 | 2.0% |
| `SDR_Taste_Smell` | 2048 | 2.0% |
| `SDR_Visceral` | 2048 | 2.0% |
| **TOTAL MASTER** | **11,264 bits** | **~2.0% Active** |

```python
@dataclass(frozen=True)
class BrainSDRInput:
    dimensions: Tuple[int] = (11264,)
    # List of integers with the sorted indices of the bits set to 1 (htm.core C++ requirement)
    sparse_indices: List[int]
```

---

## 5. Decision Vector Interface (Cognition Output -> Action/Webots Input)
Speed control commands for the quadruped’s physical motors and sphincter actions.

```python
@dataclass(frozen=True)
class MotorActuators:
    legs: Tuple[float, float, float, float] # Linear velocities [-1.0, 1.0]
    neck_head: Tuple[float, float]        # Rotation (Pitch, Yaw)
    tail: float                               # Roll

@dataclass(frozen=True)
class PhysiologicalActions:
    open_sphincter: float    # If > 0.8, defecates at Webots' current position
    gaping_flehmen: bool     # Opens mouth to absorb pheromones into the vomeronasal organ
```

