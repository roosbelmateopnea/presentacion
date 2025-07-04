import random
Ganadas = []
Perdidas = []
Empate = []
nombre = input("Ingrese Por Favor Tu nombre:")
print(f"Bienvenido/a '{nombre}' al Juego de la Banca Mucha Suerte en estas Rondas")
while True:
    Jugar = input("Deseas Jugar una Ronda:").lower()
    if Jugar == "no" or sum(Ganadas) == 5 or sum(Perdidas) == 3:
        print("Juego Terminado")
        break
    
    elif Jugar == "si":
        computadora = random.randint(1,13)
        ingreso = int(input("Ingrese Por Favor Un Numero de 1 Al 13:"))
        if ingreso == computadora:
            print("Computadora Eligio:",computadora)
            print("Jugador Eligio:",ingreso)
            print("Empate en Esta Ronda")
            Empate.append(1)

        elif ingreso > computadora:
            print("Computadora Eligio:",computadora)
            print("Jugador Eligio:",ingreso)
            print("Gana en Esta Ronda")
            Ganadas.append(1)
    
        elif ingreso < computadora:
            print("Computadora Eligio:",computadora)
            print("Jugador Eligio:",ingreso)
            print("Pierde en Esta Ronda")
            Perdidas.append(1)
        
print("Computadora Eligio:",computadora)
print("Rondas Ganadas",sum(Ganadas))
print("Rondas Empatadas",sum(Empate))
print("Rondas Perdidas",sum(Perdidas))