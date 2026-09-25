# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters
from utils.inform_tool import overlap_inform
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
    params.activeBits = w # Ancho de la ventana (bits encendidos 'w')
    numbers = [24, 30, 40, 50]  # 50 ES EL GANADOR EN CUANTO A SOLAPAMIENTO DE CODIFICADORES DE PRESIÓN.

    for number in numbers:
        params.size = number

        # start encoder with params
        encoder = ScalarEncoder(params)

        # encode 4 values of back pressure point
        sdr_one = encoder.encode(0.0)   # minimal back pressure
        sdr_two = encoder.encode(0.2)   # middel pressure
        sdr_three = encoder.encode(0.6) # high pressure
        sdr_four = encoder.encode(1.0)  # max level

        # print the internal representation
        print("=====================================================================")
        print(f"for size of {number} bits.")
        print("Position for value 0.0: ", sdr_one.sparse)
        print("Position for value 0.2: ", sdr_two.sparse)
        print("Position for value 0.6: ", sdr_three.sparse)
        print("Position for value 1.0: ", sdr_four.sparse)
        print("=====================================================================")
        lista = sdr_one.sparse.tolist()
        listb = sdr_two.sparse.tolist()
        listc = sdr_three.sparse.tolist()
        listd = sdr_four.sparse.tolist()

        overlap_inform(lista,listb,listc,listd,w=w)
        print("=====================================================================")
        