from htm.bindings.sdr import SDR
from adenosine_encoder import encode_adenosine
from glucose_encoder import encode_glucose
from tactile_encoder import encode_tactile
import time


def VisceralSDRF1(value):
    # receive the value to coding into SDR for every variable
    adenosine = SDR(encode_adenosine(value))
    glucose = SDR(encode_glucose(value))
    tactile = SDR(encode_tactile(value))
    # define the sum of every dimension of the variables; adenosine, glucose, tactile
    dimensions = SDR(282)
    # concatenate the SDRs by dimensions
    concatenation = dimensions.concatenate([adenosine,glucose,tactile])
    return concatenation.sparse.tolist()

if __name__ == '__main__':
    level = 0.0
    try:
        while level < 1.0: # run until reach the end or receive Ctrl + C
            # result of integration coding
            print(f"Visceral SDR(glucose, adenosine, tactile), level {level}; ", VisceralSDRF1(value=level))
            level += 0.1
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\n Simulation stopped.")