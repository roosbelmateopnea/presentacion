import random
Empatadas = []
Ganadas = []
Perdidas = []
print("Bienvenodo Al Juego Piedra,Papel y Tijera")
i = 1
rondas = int(input("Ingrese Por Favor Numero de Rondas a Jugar:"))
while True:
    Pregunta = input("Quieres jugar Esta Ronda Si/No?").lower()
    if Pregunta == "no":
        print("Juego Terminado")
        break
    elif Pregunta == "si":
        print(f"RONDA {i} DE {rondas}")
        Maquina = random.choice(["tijera","papel","piedra"])
        Jugar = input("Ingrese Por Favor las Opciones de Juego piedra,papel o tijera:")
        if Jugar == Maquina:
            print("Jugador/ar:",Jugar)
            print("Computadora:",Maquina)
            print("Empate Entre Jugador/ar y Computadora")
            Empatadas.append(1)
            print(f"Puntaje Parcial:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")
        elif Jugar == "tijera" and Maquina == "papel":
            print("Jugador/ar:",Jugar)
            print("Computadora:",Maquina)
            print("Jugador/ar ha ganado esta Ronda")
            Ganadas.append(1)
            print(f"Puntaje Parcial:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")
        elif Jugar == "tijera" and Maquina == "piedra":
            print("Jugador/ar:",Jugar)
            print("Computadora:",Maquina)
            print("Computadora ha ganado esta Ronda")
            Perdidas.append(1)
            print(f"Puntaje Parcial:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")
        elif Jugar == "papel" and Maquina == "tijera":
            print("Jugador/ar:",Jugar)
            print("Computadora:",Maquina)
            print("Computadora ha ganado esta Ronda")
            Perdidas.append(1)
            print(f"Puntaje Parcial:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")
        elif Jugar == "papel" and Maquina == "piedra":
            print("Jugador/ar:",Jugar)
            print("Computadora:",Maquina)
            print("Jugador/ar ha ganado esta Ronda")
            Ganadas.append(1)
            print(f"Puntaje Parcial:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")
        elif Jugar == "piedra" and Maquina == "papel":
            print("Jugador/ar:",Jugar)
            print("Computadora:",Maquina)
            print("Computadora ha ganado esta Ronda")
            Perdidas.append(1)
            print(f"Puntaje Parcial:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")
        elif Jugar == "piedra" and Maquina == "tijera":
            print("Jugador/ar:",Jugar)
            print("Computadora:",Maquina)
            print("Jugador/ar ha ganado esta Ronda")
            Ganadas.append(1)
            print(f"Puntaje Parcial:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")
        i += 1
print(f"Puntaje Final:-{sum(Ganadas)}(Jugador/ar)-{sum(Perdidas)}(Computadora)-{sum(Empatadas)}(Empates)")