# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters

# variables
null_glucose = 0.0
max_glucose = 1.0
w = 21


if __name__ == '__main__':
    # Variables
    params = ScalarEncoderParameters()
    params.minimum = null_glucose     # minimum glucose
    params.maximum = max_glucose      # maximum glucose
    params.activeBits = w             # with of window activation bits
    number = 112                      # 112 IS THE BEST VALUE AFTER PASS UTILS/INFORM_OVERLAP FUNCTION
    params.size = number

    # start encoder with params
    encoder = ScalarEncoder(params)
    # encode 4 values of back pressure point
    sdr_one = encoder.encode(0.0)    # critic
    sdr_two = encoder.encode(0.2)    # strong hunger
    sdr_three = encoder.encode(0.4)  # soft hunger
    sdr_four = encoder.encode(0.6)   # normal
    sdr_five = encoder.encode(0.8)   # near full
    sdr_six  = encoder.encode(1.0)   # full
    # SDR produce list of vector.
    one = sdr_one.sparse.tolist()
    two = sdr_two.sparse.tolist()
    three = sdr_three.sparse.tolist()
    four = sdr_four.sparse.tolist()
    five = sdr_five.sparse.tolist()
    six = sdr_six.sparse.tolist()
