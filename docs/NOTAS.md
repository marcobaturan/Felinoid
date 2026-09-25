# NOTAS.md - Criterios de Diseño para Codificación SDR (Proyecto FELYNOYD)

## Fórmula de cálculo de `n` (tamaño total del vector SDR)

```
n = w + buckets - 1
```

Donde:
- `w` = número de bits activos (ancho del cubo). Valor de partida estándar en la comunidad HTM: **21-25 bits**, independiente del dominio de la variable.
- `buckets` = número de valores/estados discretos y discriminables que necesita distinguir el sistema de control para esa variable.
- `n` = tamaño total del espacio de representación binaria.

## Criterio para decidir `buckets`

**No existe una referencia biológica objetiva que determine este número.** Es una decisión de ingeniería, no un dato medible en el organismo real. La pregunta correcta para derivarlo:

> ¿En cuántos estados discretos y reconocibles debe traducirse esta variable para que el comportamiento resultante del sistema sea creíble/funcional?

Pasos:
1. Identificar los estados fenomenológicos o funcionales más claros del fenómeno (p. ej. para hambre: saciado, normal, hambriento, crítico).
2. Confirmar que cada estado es semánticamente distinto (evitar sinónimos que infractan el conteo real).
3. Justificar el número por escrito, ligado a la necesidad de la máquina de estados/comportamiento, no al valor usado en otra variable.
4. Aplicar la fórmula con ese número de buckets.

## Criterio para decidir `Periodicidad`

Periodicidad = `True` únicamente si el valor máximo y el valor mínimo del rango son **contiguos en el espacio de representación** (ej. 23:59 y 00:00 de un reloj, o 359° y 0° de un ángulo).

Errores a evitar (detectados durante el diseño):
- Confundir "el fenómeno real tiene un componente cíclico en el organismo" con "esta variable debe codificarse como periódica". Son cosas distintas: la variable puede subir y bajar varias veces al día (patrón polifásico) sin ser periódica en el sentido de HTM, siempre que no "envuelva" del máximo al mínimo como continuación directa.
- Una variable que decae monótonamente y se resetea por un evento externo (ej. comer, dormir) **no es periódica**: es discreta por tramos, no cíclica.

## Criterio para decidir `n` cuando hay variables agregadas (vector concatenado)

Si varias variables se combinan en un solo SDR de salida (ej. `VisceralSDRF1` con glucosa + adenosina), `dimensions` debe reflejar la **suma** de los `n` individuales, no un valor arbitrario copiado de otra parte del documento. Verificar siempre que el tamaño declarado en la interfaz de salida coincida aritméticamente con la suma de los encoders que la alimentan.

## Errores propios detectados durante este ejercicio (registro para no repetir)

- Replicar `w`/`n` de una variable a otra sin derivarlos del problema (arrastre acrítico de un valor visto antes).
- Declarar un `dimensions` en la dataclase de salida que no coincide con el `n` calculado en la especificación del encoder.
- Mezclar en una sola variable dos fenómenos distintos (cantidad acumulada vs. fase cualitativa cíclica), lo que produce un encoder mal definido para ninguno de los dos.
- Confundir "el sistema real tiene una guía externa como el reloj" con "el agente debe recibir esa guía como variable de entrada" — un agente no sentiente debe modelarse por eventos y condicionamiento interno, no por acceso a información que no podría percibir biológicamente.

## ENTRADAS 

### 2026 09 12

- Escojo que 'Food' es continuo porque actúa de alarma en el sistema y por llamada continua lo satura, 
  forzando a que el organismo priorice cubrir una necesidad por supervivencia. Llena su espacio de procesos con la alarma 
  y así el cuerpo influye en el cerebro. Uso Ctrl+C porque está en el sistema Linux, mientras que otras opciones implican 
  o código complicado o instalar librerías que aumenten el peso del proyecto. Corregí el código. 
  Y además lo puse en body/glucose.py.

- Y adenosina al llegar a 1.0 emite REM de forma continua, porque es otra llamada de necesidad vital, satura 
  el sistema para priorizarse.

### 2026 09 17

