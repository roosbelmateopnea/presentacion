vocales = ["A","E","I","O","U"]
A = []
E = []
I = []
O = []
U = []
palabra = input("Ingrese Por Favor una Palabra:").upper()
i = 0
while i < len(palabra):
    if palabra[i] == vocales[0]:
        A.append(1)
    if palabra[i] == vocales[1]:
        E.append(1)
    if palabra[i] == vocales[2]:
        I.append(1)
    if palabra[i] == vocales[3]:
        O.append(1)
    if palabra[i] == vocales[4]:
        U.append(1)
    i += 1
print("Bocal 'A'",sum(A),"Veces")
print("Bocal 'E'",sum(E),"Veces")
print("Bocal 'I'",sum(I),"Veces")
print("Bocal 'O'",sum(O),"Veces")
print("Bocal 'U'",sum(U),"Veces")