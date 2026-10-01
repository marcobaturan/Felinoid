from dataclasses import dataclass
from body.adenosine import AdenosineState
from body.glucose import GlucoseState

# I define a mutable dataclass for the visceral state (initially two parameters)
@dataclass()
class VisceralStateF1:
    adenosine: AdenosineState
    glucose: GlucoseState
