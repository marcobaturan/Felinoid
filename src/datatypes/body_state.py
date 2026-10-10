from dataclasses import dataclass
from src.datatypes.adenosine import AdenosineState
from src.datatypes.glucose import GlucoseState

# I define a mutable dataclass for the visceral state (initially two parameters)
@dataclass()
class VisceralStateF1:
    adenosine: AdenosineState
    glucose: GlucoseState

# Exteroceptor
# Interoceptor
# proprioception
__doc__="""Los sistemas sensoriales se clasifican categóricamente en tres grandes grupos según la procedencia del estímulo. Cada grupo contiene diferentes sentidos y subsentidos (los tipos específicos de energía o cambio que detectan).
Aquí tienes la organización taxonómica completa, incluyendo sus términos en inglés:
## 1. Exterocepción (Exteroception)
Detecta estímulos que provienen del exterior del cuerpo.

* Sentidos clásicos (Distales):
* Visión (Vision / Sight): Subsentidos de color, brillo y movimiento.
   * Audición (Hearing / Audition): Subsentidos de tono y volumen.
   * Olfato (Smell / Olfaction): Detección de moléculas químicas volátiles.
* Sentidos de contacto:
* Gusto (Taste / Gustation): Subsentidos dulce, salado, ácido, amargo y umami.
   * Sistema somatosensorial (Tacto) (Touch / Somatosensation): Se divide en subsentidos específicos:
   * Mecanorrecepción (Mechanoreception): Presión, vibración y textura.
      * Termorrecepción (Thermoreception): Calor y frío externo.
      * Nocicepción externa (Nociception): Dolor superficial o cutáneo.
   
## 2. Propiocepción (Proprioception)
Monitorea la posición, movimiento y equilibrio de las partes del propio cuerpo.

* Sistema vestibular (Vestibular sense): Ubicado en el oído interno; detecta el equilibrio, la aceleración y la orientación de la cabeza en el espacio.
* Sistema kinestésico (Kinesthesia): Receptores en músculos, tendones y articulaciones (como los muscle spindles o husos musculares); detectan el esfuerzo, la tensión, el estiramiento y la posición de las extremidades.

## 3. Interocepción / Viscerocepción (Interoception)
Monitorea el estado interno de los órganos y los fluidos corporales para mantener la homeostasis.

* Quimiorrecepción interna (Chemoreception): Niveles de oxígeno, dióxido de carbono (CO₂) y pH en la sangre.
* Barorrecepción (Baroreception): Presión arterial.
* Osmorrecepción (Osmoreception): Concentración de agua y solutos (sed).
* Nocicepción visceral (Visceral nociception): Dolor de órganos internos (como un dolor de estómago).
* Termorrecepción central (Central thermoreception): Temperatura interna detectada por el hipotálamo.

------------------------------

"""