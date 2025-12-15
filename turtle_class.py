# mini_turtle_oo/turtle_class.py

class Turtle:
    """
    Clase Tortuga para dibujar en un canvas interno, aplicando POO.
    Cada objeto Turtle encapsula su propio estado (posicion_x, y, canvas).
    """
    # Constantes (pueden ser atributos de clase)
    ANCHO = 50
    ALTO = 30
    
    def __init__(self):
        """Inicializa los atributos de instancia."""
        # Requisito: usar self.posicion_x, inicializado en 0.
        self.posicion_x = 0  # Coordenada horizontal (x)
        self.y = 0           # Coordenada vertical (y)
        
        # Cada instancia tiene su propio canvas para garantizar la Independencia
        self.canvas = [[" " for _ in range(self.ANCHO)] for _ in range(self.ALTO)]
        print(f"Tortuga {id(self)} creada en posición (x, y): ({self.posicion_x}, {self.y})")

    def adelante(self, pasos):
        """Mueve la tortuga horizontalmente y dibuja una línea."""
        
        # Accede y modifica el estado usando self.
        pasos_reales = min(pasos, self.ANCHO - self.posicion_x - 1) 
        
        for i in range(pasos_reales):
            if self.y < self.ALTO and self.posicion_x < self.ANCHO:
                self.canvas[self.y][self.posicion_x] = "-"
            self.posicion_x += 1
        
        # Dibuja la flecha final
        if pasos_reales > 0 and self.y < self.ALTO and self.posicion_x < self.ANCHO:
            self.canvas[self.y][self.posicion_x] = ">"

    def abajo(self, pasos):
        """Mueve la tortuga verticalmente y dibuja una línea."""
        y_inicio = self.y
        
        for i in range(pasos):
            y_coordenada = y_inicio + i
            if y_coordenada < self.ALTO and self.posicion_x < self.ANCHO:
                self.canvas[y_coordenada][self.posicion_x] = "|" 
            
        # Actualiza la posición y
        self.y = y_inicio + pasos
        
        # Dibuja la flecha final 'v'
        if self.y < self.ALTO and self.posicion_x < self.ANCHO:
            self.canvas[self.y][self.posicion_x] = "v"

    def reiniciar(self):
        """Reinicia la posición horizontal (self.posicion_x) a 0."""
        self.posicion_x = 0
        print(f"--- Posición X de Tortuga {id(self)} reiniciada a 0 ---")

    def resultado(self):
        """Imprime el estado actual del canvas de esta tortuga."""
        print("\n" + "="*50)
        print(f"RESULTADO DEL OBJETO TURTLE ID: {id(self)}")
        print("="*50)
        for fila in self.canvas:
            print("".join(fila))
        print("="*50 + "\n")