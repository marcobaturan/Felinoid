# importamos los módulos propios y creados de las dataclases de glucosa y adenosina.
from dataclasses import dataclass
import time
from adenosine import AdenosineState
from glucose import GlucoseState
from perception.VisceralSDR_F1 import VisceralSDRF1


# Defino una dataclase mutable para el estado visceral (inicialmente dos parámetros)
@dataclass()
class VisceralStateF1:
    adenosine: AdenosineState
    glucose: GlucoseState

# Instanciamos la dataclase con parametrizacion de los estados de adenosina y glucosa iniciados en sus valores de inicio
visceral_state = VisceralStateF1(adenosine=AdenosineState(level=0.0), glucose= GlucoseState(level=1.0))

class ChangeVisceralState:
    """Change Visceral State

        Es la clase a instancias para iterar en el tiempo para producir un cambio en los estados viscerales
        los cuales serán los estimulos internos del organismo para condicionar el cerebro del organismo y
        producir estados internos y somáticos.
    """
    def __init__(self):
        self.actual_glucose_state = visceral_state.glucose
        self.actual_adenosine_state = visceral_state.adenosine

    def glucose_change(self):
        # mecanismo de decaida de glucosa en la dimensión del tiempo según un reloj interno
        # Inicialmente en decima de segundo.
        # produce hambre
        if self.actual_glucose_state.level > 0.0:
            new_level_glucose = round(self.actual_glucose_state.level - 0.1, 1)
            self.actual_glucose_state.level = new_level_glucose

            print(f"Glucose level: {self.actual_glucose_state.level}")

        if self.actual_glucose_state.level == 0.0:
            print("Food")

    def adenosine_change(self):
        # mecanismo de subida de adenosina en la dimensión del tiempo según un reloj interno
        # Inicialmente en decima de segundo.
        # produce sueño
        if self.actual_adenosine_state.level < 1.0:
            new_level_adenosine = round(self.actual_adenosine_state.level + 0.1, 1)
            self.actual_adenosine_state.level = new_level_adenosine

            print(f"Adenosine level: {self.actual_adenosine_state.level}")

        if self.actual_adenosine_state.level == 1.0:
            print("REM")


# instancia del mecanismo de estado visceral en la dimensión del tiempo
change_visceral_state = ChangeVisceralState()

if __name__ == '__main__':
    try:
        while True: # Mientras no se invoque un comando de salida por teclado la misma instancia induce un cambio en
            # ambas variables.
            change_visceral_state.glucose_change()
            change_visceral_state.adenosine_change()
            sdr = VisceralSDRF1(glucose_value = change_visceral_state.actual_glucose_state.level, adenosine_value=change_visceral_state.actual_adenosine_state.level)
            print("Visceral SDR state: ", sdr)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n Simulation stopped.")
