# main.py
from mini_turtle_oo import Turtle

print("--- Ejercicio 2: Prueba Orientada a Objetos (POO) ---")

# Requisito: Crear dos objetos independientes
t1 = Turtle()
t2 = Turtle()

# ----------------------------------------
# 1. Dibujo de la Tortuga 1 (Escalera)
# ----------------------------------------
print("\nDibujando con Tortuga 1")
t1.adelante(10)
t1.abajo(2)
t1.adelante(8)
t1.abajo(2)

# ----------------------------------------
# 2. Dibujo de la Tortuga 2 (Forma corta)
# ----------------------------------------
# T2 es independiente de T1 y comienza en (0, 0)
print("\nDibujando con Tortuga 2")
t2.adelante(3)
t2.abajo(1)
t2.adelante(3)

# Mostrar resultados
print("\n--- Resultados Individuales ---")
t1.resultado()
t2.resultado()

# ----------------------------------------
# 3. Prueba de Reinicio e Independencia
# ----------------------------------------
print("\n--- PRUEBA DE INDEPENDENCIA: Reinicio solo T1 ---")

# Reiniciar solo la posición X de T1 (no afecta a T2)
t1.reiniciar()

# T1 dibuja desde X=0
t1.adelante(5)
t1.resultado() 

# T2 dibuja desde donde se quedó
print("\nComprobando que T2 no fue afectada...")
t2.adelante(5)
t2.resultado()