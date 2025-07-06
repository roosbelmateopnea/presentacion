import random
preguntas = {
    1: [
        {
            "pregunta": "¿Cuántos días tiene una semana?",
            "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿De qué color es el cielo en un día despejado?",
            "opciones": ["A) Verde", "B) Azul", "C) Gris", "D) Amarillo"],
            "respuesta": "B"
        }
    ],
    2: [
        {
            "pregunta": "¿Cuál es el número que sigue después del 19?",
            "opciones": ["A) 18", "B) 20", "C) 21", "D) 22"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué planeta es conocido como el 'planeta rojo'?",
            "opciones": ["A) Venus", "B) Marte", "C) Júpiter", "D) Saturno"],
            "respuesta": "B"
        }
    ],
    3: [
        {
            "pregunta": "¿Cuántas patas tiene una araña?",
            "opciones": ["A) 6", "B) 8", "C) 10", "D) 4"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Quién escribió Don Quijote de la Mancha?",
            "opciones": ["A) Gabriel García Márquez", "B) Pablo Neruda", "C) Miguel de Cervantes", "D) Federico García Lorca"],
            "respuesta": "C"
        }
    ],
    4: [
        {
            "pregunta": "¿Cuál es la capital de México?",
            "opciones": ["A) Guadalajara", "B) Monterrey", "C) Cancún", "D) Ciudad de México"],
            "respuesta": "D"
        },
        {
            "pregunta": "¿Cuántos continentes hay en el mundo?",
            "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "respuesta": "C"
        }
    ],
    5: [
        {
            "pregunta": "Si tienes 3 pares de zapatos, ¿cuántos zapatos tienes en total?",
            "opciones": ["A) 3", "B) 4", "C) 6", "D) 8"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué gas necesitamos para respirar?",
            "opciones": ["A) Hidrógeno", "B) Nitrógeno", "C) Dióxido de carbono", "D) Oxígeno"],
            "respuesta": "D"
        }
    ],
    6: [
        {
            "pregunta": "Si un tren sale a las 3:00 p.m. y llega a las 6:30 p.m., ¿cuánto duró el viaje?",
            "opciones": ["A) 2 horas", "B) 3 horas", "C) 3 horas y media", "D) 4 horas"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Quién propuso la teoría de la relatividad?",
            "opciones": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Stephen Hawking"],
            "respuesta": "C"
        }
    ],
    7: [
        {
            "pregunta": "¿Cuál es el resultado de 1/2 + 1/4?",
            "opciones": ["A) 3/4", "B) 1", "C) 2/4", "D) 5/4"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Qué país tiene la ciudad de Estambul?",
            "opciones": ["A) Grecia", "B) Turquía", "C) Italia", "D) Egipto"],
            "respuesta": "B"
        }
    ],
    8: [
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["A) 1914", "B) 1929", "C) 1939", "D) 1945"],
            "respuesta": "C"
        },
        {
            "pregunta": "Si el 30% de  una cantidad es 90, ¿cuál es la cantidad total?",
            "opciones": ["A) 200", "B) 250", "C) 270", "D) 300"],
            "respuesta": "C"
        }
    ],
    9: [
        {
            "pregunta": "¿Qué filósofo escribió La República?",
            "opciones": ["A) Aristóteles", "B) Sócrates", "C) Platón", "D) Descartes"],
            "respuesta": "C"
        },
        {
            "pregunta": "Si una inversión crece un 5% anual compuesto durante 3 años, ¿cuál es el factor de crecimiento?",
            "opciones": ["A) 1.15", "B) 1.157625", "C) 1.05", "D) 1.10"],
            "respuesta": "B"
        }
    ],
    10: [
        {
            "pregunta": "¿Qué afirma el Principio Antrópico en cosmología?",
            "opciones": [
                "A) Que la vida en la Tierra es una coincidencia absoluta.",
                "B) Que el universo debe permitir la existencia del observador consciente.",
                "C) Que la materia oscura no tiene influencia en la evolución del universo.",
                "D) Que el tiempo es una ilusión perceptual creada por el cerebro."
            ],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué establece el Teorema de Bell en física cuántica?",
            "opciones": [
                "A) Que las partículas cuánticas pueden comunicarse instantáneamente.",
                "B) Que las leyes clásicas explican todos los fenómenos subatómicos.",
                "C) Que no existe el entrelazamiento cuántico.",
                "D) Que ninguna teoría de variables ocultas local puede reproducir todas las predicciones de la mecánica cuántica."
            ],
            "respuesta": "D"
        }
    ]
}


import random
preguntas = {
    1: [
        {
            "pregunta": "¿Cuántos días tiene una semana?",
            "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿De qué color es el cielo en un día despejado?",
            "opciones": ["A) Verde", "B) Azul", "C) Gris", "D) Amarillo"],
            "respuesta": "B"
        }
    ],
    2: [
        {
            "pregunta": "¿Cuál es el número que sigue después del 19?",
            "opciones": ["A) 18", "B) 20", "C) 21", "D) 22"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué planeta es conocido como el 'planeta rojo'?",
            "opciones": ["A) Venus", "B) Marte", "C) Júpiter", "D) Saturno"],
            "respuesta": "B"
        }
    ],
    3: [
        {
            "pregunta": "¿Cuántas patas tiene una araña?",
            "opciones": ["A) 6", "B) 8", "C) 10", "D) 4"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Quién escribió Don Quijote de la Mancha?",
            "opciones": ["A) Gabriel García Márquez", "B) Pablo Neruda", "C) Miguel de Cervantes", "D) Federico García Lorca"],
            "respuesta": "C"
        }
    ],
    4: [
        {
            "pregunta": "¿Cuál es la capital de México?",
            "opciones": ["A) Guadalajara", "B) Monterrey", "C) Cancún", "D) Ciudad de México"],
            "respuesta": "D"
        },
        {
            "pregunta": "¿Cuántos continentes hay en el mundo?",
            "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "respuesta": "C"
        }
    ],
    5: [
        {
            "pregunta": "Si tienes 3 pares de zapatos, ¿cuántos zapatos tienes en total?",
            "opciones": ["A) 3", "B) 4", "C) 6", "D) 8"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué gas necesitamos para respirar?",
            "opciones": ["A) Hidrógeno", "B) Nitrógeno", "C) Dióxido de carbono", "D) Oxígeno"],
            "respuesta": "D"
        }
    ],
    6: [
        {
            "pregunta": "Si un tren sale a las 3:00 p.m. y llega a las 6:30 p.m., ¿cuánto duró el viaje?",
            "opciones": ["A) 2 horas", "B) 3 horas", "C) 3 horas y media", "D) 4 horas"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Quién propuso la teoría de la relatividad?",
            "opciones": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Stephen Hawking"],
            "respuesta": "C"
        }
    ],
    7: [
        {
            "pregunta": "¿Cuál es el resultado de 1/2 + 1/4?",
            "opciones": ["A) 3/4", "B) 1", "C) 2/4", "D) 5/4"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Qué país tiene la ciudad de Estambul?",
            "opciones": ["A) Grecia", "B) Turquía", "C) Italia", "D) Egipto"],
            "respuesta": "B"
        }
    ],
    8: [
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["A) 1914", "B) 1929", "C) 1939", "D) 1945"],
            "respuesta": "C"
        },
        {
            "pregunta": "Si el 30% de  una cantidad es 90, ¿cuál es la cantidad total?",
            "opciones": ["A) 200", "B) 250", "C) 270", "D) 300"],
            "respuesta": "C"
        }
    ],
    9: [
        {
            "pregunta": "¿Qué filósofo escribió La República?",
            "opciones": ["A) Aristóteles", "B) Sócrates", "C) Platón", "D) Descartes"],
            "respuesta": "C"
        },
        {
            "pregunta": "Si una inversión crece un 5% anual compuesto durante 3 años, ¿cuál es el factor de crecimiento?",
            "opciones": ["A) 1.15", "B) 1.157625", "C) 1.05", "D) 1.10"],
            "respuesta": "B"
        }
    ],
    10: [
        {
            "pregunta": "¿Qué afirma el Principio Antrópico en cosmología?",
            "opciones": [
                "A) Que la vida en la Tierra es una coincidencia absoluta.",
                "B) Que el universo debe permitir la existencia del observador consciente.",
                "C) Que la materia oscura no tiene influencia en la evolución del universo.",
                "D) Que el tiempo es una ilusión perceptual creada por el cerebro."
            ],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué establece el Teorema de Bell en física cuántica?",
            "opciones": [
                "A) Que las partículas cuánticas pueden comunicarse instantáneamente.",
                "B) Que las leyes clásicas explican todos los fenómenos subatómicos.",
                "C) Que no existe el entrelazamiento cuántico.",
                "D) Que ninguna teoría de variables ocultas local puede reproducir todas las predicciones de la mecánica cuántica."
            ],
            "respuesta": "D"
        }
    ]
}
import random
preguntas = {
    1: [
        {
            "pregunta": "¿Cuántos días tiene una semana?",
            "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿De qué color es el cielo en un día despejado?",
            "opciones": ["A) Verde", "B) Azul", "C) Gris", "D) Amarillo"],
            "respuesta": "B"
        }
    ],
    2: [
        {
            "pregunta": "¿Cuál es el número que sigue después del 19?",
            "opciones": ["A) 18", "B) 20", "C) 21", "D) 22"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué planeta es conocido como el 'planeta rojo'?",
            "opciones": ["A) Venus", "B) Marte", "C) Júpiter", "D) Saturno"],
            "respuesta": "B"
        }
    ],
    3: [
        {
            "pregunta": "¿Cuántas patas tiene una araña?",
            "opciones": ["A) 6", "B) 8", "C) 10", "D) 4"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Quién escribió Don Quijote de la Mancha?",
            "opciones": ["A) Gabriel García Márquez", "B) Pablo Neruda", "C) Miguel de Cervantes", "D) Federico García Lorca"],
            "respuesta": "C"
        }
    ],
    4: [
        {
            "pregunta": "¿Cuál es la capital de México?",
            "opciones": ["A) Guadalajara", "B) Monterrey", "C) Cancún", "D) Ciudad de México"],
            "respuesta": "D"
        },
        {
            "pregunta": "¿Cuántos continentes hay en el mundo?",
            "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "respuesta": "C"
        }
    ],
    5: [
        {
            "pregunta": "Si tienes 3 pares de zapatos, ¿cuántos zapatos tienes en total?",
            "opciones": ["A) 3", "B) 4", "C) 6", "D) 8"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué gas necesitamos para respirar?",
            "opciones": ["A) Hidrógeno", "B) Nitrógeno", "C) Dióxido de carbono", "D) Oxígeno"],
            "respuesta": "D"
        }
    ],
    6: [
        {
            "pregunta": "Si un tren sale a las 3:00 p.m. y llega a las 6:30 p.m., ¿cuánto duró el viaje?",
            "opciones": ["A) 2 horas", "B) 3 horas", "C) 3 horas y media", "D) 4 horas"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Quién propuso la teoría de la relatividad?",
            "opciones": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Stephen Hawking"],
            "respuesta": "C"
        }
    ],
    7: [
        {
            "pregunta": "¿Cuál es el resultado de 1/2 + 1/4?",
            "opciones": ["A) 3/4", "B) 1", "C) 2/4", "D) 5/4"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Qué país tiene la ciudad de Estambul?",
            "opciones": ["A) Grecia", "B) Turquía", "C) Italia", "D) Egipto"],
            "respuesta": "B"
        }
    ],
    8: [
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["A) 1914", "B) 1929", "C) 1939", "D) 1945"],
            "respuesta": "C"
        },
        {
            "pregunta": "Si el 30% de  una cantidad es 90, ¿cuál es la cantidad total?",
            "opciones": ["A) 200", "B) 250", "C) 270", "D) 300"],
            "respuesta": "C"
        }
    ],
    9: [
        {
            "pregunta": "¿Qué filósofo escribió La República?",
            "opciones": ["A) Aristóteles", "B) Sócrates", "C) Platón", "D) Descartes"],
            "respuesta": "C"
        },
        {
            "pregunta": "Si una inversión crece un 5% anual compuesto durante 3 años, ¿cuál es el factor de crecimiento?",
            "opciones": ["A) 1.15", "B) 1.157625", "C) 1.05", "D) 1.10"],
            "respuesta": "B"
        }
    ],
    10: [
        {
            "pregunta": "¿Qué afirma el Principio Antrópico en cosmología?",
            "opciones": [
                "A) Que la vida en la Tierra es una coincidencia absoluta.",
                "B) Que el universo debe permitir la existencia del observador consciente.",
                "C) Que la materia oscura no tiene influencia en la evolución del universo.",
                "D) Que el tiempo es una ilusión perceptual creada por el cerebro."
            ],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué establece el Teorema de Bell en física cuántica?",
            "opciones": [
                "A) Que las partículas cuánticas pueden comunicarse instantáneamente.",
                "B) Que las leyes clásicas explican todos los fenómenos subatómicos.",
                "C) Que no existe el entrelazamiento cuántico.",
                "D) Que ninguna teoría de variables ocultas local puede reproducir todas las predicciones de la mecánica cuántica."
            ],
            "respuesta": "D"
        }
    ]
}

pago = 1
contador = 1
condicion = True
condicionb = True
comodin1 = ["1.Llamar a un amigo"]
comodin2 = ["2.50/50"]
comodin3 = ["3.Cambiar de pregunta"]

while condicion:
    print(f"NIVEL:{contador}")
    print(preguntas[contador][0]["pregunta"])
    for opcion in preguntas[contador][0]["opciones"]:
        print(opcion)
        
    respuesta = input("Ingrese por favor la respuesta 'A','B','C','D' o la palabra 'comodin': ").upper()
    if respuesta == "COMODIN":
        print("¡Vamos con toda tu Puedes!")
        print("Comodines Disponibles:")
        print(comodin1)
        print(comodin2)
        print(comodin3)
  
        comodin = input("Escribe 1, 2 o 3 según el comodín que deseas usar: ")


        if comodin == "1":
            aleatorio = random.choice(["A", "B", "C", "D"])
            print("Tu amigo cree que la respuesta es:",aleatorio)
            comodin1.remove("1.Llamar a un amigo")




        elif comodin == "2":
            correcta = preguntas[contador][0]["respuesta"]
            letras = ["A", "B", "C", "D"]
            letras.remove(correcta)
            opcion_extra = random.choice(letras)

            print("Opciones disponibles después del 50/50:")
            print(preguntas[contador][0]["pregunta"])
            for prueba in preguntas[contador][0]["opciones"]:
                if prueba[0] == correcta or prueba[0] == opcion_extra:
                    print(prueba)
            comodin2.remove("2.50/50")
        

        elif comodin == "3":
            
            print("¡Vamos con toda tu Puedes!")
            comodin3.remove("3.Cambiar de pregunta")
            print(preguntas[contador][1]["pregunta"])
            for opcion in preguntas[contador][1]["opciones"]:
                print(opcion)
            nueva_respuesta = input("Ingrese por favor la respuesta 'A','B','C','D':").upper()
            if nueva_respuesta == preguntas[contador][1]["respuesta"]:
                print("¡Correcto Felicidades!")
                print("Tu pago hasta el Momento es de:",pago * 100000)
                contador += 1
                pago += 1
            else:
                print("Incorrecto. Has perdido Tu Dinero.")
                condicion = False

    elif respuesta == preguntas[contador][0]["respuesta"]:
        print("Felicidades. Respuesta correcta.")
        print("Tu pago hasta el Momento es de:",pago * 100000)
        contador += 1
        pago += 1
    else:
        print("Lo siento mucho. Respuesta incorrecta. Has perdido tu dinero.")
        condicion = False
