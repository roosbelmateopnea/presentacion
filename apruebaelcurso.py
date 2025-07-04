pracalificacion = int(input("Ingrese Por Fvaor la Primeera Calificacion:"))
sgocalificacion = int(input("Ingrese Por Favor la Segunda Calificaacion:"))
tracalificacion = int(input("INgrese Por Favior la Tercera Calificacion:"))
suma = pracalificacion + sgocalificacion + tracalificacion
division = suma / 3

if division < 70:
    print("Reprueba Este Curso")
elif division >= 70:
    print("Aprueba Este Curso")    
