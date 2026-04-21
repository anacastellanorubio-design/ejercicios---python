#Definir los siguientes datos
Camiseta = 10 
Sudadera = 20.5
Gorra = 5.5 

print("Camiseta: 10 euros")
print("Sudadera: 20.5 euros")
print("Gorra: 5.5 euros")
print("Que cantidad de cada articulo?")

#Preguntar la cantidad a usuario
cantidad_camiseta = int (input ("¿Cuántas camisetas quiere? "))
cantidad_sudadera = int (input ("¿Cuántas sudaderas quiere? "))
cantidad_gorra = int (input ("¿Cuántas gorras quiere? "))

#Calcula el total de la Compra
total_camiseta = camiseta * cantidad_camiseta
total_sudadera = sudadera * cantidad_sudadera
total_gorras = gorra * cantidad_gorra
Total Compra = total_camiseta + total_sudadera + total_gorra

#Añadir 21% IVA al total de la Compra 
Total_compra_IVA = Total_compra +((Total_compra * 21)/100)


