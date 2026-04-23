cantidad_notas = int(input("¿Cuántas notas deseas introducir? "))
suma = 0

for i in range(cantidad_notas):
    nota = float(input(f"Introduce la nota {i + 1}: "))
    suma +=nota

media = suma / cantidad_notas 

print("Suma Total:", suma)
print("Media", media)   
    




   
   
