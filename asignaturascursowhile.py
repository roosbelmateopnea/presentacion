reprobadas = []
aprobadas = []
materias = []
notas = []

i = 0
j = 1
contar = int(input("Ingrese Por Fvaor Cuantas Materias Son:"))
while i < contar:
    conocer = input(f"Ingrese #{j} Materia:")
    materias.append(conocer)
    notasb = int(input(f"Ingrese Nota de {materias[i]}:"))
    notas.append(notasb)
    if notasb >= 60:
        aprobadas.append(materias[i])
    elif notasb < 60:
        reprobadas.append(materias[i])
    i += 1
    j += 1

print("Materias Reprobadas Son:",reprobadas)

#    notas_pedir = int(input(f"Ingrese Nota de {agregar[0 + contadorb]}"":"))