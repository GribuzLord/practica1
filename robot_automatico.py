#Sin preguntarle al usuario moverse en automatico
import random
import matplotlib.pyplot as plt

mov=["Izquierda","Derecha"]
mapa=[[1,0,0,0,1,0,0,0],
     [1,1,1,0,1,0,1,0],
     [0,0,1,1,1,0,1,0],
     [0,0,1,0,1,1,1,1],
     [1,1,1,0,0,0,0,1],
     [0,0,1,0,0,0,0,1],
     [0,0,1,1,1,1,1,1]]

x=5
y=3
plt.scatter(x,y)
while True:
    
    
    print("Ingrese a donde quiere dirigirse:")
    print("1:Arriba")
    print("2:Izquierda")
    print("3:Derecha")
    respuesta=["1","2","3"]
    
    res=0;
    print(res)
    print(respuesta[res])
    print(respuesta[res])
    
    if y-1 >= 0 and mapa[y-1][x] == 1 and respuesta[res] == "1":
            y -= 1
    else:
        res=random.randint(1,2)
        print("Aqui:", res)
    if respuesta[res] == "2" and x-1 >= 0 and mapa[y][x-1] == 1:
        x -= 1
    elif respuesta[res] == "3" and x+1 < len(mapa[0]) and mapa[y][x+1] == 1:
        x += 1
    else:
        print("En esa dirección no se puede ir")
        
    print("Posición actual:", x, y)
    plt.imshow(mapa,cmap="grey")
    plt.show()
    plt.scatter(x,y)