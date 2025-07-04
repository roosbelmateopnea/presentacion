def bonAppetit(bill, k, b):
    total = 0
    for i in range(len(bill)):
        if i != k:
            total = total + bill[i]

    parte_anna = total // 2

    if b == parte_anna:
        print("Bon Appetit")
    else:
        devolucion = b - parte_anna
        print(devolucion)
