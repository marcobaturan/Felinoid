from htm.bindings.sdr import SDR
from htm.algorithms import SpatialPooler as SP
from htm.algorithms import TemporalMemory as TM
from perception.VisceralSDR_F1 import VisceralSDRF1
import time

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

sparse_list = []

def encode_spatial(adenosine: float, glucose: float) -> list[int]:
        """ Encode spatial
            Compute biochemical parameters to produce
            SDR iteration before temporal memory
        """
        sdr_visceral_SDRF1 = VisceralSDRF1(adenosine_value=adenosine, glucose_value=glucose)
        inputSDR.sparse = sdr_visceral_SDRF1
        sp.compute(inputSDR, True, activeSDR)
        active_SDR_clean_list = activeSDR.sparse
        return active_SDR_clean_list.tolist()

# Derived from documentation: htm.core/py/htm/examples/tm/hello_tm.py
tm = TM(columnDimensions = (2048,), # mod from chat remembering
        cellsPerColumn=1,           # the rest of params are equal as example by ignorance
        initialPermanence=0.5,
        connectedPermanence=0.5,
        minThreshold=8,
        maxNewSynapseCount=20,
        permanenceIncrement=0.1,
        permanenceDecrement=0.0,
        activationThreshold=8,
        )


if __name__ == "__main__":
        count = 0
        glucose = 1.0
        adenosine = 0.0

        while count < 10:
                # bloque de computo
                sparse_list.append(encode_spatial(adenosine=adenosine,glucose=glucose))
                count += 1
                glucose -= 0.1
                adenosine += 0.1
                # wait simulation
                time.sleep(0.1)

print(sparse_list)