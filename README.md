# VLSM Subnetting Calculator & IP Planner (Python + GUI)

Una aplicación de escritorio de alto rendimiento desarrollada en **Python** diseñada para automatizar el cálculo, enmascaramiento y la planificación de direccionamiento IPv4 mediante el algoritmo **VLSM (Variable Length Subnet Mask)**. El sistema integra un motor matemático optimizado para operaciones de red acoplado a una interfaz gráfica de usuario (GUI) limpia e interactiva construida con **Tkinter**.

---

## Características Principales

* **Algoritmo de Segmentación Eficiente:** Clasifica automáticamente las solicitudes de hosts de mayor a menor para asignar los bloques CIDR estrictamente necesarios, reduciendo el desperdicio de direcciones IP a cero.
* **Cálculo Métrico Completo:** Genera instantáneamente mapas de red detallados que incluyen la dirección de red base, máscara de subred, prefijo CIDR, rango de hosts útiles (primer y último host) y dirección de Broadcast.
* **Interfaz Gráfica con Tkinter:** Interfaz interactiva que abstrae la complejidad de la lógica binaria mediante formularios de captura validados en tiempo real y visualización de resultados tabulados.
* **Procesamiento Síncrono Local:** Ejecución veloz de operaciones de enmascaramiento de red sin demoras en la capa de presentación.

---

## Stack Tecnológico

* **Lenguaje Core:** Python 3.x
* **Interfaz de Usuario:** Tkinter (GUI Nativa)
* **Dominio Lógico:** Operaciones de red e Ingeniería de Infraestructura IPv4

---

## Estructura del Proyecto

El código fuente separa limpiamente la lógica algorítmica de la renderización visual:

```text
VLSM/
├── VLSM.py           # Motor algorítmico central y procesamiento matemático de red
└── Interfaz.py       # Capa de presentación, formularios y componentes visuales
