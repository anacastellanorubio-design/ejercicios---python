#Crear una lista con los 8 planetas 
planetas = ["Mercurio","Venus","Tierra","Marte","Júpiter"," Saturno","Urano","Neptuno"]

#Pedir al usuario que elija un númmero del 1 al 8 
numero = int(input("Introduce un número del 1 al 8: "))

if numero >= 1 and numero <= 8:
    print("El planeta es:", planetas[numero - 1])

else:
    print("Error: número inválido. Debe ser del 1 al 8.")  
 

