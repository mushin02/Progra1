precio_del_producto= int(input("ingrese el precio del producto"))
if (precio_del_producto<100):
    descuento= precio_del_producto * 0.02
elif(precio_del_producto >= 100):
    descuento= precio_del_producto * 0.1

precio_final = precio_del_producto - descuento

print(f'el precio final es {precio_final}')

