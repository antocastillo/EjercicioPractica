def calcular_precio_total(precio1, precio2, precio3):
    total = 0
    for precio in [precio1, precio2, precio3]:
        total += precio
    return total

def evaluar_compra(total, nombre, comida):
    if total > 5000:
        estado = "Compra cara"
    else:
        estado = "Compra económica"
    
    if total == 0:
        estado = "No compraste nada"

    return f"{nombre} compró {comida}: {estado}"

def mostrar_ticket(precio1, precio2, precio3):
    total = calcular_precio_total(precio1, precio2, precio3)
    mensaje = evaluar_compra(total, "Anto", "hamburguesas")
    print("Total a pagar: $", total)
    print(mensaje)


mostrar_ticket(2000, 1500, 1800)
