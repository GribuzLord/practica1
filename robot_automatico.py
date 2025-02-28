#Sin preguntarle al usuario moverse en automatico
import random
import matplotlib.pyplot as plt

mov=["Izquierda","Derecha"]
mapa=[[1,0,0,0,1,0,0],
     [1,1,1,0,1,0,1],
     [0,0,1,1,1,0,1],
     [0,0,1,0,1,1,1],
     [1,1,1,0,0,0,0]]

x=5
y=3
plt.scatter(x,y)

while True:
    
    
    print("Ingrese a donde quiere dirigirse:")
    print("1:Arriba")
    print("2:Abajo")
    print("3:Izquierda")
    print("4:Derecha")
    respuesta=["1","2","3","4"]
    res=random.randint(0,3)
    print(respuesta[res])
    
    
    if respuesta[res] == "1" and y-1 >= 0 and mapa[y-1][x] == 1:
        y -= 1
    elif respuesta[res] == "2" and y+1 < len(mapa) and mapa[y+1][x] == 1:
        y += 1
    elif respuesta[res] == "3" and x-1 >= 0 and mapa[y][x-1] == 1:
        x -= 1
    elif respuesta[res] == "4" and x+1 < len(mapa[0]) and mapa[y][x+1] == 1:
        x += 1
    else:
        print("En esa dirección no se puede ir")
        
    print("Posición actual:", x, y)
    plt.imshow(mapa,cmap="grey")
    plt.show()
    plt.scatter(x,y)