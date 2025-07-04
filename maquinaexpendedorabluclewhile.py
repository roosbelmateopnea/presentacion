productos = {
    1: {"producto": "Cafe", "precio": 3000},
    2: {"producto": "Te", "precio": 2500},
    3: {"producto": "Jugo", "precio": 3500}
}
Total = []
while True:
    print(f"1.Producto: {productos[1]['producto']} Valor ${productos[1]['precio']}")
    print(f"2.Producto: {productos[2]['producto']} Valor ${productos[2]['precio']}")
    print(f"3.Producto: {productos[3]['producto']} Valor ${productos[3]['precio']}")
    ingreso = int(input("Ingrese Por Favor Productos a Comprar,'0' Salir:"))
    match ingreso:
        case 0:
            print("Compra Terminada")
            break
        case 1:
            print("Compra de Cafe Valor 3000")
            Total.append(productos[1]["precio"])
        case 2:
            print("Compra de Te Valor 2500")
            Total.append(productos[2]["precio"])
        case 3:
            print("Compra de Jugo Valor 3500")
            Total.append(productos[3]["precio"])
        case _:
            print("Codigo Error")
print("Total productos Comprados",sum(Total))
                   