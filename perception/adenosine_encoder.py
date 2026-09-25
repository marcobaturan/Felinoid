# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters

# variables
null_adenosine = 0.0
max_adenosine = 1.0
w = 21


if __name__ == '__main__':
    # variables
    params = ScalarEncoderParameters()
    params.minimum = null_adenosine     # minimum adenosine
    params.maximum = max_adenosine      # maximum adenosine
    params.activeBits = w               # with of window activation bits
    number = 120                        # 120 IS THE BEST VALUE AFTER PASS UTILS/INFORM_OVERLAP FUNCTION
    params.size = number
    # start encoder with params
    encoder = ScalarEncoder(params)

    # encode 4 values of back pressure point
    sdr_zero = encoder.encode(0.0)
    sdr_one = encoder.encode(0.1)
    sdr_two = encoder.encode(0.2)
    sdr_three = encoder.encode(0.3)
    sdr_four = encoder.encode(0.4)
    sdr_five = encoder.encode(0.5)
    sdr_six  = encoder.encode(0.6)
    sdr_seven = encoder.encode(0.7)
    sdr_eight = encoder.encode(0.8)
    sdr_nine = encoder.encode(0.9)
    sdr_ten = encoder.encode(1.0)

    # Representations
    one = sdr_one.sparse.tolist()
    two = sdr_two.sparse.tolist()
    three = sdr_three.sparse.tolist()
    four = sdr_four.sparse.tolist()
    five = sdr_five.sparse.tolist()
    six = sdr_six.sparse.tolist()
    seven = sdr_seven.sparse.tolist()
    eight = sdr_eight.sparse.tolist()
    nine = sdr_nine.sparse.tolist()
    ten = sdr_ten.sparse.tolist()
