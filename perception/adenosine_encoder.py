# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters


# variables
# extract here the variables and parameters to reduce computation
null_adenosine = 0.0
max_adenosine = 1.0
w = 21
params = ScalarEncoderParameters()
params.minimum = null_adenosine  # minimum adenosine
params.maximum = max_adenosine  # maximum adenosine
params.activeBits = w  # with of window activation bits
params.size = 120  # 120 IS THE BEST VALUE AFTER PASS UTILS/INFORM_OVERLAP FUNCTION
encoder = ScalarEncoder(params) # start encoder with params

def encode_adenosine(value: float) -> list[int]:
    # SDR produce list of vector.
    return encoder.encode(value).sparse.tolist()
