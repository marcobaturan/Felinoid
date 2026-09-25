# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters


# variables
# extract here the variables and parameters to reduce computation
null_glucose = 0.0
max_glucose = 1.0
w = 21
params = ScalarEncoderParameters()
params.minimum = null_glucose  # minimum glucose
params.maximum = max_glucose  # maximum glucose
params.activeBits = w  # with of window activation bits
params.size = 112  # 112 IS THE BEST VALUE AFTER PASS UTILS/INFORM_OVERLAP FUNCTION
encoder = ScalarEncoder(params) # start encoder with params

def encode_glucose(value: float) -> list[int]:
    # SDR produce list of vector.
    return encoder.encode(value)
