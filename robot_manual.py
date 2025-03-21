#Realizar un programa que implemente un agente tipo reflex 
#Se tendra un solo sensor que haga un robot pueda dtecetar
#si hay o no un objeto (el cual sera introducido por el usuario)
#Sera un programa infinito
#Si no hay un objeto avanzaremos hacia adelante(Se imprime: avanzando hacia adlenate)
#Si no hya un objeto el robot el robot se debe mover de forma aleatoria
# a la izquierda o a la derecha

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
    print(mapa)
    plt.imshow(mapa,cmap="grey")
    plt.show()
    plt.scatter(x,y)
    print("Hay algun objeto que bloquee el movimiento? (Si/no)")
    entrada=input() #Regresa una variable tipo string
    if(entrada == "Si" or entrada=="si"):
        
        movimientos=random.randint(0,1)
        print(f"Avanzando hacia: {mov[movimientos]}")
        
        if movimientos==0 and x-1 >= 0 and mapa[y][x-1] == 1:
            x=x-1
        elif movimientos==1 and x-1 >= 0 and mapa[y][x+1] == 1:
            x=x+1
    elif y-1 >= 0 and mapa[y-1][x] == 1:
        print("Avanzando hacia adelante")
        y=y-1
    else:
        print("Por ahi no pa")
    print(x,y)