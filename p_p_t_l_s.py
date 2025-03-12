import random



def pptls():
    print("Elige una opción: piedra, papel, tijera, lagarto, spock")
    jugador = input("Tu elección: ").lower()

    if jugador != "piedra" and jugador != "papel" and jugador != "tijera" and jugador != "lagarto" and jugador != "spock":
        print("Opción inválida. Intenta de nuevo.")
        pptls()
    else:

        opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
        computadora = opciones[random.randint(0, 4)]

        print(f"Tú elegiste: {jugador}")
        print(f"La computadora eligió: {computadora}")

        if jugador == computadora:
            print("¡Es un empate!")
        elif jugador == "piedra":
            if computadora == "tijera":
                print("¡Ganaste! Tijera ha sido aplastada por Piedra!")
            elif computadora == "lagarto":
                print("¡Ganaste! Lagarto ha sido aplastado por Piedra!")
            else:
                print("¡Perdiste!")
        elif jugador == "papel":
            if computadora == "piedra":
                print("¡Ganaste! Piedra ha sido envuelta por Papel!")
            elif computadora == "spock":
                print("¡Ganaste! Spock ha sido desautorizado por Papel!")
            else:
                print("¡Perdiste!")
        elif jugador == "tijera":
            if computadora == "papel":
                print("¡Ganaste! Papel ha sido cortado por Tijera!")
            elif computadora == "lagarto":
                print("¡Ganaste! Lagarto ha sido decapitado por Tijera!")
            else:
                print("¡Perdiste!")
        elif jugador == "lagarto":
            if computadora == "papel":
                print("¡Ganaste! Papel ha sido comido por Lagarto!")
            elif computadora == "spock":
                print("¡Ganaste! Spock ha sido envenenado por Lagarto!")
            else:
                print("¡Perdiste!")
        elif jugador == "spock":
            if computadora == "tijera":
                print("¡Ganaste! Tijera ha sido vaporizada por Spock!")
            elif computadora == "piedra":
                print("¡Ganaste! Piedra ha sido desintegrada por Spock!")
            else:
                print("¡Perdiste!")

pptls()
