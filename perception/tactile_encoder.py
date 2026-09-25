# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters


# variables
# extract here the variables and parameters to reduce computation
null_pres = 0.0
max_pres = 1.0
w = 21
params = ScalarEncoderParameters()
params.minimum = null_pres  # Null pressure
params.maximum = max_pres  # max pressure
params.activeBits = w  # With of windows activation bits
params.size = 50  # 50 IS THE BEST VALUE AFTER PASS UTILS/INFORM_OVERLAP FUNCTION
encoder = ScalarEncoder(params) # start encoder with params

def encode_tactile(value: float) -> list[int]:
    # SDR produce list of vector.
    return encoder.encode(value)