from htm.bindings.sdr import SDR
from .adenosine_encoder import encode_adenosine
from .glucose_encoder import encode_glucose
import time




def VisceralSDRF1(glucose_value: float, adenosine_value: float) -> list[int]:
    glucose_sdr = encode_glucose(glucose_value)
    adenosine_sdr = encode_adenosine(adenosine_value)
    combined = SDR(232)
    combined.concatenate([glucose_sdr, adenosine_sdr])

    return combined.sparse.tolist()
