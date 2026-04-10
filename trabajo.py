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

def clasificar_total(total):
    if total == 0:
        return "Sin compra"
    elif total < 3000:
        return "Compra baja"
    else:
        return "Compra alta"

def mostrar_productos(lista_precios):
    print("Productos comprados:")
    for i in range(len(lista_precios)):
        print(f"Producto {i+1}: ${lista_precios[i]}")

def contar_productos(lista_precios):
    i = 0
    contador = 0
    while i < len(lista_precios):
        contador += 1
        i += 1
    return contador

def mostrar_ticket(precio1, precio2, precio3):
    precios = [precio1, precio2, precio3]
    
    total = calcular_precio_total(precio1, precio2, precio3)
    mensaje = evaluar_compra(total, "Anto", "hamburguesas")
    
    clasificacion = clasificar_total(total)
    cantidad = contar_productos(precios)

    print("Total a pagar: $", total)
    print(mensaje)
    print("Clasificación:", clasificacion)
    print("Cantidad de productos:", cantidad)
    mostrar_productos(precios)

mostrar_ticket(2000, 1500, 1800)

    