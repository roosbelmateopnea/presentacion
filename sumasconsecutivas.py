total = int(input("Ingrese Por favor el Primer Numero:"))
total += int(input("Ingrese Por Favor el Segundo Numero:"))

while True:
    pregunta = input("Quieres Añadir Otro Numero si / no:")
    if  pregunta == "si":
        total += int(input("Ingrese Por Favor otro Numero:"))

    elif pregunta == "no":
        break 
    
    else:
        print("El valor A ingresar es Valido Ingresa Si/No")
print("El Resultdo Total es:",total)
