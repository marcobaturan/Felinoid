# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters

# variables
null = 0.0
max_pres = 1.0
w = 21
# 1. Definition of the encoder's params; usar la formula, n = w + bucket - 1.
# buckets = 4, 10, 20, 30
# Case A-> n = 21 + 4- 1 => 24
# Case b-> n = 21 + 10-1 => 30
# Case c-> n = 21 + 20-1 => 40
# Case d-> n = 21 + 30-1 => 50

if __name__ == '__main__':
    params = ScalarEncoderParameters()
    params.minimum = null  # Null pressure
    params.maximum = max_pres  # max pressure
    params.activeBits = w # With of windows activation bits
    number = 50 # 50 IS THE BEST VALUE AFTER PASS UTILS/INFORM_OVERLAP FUNCTION
    params.size = number

    # start encoder with params
    encoder = ScalarEncoder(params)

    # encode 4 values of back pressure point
    sdr_one = encoder.encode(0.0)   # minimal back pressure
    sdr_two = encoder.encode(0.2)   # middel pressure
    sdr_three = encoder.encode(0.6) # high pressure
    sdr_four = encoder.encode(1.0)  # max level

    # Internal representations
    lista = sdr_one.sparse.tolist()
    listb = sdr_two.sparse.tolist()
    listc = sdr_three.sparse.tolist()
    listd = sdr_four.sparse.tolist()
