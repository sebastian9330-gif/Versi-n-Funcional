# 🐢 mini-turtle-oo: Paquete Python Orientado a Objetos (POO)

Este repositorio contiene la implementación de un pequeño paquete Python (`mini_turtle_oo`) diseñado para simular una "tortuga" de dibujo básica en la terminal, refactorizando el diseño desde un enfoque funcional a un enfoque **Orientado a Objetos (POO)**.

El objetivo principal es demostrar los principios de **Encapsulamiento** e **Independencia** a través de la **Clase `Turtle`**.

### 🌟 Requisitos Funcionales Implementados

* **Clase Central:** Toda la lógica del dibujo reside en `class Turtle`.
* **Encapsulamiento:** El estado del dibujo (posición `x`, `y`, y el `canvas`) está contenido dentro de **atributos de instancia** (ej. `self.posicion_x`), eliminando la necesidad de variables globales.
* **Independencia:** Se pueden crear múltiples objetos `Turtle` (`t1`, `t2`, etc.) que mantienen su propio estado y dibujo de forma totalmente independiente.

---

## 📦 Estructura del Proyecto

El paquete sigue una estructura estándar para módulos de Python con foco en el diseño POO:

```text
mini_turtle_oo_task/
├── mini_turtle_oo/             <-- Carpeta del Paquete
│   ├── __init__.py             <-- Interfaz (Exporta la Clase Turtle)
│   └── turtle_class.py         <-- Lógica (Define la Clase Turtle)
├── main.py                     <-- Script de prueba con OBJETOS




