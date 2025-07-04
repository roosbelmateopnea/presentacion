actual = int(input("Precio Actual * Hora:"))
ingreso = int(input("Ingrese Por Favor las Horas Trabajas:"))
calculo = ingreso - 40 
operacion1 = 40 * actual
operacion2 = actual * calculo * 2
operacion3 = actual * calculo * 3

if ingreso <= 40:
    print("Horas Extras Trabajadas:",calculo)
    print("Pago Normal Total:",actual * ingreso)
    
elif ingreso <=  48:
    print("Pago Normal:",40 * actual)
    print("Horas Extras Trabajadas:",calculo)
    print("Pago Horas Extras:",operacion2)
    print("Pago Total:",operacion1 + operacion2)
    
elif ingreso >  48:
    print("Pago Normal:",40 * actual)
    print("Horas Extras Trabajadas:",calculo)
    print("Pago Horas Extras:",operacion3)
    print("Pago Total:",operacion1 + operacion3)
    




