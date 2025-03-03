# **Hoja de Trabajo 2 - Inteligencia Artificial**

## Introducción
Esta hoja de trabajo consiste en el desarrollo de un agente básico que sea capaz de resolver un problema de decisión de Markov. En este caso se desarrolló en el entorno **Frozen Lake**.



## ¿Qué es el problema Frozen Lake?
El Frozen Lake es un entorno simulado que representa un lago congelado dividido en una cuadrícula. El objetivo es que un agente se mueva desde un punto inicial hasta un punto de meta sin caer en agujeros en el hielo.

Los elementos del entorno son:
1. Punto inicial (Start): Esquina superior izquierda de la cuadrícula.

2. Punto de meta (Goal): Esquina inferior derecha de la cuadrícula.

3. Hielo seguro (Frozen): Casillas por las que el agente puede moverse sin problemas.

4. Hoyos (Holes): Casillas que, si el agente cae en ellas, termina el episodio con una recompensa negativa.

5. Acciones: El agente puede moverse en 4 direcciones: arriba, abajo, izquierda o derecha.