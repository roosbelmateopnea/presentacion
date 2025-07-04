invitados = []
i = 1
while True:
    confirmacion = input("Deseas Invitar personas al Banquete Si/No:").lower()
    if confirmacion == "si":
        pregunta = input(f"Ingresa Nombre invitado #{i} al Banquete:")
        invitados.append(pregunta)
        i += 1
    elif confirmacion == "no":
        print("Los invitados al Banquete de Amigos son:",invitados)
        break
    else:
        print("Error Dato Ingresado Incorrecto ingrese Si/No")
    