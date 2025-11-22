# QFF25

# Crear entorno local:
``` bash
conda env create --solver libmamba --file ICC25.yml --name ICC25
conda init
conda activate ICC25
```
# Autores

- Aldana Lescano Maier
- Joaquín Hernández
- Leandro BAtlle

# Resolución

Ver [src/main.ipynb](https://github.com/eterX/QFF25/blob/extra-ruido/src/main.ipynb)

- resuelto: Objetivo principal, y *extras*: simuladores con ruido, visualizaciones avanzadas.

# Enunciado

## ⭐ Operación: Caja Fuerte Cuántica

En el laboratorio del FIUBA ocurrió un fallo inesperado: varias cajas fuertes cuánticas perdieron sus contraseñas. Ninguna se abre con métodos clásicos. Cada clave está escondida en una superposición de estados, y solo un algoritmo cuántico bien diseñado puede recuperarla.

La única pista que dejaron los ingenieros antes del apagón fue:

> ***"No busques la clave. Amplifica la correcta."***
> 

Tu equipo de cuatro personas deberá construir, desde cero, un **buscador cuántico basado en Grover** capaz de revelar la contraseña perdida utlizando *Qiskit*.

No se entregará ningún Colab inicial ni funciones prearmadas. Ustedes decidirán cómo representar el espacio de contraseñas, cómo marcar la solución y cómo amplificarla hasta poder medirla.

---

### 🎯 Objetivo principal

El desafío consiste en:

- Crear un **espacio de búsqueda** (bitstrings del tamaño que elijan).
- Implementar un **oráculo** que marque la contraseña correcta con un phase flip.
- Construir un **difusor** o amplificador tipo Grover.
- Ejecutar el algoritmo y **recuperar la contraseña** a partir de mediciones.
- Documentar todo en un **único Colab**, con explicaciones y visualizaciones claras.

---

### ⭐ Bonus: Puntos extra

Los equipos pueden sumar puntos por:

- Usar **otros algoritmos de búsqueda**, distintos o más generales que Grover como Generalized Amplitude Amplification, Quantum Walk Search, Amplitude Estimation, Variational Quantum Search o Grover Adaptative Search.
- Diseñar **oráculos complejos**, con múltiples soluciones o condiciones no triviales. Como también, proponer **generalizaciones**: patrones parciales, rangos, propiedades matemáticas, o búsquedas no estándar. ¡Ver cajas especiales!
- Ejecutar experimentos en **simuladores con ruido** y analizar sus efectos.
- Agregar **visualizaciones avanzadas** o herramientas interactivas.
- Comparar su solución cuántica con una búsqueda clásica equivalente.
- Implementar **mitigación de ruido** o variantes híbridas cuántico-clásicas.

Nada de esto es obligatorio, pero sí muy valorado.

---

### 🎒 Las cajas especiales perdidas

Además de la caja fuerte principal, el laboratorio dejó **cuatro cajas misteriosas**, cada una protegida por un oráculo más extraño que el anterior. No son obligatorias, pero quienes las resuelvan demostrarán verdadera maestría cuántica.

- **Caja de Atenea:** Acepta claves que cumplen varias propiedades combinadas. Un oráculo lógico y matemático.
    
    [**Caja de Atenea — Mini‑Desafio**](https://www.notion.so/Caja-de-Atenea-Mini-Desafio-2b34981ca2b980758603f9ebd51e1687?pvs=21)
    
- **Caja de Einstein:** Su "contraseña" es una *relación*, no un número. Requiere un oráculo que evalúe propiedades emergentes.
    
    [**Caja de Einstein — Mini‑Desafio**](https://www.notion.so/Caja-de-Einstein-Mini-Desafio-2b34981ca2b980f19f6cea6d4846a5c9?pvs=21)
    
- **Caja del Fantasma:** Reconoce patrones incompletos: marca familias de estados en lugar de uno solo.
    
    [Caja del Fantasma — Mini-Desafio](https://www.notion.so/Caja-del-Fantasma-Mini-Desafio-2b34981ca2b980aa9536d6dee7ac52d6?pvs=21)
    
- **Caja del Oráculo Roto:** Viene defectuosa y marca estados incorrectos; exige corrección, mitigación o rediseño inteligente.
    
    [Caja del Oraculo Roto](https://www.notion.so/Caja-del-Oraculo-Roto-2b34981ca2b980c3aa84e83b9c11efeb?pvs=21)
    

---

La contraseña está perdida en un mar de amplitudes.

La caja fuerte espera.

El circuito correcto la revelará.

---

### Qiskit Fall Fest FIUBA 2025 • Operación: Caja Fuerte Cuántica

Paseo Colón 850, CABA, Argentina • 22/11/2025

Más inforomación: [FIUBA Qiskit Fall Fest 2025 | IBM Quantum Computing Event](https://fiuba-qff-2025.vercel.app/)
