agregar = []
reprobadas = []
aprobadas = []
cantidad = int(input("Ingrese Por Favor Numero Materias:"))
contador = 1
for i in range(cantidad):
    materias = input(f"Ingrese #{contador} Materia:")
    agregar.append(materias)
    contador += 1

contadorb = 0
for j in agregar:
    notas_pedir = int(input(f"Ingrese Nota de {agregar[contadorb]}"":"))
    if notas_pedir < 60:
        reprobadas.append(agregar[contadorb])
    elif notas_pedir >= 60:
        aprobadas.append(agregar[contadorb])
    contadorb +=1

print("Tus Materias Reprobadas son:",reprobadas)
