from htm.bindings.sdr import SDR
from htm.algorithms import SpatialPooler as SP
from perception.VisceralSDR_F1 import VisceralSDRF1
from utils.inform_tool import overlap_inform
import time

# sdr_visceral_SDRF1 = VisceralSDRF1(adenosine_value=0.0, glucose_value=1.0)

# derived from examples sp
# Create the Spatial Pooler, and the SDR data structures needed to work with it.
inputSDR  = SDR( dimensions = (232,) )
activeSDR = SDR( dimensions = (2048,) )

sp = SP(inputDimensions    = inputSDR.dimensions,
        columnDimensions   = activeSDR.dimensions,
        localAreaDensity   = 0.02,
        globalInhibition   = True,
        seed               = 1,
        synPermActiveInc   = 0.01,
        synPermInactiveDec = 0.008)

# add sdr visceral  to sparse input attribute
# inputSDR.sparse = sdr_visceral_SDRF1
# sp.compute(inputSDR, True, activeSDR)
# get active layer
sparse_list = []
if __name__ == "__main__":
        count = 0
        glucose = 1.0
        adenosine = 0.0

        while count < 10:
                # bloque de computo
                sdr_visceral_SDRF1 = VisceralSDRF1(adenosine_value=adenosine, glucose_value=glucose)
                inputSDR.sparse = sdr_visceral_SDRF1
                sp.compute(inputSDR, True, activeSDR)
                # get active layer
                print(f'second {count}, glucose {glucose}, adenosine {adenosine}: ', activeSDR.sparse)
                print((2 * len(activeSDR.sparse)) * '-') # just for aesthetics
                active_SDR_clean_list = activeSDR.sparse
                count += 1
                glucose -= 0.1
                adenosine += 0.1
                # wait simulation
                time.sleep(0.1)
                # noinspection PyArgumentList
                sparse_list.append(active_SDR_clean_list.tolist())
sl = sparse_list
print("Overlap inform:")
overlap_inform(sl[0],sl[1],sl[2],sl[3],sl[4],sl[5],sl[6],sl[7],sl[8],sl[9], w=21)
print('-------------------------------------------------------------')