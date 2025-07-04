def countApplesAndOranges(s, t, a, b, apples, oranges):
    manzanas_en_casa = 0
    naranjas_en_casa = 0
    for i in range(len(apples)):
        posicion_manzana = a + apples[i] 
        if posicion_manzana >= s and posicion_manzana <= t:
            manzanas_en_casa = manzanas_en_casa + 1
    for j in range(len(oranges)):
        posicion_naranja = b + oranges[j] 
        if posicion_naranja >= s and posicion_naranja <= t:
            naranjas_en_casa = naranjas_en_casa + 1
    print(manzanas_en_casa)
    print(naranjas_en_casa)
 