# importamos los módulos propios y creados de las dataclases de glucosa y adenosina.
import time
from adenosine import AdenosineState
from datatypes.datatypes import VisceralStateF1
from glucose import GlucoseState
from memory.htm_pipeline import encode_memory
from utils.inform_tool import printStateTM


# We instantiate the dataclass with parameterization of the adenosine and glucose states started at their starting values
visceral_state = VisceralStateF1(adenosine=AdenosineState(level=0.0), glucose= GlucoseState(level=1.0))

class ChangeVisceralState:
    """Change Visceral State

        It is the class of instances to iterate over time to produce a change in the visceral states.
        Which will be the internal stimuli of the organism to condition the brain of the organism and produce internal
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
            response = encode_memory(adenosine=change_visceral_state.actual_adenosine_state.level,
                          glucose= change_visceral_state.actual_glucose_state.level)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n Simulation stopped.")
        print('active_columns', response['active_columns'])
        print('anomaly', response['anomaly'])
        print('Show tm state:')
        printStateTM(response['tm'])
