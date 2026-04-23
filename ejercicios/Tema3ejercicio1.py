# Solicitar datos
nombre = input("Nombre del producto: ")
precio_unidad = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento (%): "))
iva = float(input("IVA (%): "))

subtotal= precio_unidad * cantidad
precio_con_descuento = subtotal * (1 - descuento / 100)
precio_total = precio_con_descuento * (1 + iva / 100)