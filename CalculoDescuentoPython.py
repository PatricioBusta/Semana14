from Funcion import calcular_descuento

if __name__ == "__main__":
    #  1: Solo Subtotal
    subtotal_1 = 248.65
    descuento_1 = calcular_descuento(subtotal_1)
    total_1 = subtotal_1 - descuento_1
    print(f"Compra 1: Subtotal: ${subtotal_1:.2f}, Descuento: ${descuento_1:.2f}, Total: ${total_1:.2f}")

    # 2: Subtotal y porcentaje de descuento personalizado
    subtotal_2 = 134.56
    porcentaje_descuento_2 = 20
    descuento_2 = calcular_descuento(subtotal_2, porcentaje_descuento_2)
    total_2 = subtotal_2 - descuento_2
    print(f"Compra 2: Subtotal: ${subtotal_2:.2f}, Descuento: ${descuento_2:.2f}, Total: ${total_2:.2f}")