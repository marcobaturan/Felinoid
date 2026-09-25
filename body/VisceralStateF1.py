# importamos los módulos propios y creados de las dataclases de glucosa y adenosina.
from dataclasses import dataclass
import time
from adenosine import AdenosineState
from glucose import GlucoseState
from perception.VisceralSDR_F1 import VisceralSDRF1


# I define a mutable dataclass for the visceral state (initially two parameters)
@dataclass()
class VisceralStateF1:
    adenosine: AdenosineState
    glucose: GlucoseState

# We instantiate the dataclass with parameterization of the adenosine and glucose states started at their starting values
visceral_state = VisceralStateF1(adenosine=AdenosineState(level=0.0), glucose= GlucoseState(level=1.0))

class ChangeVisceralState:
    """Change Visceral State

        EIt is the class at instances to iterate over time to produce a change in the visceral states which will be
        the internal stimuli of the organism to condition the brain of the organism and produce internal
        and somatic states.
    """
    def __init__(self):
        self.actual_glucose_state = visceral_state.glucose
        self.actual_adenosine_state = visceral_state.adenosine

    def glucose_change(self):
        # glucose decay mechanism in the dimension of time according to an internal clock
        if self.actual_glucose_state.level > 0.0:
            new_level_glucose = round(self.actual_glucose_state.level - 0.1, 1)
            self.actual_glucose_state.level = new_level_glucose

            print(f"Glucose level: {self.actual_glucose_state.level}")

        if self.actual_glucose_state.level == 0.0:
            print("Food")

    def adenosine_change(self):
        # adenosine decay mechanism in the dimension of time according to an internal clock

        if self.actual_adenosine_state.level < 1.0:
            new_level_adenosine = round(self.actual_adenosine_state.level + 0.1, 1)
            self.actual_adenosine_state.level = new_level_adenosine

            print(f"Adenosine level: {self.actual_adenosine_state.level}")

        if self.actual_adenosine_state.level == 1.0:
            print("REM")


change_visceral_state = ChangeVisceralState()

if __name__ == '__main__':
    try:
        while True: # As long as a keyboard output command is not invoked, the same instance induces a change in

            change_visceral_state.glucose_change()
            change_visceral_state.adenosine_change()
            sdr = VisceralSDRF1(glucose_value = change_visceral_state.actual_glucose_state.level, adenosine_value=change_visceral_state.actual_adenosine_state.level)
            print("Visceral SDR state: ", sdr)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n Simulation stopped.")
