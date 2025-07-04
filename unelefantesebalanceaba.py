condicion = True
while condicion:
    ingreso = int(input("Ingrese Por favor Numero Cuantos Elefantes se Valanceban:"))  
    if ingreso == 1:
        print("1 elefante se balanceaba")
        print("Sobre la tela de una araña")
        print("Como veía que resistía")
        print("Fueron a llamar otro elefante")
        condicion = False
    elif ingreso != i:
        print("Dato Ingresado Erroneo Ingrese El siguiente numero por Favor:")
i = 2
while i <= 10:
    ingreso = int(input("Ingrese Por favor Numero Cuantos Elefantes se Valanceban:"))  
    if ingreso == i:
        print(i,"elefantes se balanceaban")
        print("Sobre la tela de una araña")
        print("Como veía que resistía")
        print("Fueron a llamar otro elefante")
        i += 1
    elif ingreso != i:
        print("Dato Ingresado Erroneo Ingrese El siguiente numero por Favor:")