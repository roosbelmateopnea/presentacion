Materias = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

Matematicas = int(input("Ingrese Por Favor Nota de Matematicas:"))
Fisica = int(input("Ingrese Por Favor Nota de Fisica:"))
Quimica = int(input("Ingrese Por Favor Nota de Quimica:"))
Historia = int(input("Ingrese Por Favor Nota de Historia:"))
Lengua = int(input("Ingrese Por Favor Nota de Lengua:"))

if Matematicas >= 60:
    Materias.remove("Matematicas")

if Fisica >= 60:
    Materias.remove("Fisica")

if Quimica >= 60:
    Materias.remove("Quimica")

if Historia >= 60:
    Materias.remove("Historia")

if Lengua >= 60:
    Materias.remove("Lengua")

print("Las Asignaturas Reprobadas Son:",Materias)