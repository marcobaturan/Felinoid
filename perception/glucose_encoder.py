# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters
from utils.inform_tool import overlap_inform

# variables
null_glucose = 0.0
max_glucose = 1.0
w = 21


if __name__ == '__main__':
    params = ScalarEncoderParameters()
    params.minimum = null_glucose     # minimum glucose
    params.maximum = max_glucose      # maximum glucose
    params.activeBits = w             # with of window activation bits
    numbers = [100,105,110,112]       # 112 ES EL GANADOR EN CUANTO A SOLAPAMIENTO DE CODIFICADORES DE GLUCOSA.

    for number in numbers:
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


        # print the internal representation
        print("=====================================================================")
        print(f"for size of {number} bits.")
        print("Position for value 0.0: ", sdr_one.sparse)
        print("Position for value 0.2: ", sdr_two.sparse)
        print("Position for value 0.4: ", sdr_three.sparse)
        print("Position for value 0.6: ", sdr_four.sparse)
        print("Position for value 0.8: ", sdr_five.sparse)
        print("Position for value 1.0: ", sdr_six.sparse)
        print("=====================================================================")
        one = sdr_one.sparse.tolist()
        two = sdr_two.sparse.tolist()
        three = sdr_three.sparse.tolist()
        four = sdr_four.sparse.tolist()
        five = sdr_five.sparse.tolist()
        six = sdr_six.sparse.tolist()


        overlap_inform(one, two, three, four, five,six, w=w)
        print("=====================================================================")
