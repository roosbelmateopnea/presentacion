numero1 = int(input("Ingrese el Primer Numero Por Fvaor:"))
numero2 = int(input("Ingrese el Segundo Numero Por Favor:"))
numero3= int(input("Ingrese el Tercer Numero Por Favor"))

if numero1 > numero2 and numero1 > numero3:
    print("El Numero Mayor Es:",numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El Numero Mayor Es:",numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("El Numero Mayor Es:",numero3)