- Selecciono hacer las clases de datos mutables y refactorizar las dos funciones de cambio de glucosa y adenosina dentro 
- módulo de cambio de estado visceral para así mantener el código limpio, claro y simple. De paso está integrado y
- optimizado. Documento el código. Me queda pendiente leer sobre ScalarEncoder de htm.core para saber como funciona y
- explicarselo a CW. 
- PERSONAL: como este es un proyecto personal, puede que encuantres pensamiento mios al respecto. Siento cansancio, tristeza
- pero a la vez orgullo. Hago algo que me gusta y que me fuerza a mejorar porque aprendo y practico. Pero me siento
- triste por lo tarde que es y que la influencia de vibe coding me ha atrofiado mucho mis habilidades. Y eso duele.

### 2026 09 18

- Aprendo que es dataclass, encoder, SDR, SpatialPool, TimeMemory en HTM y su ciclo base.
- Basandome en la formula n = w + bucket - 1 y a esta descripción evidenciada:

* Mechanical Detection Threshold (MDT): The minimum force required for the nervous system to register a light touch or stroke.
* Pressure Perception Threshold (PPT): The point where light touch transitions into a clearly felt blunt force or weight affecting deeper tissues.
* Mechanical Pain Threshold (MPT) / Mechanical Nociceptive Threshold (MNT): The exact transition where pressure changes from a neutral sensation into sharp, localized pain or an immediate reflex withdrawal.
* Pressure Pain Tolerance (PPTol): The maximum amount of painful pressure a subject can endure before actively escaping or stopping the stimulus.

- n = 21 + 4 -1 = 24

Bien. Con el contrato confirmado, la implementación aislada de Fase 2 es directa: un ScalarEncoder(w=21, n=25, minimum=0.0, maximum=1.0, periodic=False) (o los nombres de parámetro exactos que hayas visto en la documentación — verifícalos tú, no asumas que coinciden con lo que escribo aquí) que reciba back_pressure y devuelva un SDR.

Escribe el script (algo del estilo perception/tactile_encoder.py, ya que corresponde a esa capa según tu estructura de carpetas) que:

Instancie el encoder con los parámetros del contrato.
Codifique 2-3 valores de prueba de back_pressure (p. ej. 0.0, 0.5, 1.0).
Imprima por consola los índices de bits activos de cada uno, para verificar visualmente que: (a) son exactamente 21 bits, (b) los índices caben dentro de 0-24, (c) valores cercanos (p. ej. 0.5 y 0.6) producen SDRs con solapamiento alto, y valores lejanos (0.0 y 1.0) con solapamiento bajo o nulo.

Decisión razonable — la justificación (percepción táctil fina) es coherente con la naturaleza de la variable, y con `n=50` el trade-off de generalización que señalé (43% en el par más próximo) sigue siendo aceptable.

---

## Resumen de sesión — 19 de septiembre de 2026 — Proyecto Felinoid

**Alcance:** Fase 1 (cuerpo simbólico) cerrada; Fase 2 (percepción táctil, `back_pressure`) cerrada.

### Fase 1 — Unificación del cuerpo simbólico
- `VisceralStateF1.py` unifica `glucose.py` y `adenosine.py` mediante composición de dataclasses (`VisceralStateF1` contiene `GlucoseState` y `AdenosineState`) en un único bucle de tick de 100ms.
- Decisión de diseño: mutabilidad directa de atributos en vez de inmutabilidad estricta (`frozen=True`), por simplicidad y legibilidad en fase PoC — contrato actualizado para reflejar esta elección.
- Eventos "Food" (glucosa a 0.0) y "REM" (adenosina a 1.0) implementados como señales continuas que saturan el sistema, justificados fenomenológicamente como mecanismo de prioridad por supervivencia, coherente con el principio de diseño "el cuerpo influye la mente".
- Módulos `glucose.py`/`adenosine.py` reducidos a solo sus dataclasses de estado, sin lógica ni bloque `main`, para mantener el código limpio.

### Fase 2 — Codificación sensorial (tacto)
- Estudiada la API de `ScalarEncoder` de `htm.core` antes de implementar.
- Parámetro `buckets` para `back_pressure` investigado con fuente clínica veterinaria (escala UNESP-Botucatu / Escala Descriptiva Simple, 4 niveles de dolor/reacción táctil), verificada en fuente primaria tras alerta sobre citar un LLM como fuente sin comprobar.
- Distinguido correctamente: la escala clínica categórica no determina directamente el parámetro técnico `buckets` del encoder — son dos capas de abstracción distintas.
- Construida herramienta reutilizable de medición de solapamiento entre SDRs (`utils/overlap_utils.py` + `utils/inform_tool.py`), agnóstica de `htm.core`, con lógica generalizada de "pares consecutivos + extremos" sobre listas de SDRs de longitud arbitraria.
- Experimento con 4 configuraciones de `n` (24, 30, 40, 50) sobre 4 puntos de prueba (0.0, 0.2, 0.6, 1.0): solapamiento en extremos bajó de 86% (n=24) a 0% (n=50), confirmando el trade-off entre discriminación y generalización.
- **Decisión final: `w=21, n=50`**, priorizando discriminación fina por la naturaleza sensible de la percepción táctil.

