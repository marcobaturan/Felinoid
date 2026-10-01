from dataclasses import dataclass
from datatypes.adenosine import AdenosineState
from datatypes.glucose import GlucoseState

# I define a mutable dataclass for the visceral state (initially two parameters)
@dataclass()
class VisceralStateF1:
    adenosine: AdenosineState
    glucose: GlucoseState
