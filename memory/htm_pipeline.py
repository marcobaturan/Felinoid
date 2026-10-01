__doc__ = """
This program build the HTM pipeline to connect visceral state of the organism from encoders to SP and TM.
Establishing a bridge between inner body states and neocortex in order to learn how to self perceive the 
model of self in order to improve the cognitive cycle of perceive-learn-think-act and complement the 
external perceptions.
"""

# imports
from htm.bindings.sdr import SDR
from htm.algorithms import SpatialPooler as SP
from htm.algorithms import TemporalMemory as TM
from perception.VisceralSDR_F1 import VisceralSDRF1


# variables
sparse_list = []

# instantiations
# Create the Spatial Pooler, and the SDR data structures needed to work with it.
inputSDR  = SDR( dimensions = (232,) )
activeSDR = SDR( dimensions = (2048,) )
tmInputSDR = SDR( dimensions = (2048,) )

# Instance SpatialPooler
sp = SP(inputDimensions    = inputSDR.dimensions,
        columnDimensions   = activeSDR.dimensions,
        localAreaDensity   = 0.02,
        globalInhibition   = True,
        seed               = 1,
        synPermActiveInc   = 0.01,
        synPermInactiveDec = 0.008)

# Create temporal memory
tm = TM(columnDimensions = activeSDR.dimensions,
        cellsPerColumn=1,
        initialPermanence=0.5,
        connectedPermanence=0.5,
        minThreshold=8,
        maxNewSynapseCount=20,
        permanenceIncrement=0.1,
        permanenceDecrement=0.0,
        activationThreshold=8,
        )

# functions
def encode_spatial(adenosine: float, glucose: float) -> list[int]:
        """ Encode spatial
            Compute biochemical parameters to produce
            SDR iteration before temporal memory
        """
        sdr_visceral_sdrf1 = VisceralSDRF1(adenosine_value=adenosine, glucose_value=glucose)
        inputSDR.sparse = sdr_visceral_sdrf1
        sp.compute(inputSDR, True, activeSDR)
        active_sdr_clean_list = activeSDR.sparse
        return active_sdr_clean_list.tolist()

def encode_memory(adenosine: float, glucose: float) -> dict:
        """
        Compute the spatial encoding to learn contextual and sequential patterns.
        """
        tmInputSDR.sparse = encode_spatial(adenosine=adenosine, glucose=glucose)
        tm.compute(tmInputSDR, learn=True)
        return {
                "active_columns": tm.getActiveCells().sparse.tolist(),
                "anomaly": tm.anomaly,
                "tm": tm,
        }
