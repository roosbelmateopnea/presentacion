import random
numero_secreto = random.randint(1,100)
condicion = True
i = 1
while condicion:
    ingreso = int(input("Ingrese Por Favor el Numero A Divinar:"))

    if ingreso == numero_secreto:
        print("Felicidades Acerto el numero Scereto Era:",numero_secreto)
        print(f"los Intentos de Adivinar este numero son:{i}")
        condicion = False
        
    
    elif ingreso > numero_secreto:
        print("Numero Ingresado Es Mayor a Numero a Divinar")
        
        
    elif ingreso < numero_secreto:
        print("Numero Ingresado Es Menor a Numero a Divinar")
    i += 1
        
    