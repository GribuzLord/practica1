#BFS significa Búsqueda en Anchura (Breadth-First Search), básicamente lo que hace es:

#Empieza en un punto inicial.
#Explora todas las posibles direcciones (arriba, abajo, izquierda, derecha).
#Va guardando las coordenadas en una cola (queue).
#Si llega a la meta, se detiene.
#Si se topa con un cero (pared), no avanza.

import matplotlib.pyplot as plt
import random
from collections import deque

# Laberinto
mapa = [[1, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0]]

# Punto de inicio
inicio = (3, 5)  # y, x
meta = (0, 4)  # Aquí ponemos la salida

# Movimientos posibles (Arriba, Abajo, Izquierda, Derecha)
movimientos = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # (y, x)
nombres = ["Izquierda", "Derecha", "Arriba", "Abajo"]

def bfs(inicio, meta):
    cola = deque()
    cola.append((inicio, []))
    visitados = set()
    
    while cola:
        (y, x), camino = cola.popleft()
        
        if (y, x) == meta:
            print("¡Llegamos a la meta! 🏁🔥")
            return camino
        
        if (y, x) in visitados:
            continue
        
        visitados.add((y, x))
        
        for i, (dy, dx) in enumerate(movimientos):
            nuevo_y, nuevo_x = y + dy, x + dx
            
            if 0 <= nuevo_y < len(mapa) and 0 <= nuevo_x < len(mapa[0]) and mapa[nuevo_y][nuevo_x] == 1:
                cola.append(((nuevo_y, nuevo_x), camino + [nombres[i]]))
    
    print("No hay salida 😭")
    return []

# Dibujar mapa
plt.imshow(mapa, cmap="gray")
plt.scatter(inicio[1], inicio[0], color="blue", label="Inicio")
plt.scatter(meta[1], meta[0], color="green", label="Meta")
plt.legend()

# Resolver
camino = bfs(inicio, meta)
if camino:
    print("Camino recorrido:", camino)
plt.show()