### Deuda técnica / pendientes explícitos
- Ninguna otra variable (glucosa, adenosina) tiene todavía su propio `ScalarEncoder` — solo `back_pressure` está resuelto en Fase 2.
- Siguiente paso lógico: aplicar el mismo proceso de derivación empírica de `buckets`/`n` a `blood_glucose` y `accumulated_adenosine`, que actualmente siguen con el valor `n=25` fijado antes de tener esta metodología de medición de solapamiento — revisar si se sostiene con el mismo rigor ahora disponible.

## Resumen de sesión - 24 de septiembre de 2026

### Deuda técnica
- Se completa el codificador de escala para azucar y adenosina, se actualiza el contrato de interface fase 1, se ponen las razones y hechos.
- Se ajusta los buckes de adenosine a granularidad fina y distribución amplia.
- Nota deuna conversación de peloteo: Working in Felinoid make me strong conscious about a big problem about the arc percepción-conception. E.g: Now I'm working in connect glucose levels sensor, from 0.0 to 1.0 with five label for levels, to encoder to produce proper SDR. I will use my tool for measuring of overlap memory patterns between layers of HTM column. Meanwhile touch is a continuous perception with high discrimination the levels of sugar/hunger is different; because one can have relative middle to low suggar and ignore the pain in the stomach. And all animal not only eat when they have hunger for very low sugar, they need a trigger (sound of bottle, for example) in humans is smell, or watch a big letter of McDonald's. but in this phase it's only a chemical sensor connected to encoder to produce SDR in HTM.

## Resumen de sesión - 25 de septiembre de 2026

### Almaceno en NOTAS.md de ejemplo de test de SDR

Este tipo de estructura permite analizar la codificación de los valores provenientes de los sensores a los codificadores
que lo convierten en representaciones distribuidas escasas para detectar el solapamiento entre patrones de activación
entre instancias de tiempo para que haya continuidad semantica y aprendizaje de percepciones.
  
```Python
# Import a library after read docs
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters
from utils.inform_tool import overlap_inform

# variables
null_glucose = 0.0
max_glucose = 1.0
w = 21


if __name__ == '__main__':
    params = ScalarEncoderParameters()
    params.minimum = null_glucose     # minimum glucose
    params.maximum = max_glucose      # maximum glucose
    params.activeBits = w             # with of window activation bits
    numbers = [100,105,110,112]       # 112 ES EL GANADOR EN CUANTO A SOLAPAMIENTO DE CODIFICADORES DE GLUCOSA.

    for number in numbers:
        params.size = number

        # start encoder with params
        encoder = ScalarEncoder(params)
        # encode 4 values of back pressure point
        sdr_one = encoder.encode(0.0)    # critic
        sdr_two = encoder.encode(0.2)    # strong hunger
        sdr_three = encoder.encode(0.4)  # soft hunger
        sdr_four = encoder.encode(0.6)   # normal
        sdr_five = encoder.encode(0.8)   # near full
        sdr_six  = encoder.encode(1.0)   # full


        # print the internal representation
        print("=====================================================================")
        print(f"for size of {number} bits.")
        print("Position for value 0.0: ", sdr_one.sparse)
        print("Position for value 0.2: ", sdr_two.sparse)
        print("Position for value 0.4: ", sdr_three.sparse)
        print("Position for value 0.6: ", sdr_four.sparse)
        print("Position for value 0.8: ", sdr_five.sparse)
        print("Position for value 1.0: ", sdr_six.sparse)
        print("=====================================================================")
        one = sdr_one.sparse.tolist()
        two = sdr_two.sparse.tolist()
        three = sdr_three.sparse.tolist()
        four = sdr_four.sparse.tolist()
        five = sdr_five.sparse.tolist()
        six = sdr_six.sparse.tolist()


        overlap_inform(one, two, three, four, five,six, w=w)
        print("=====================================================================")

```

