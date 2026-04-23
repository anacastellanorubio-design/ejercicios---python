for i in range(5):
    color = input("Introduce un color: ")

    if color == "azul":
        print("¡Premio!")
        break      
    else:   
        print("No es correcto, prueba otro color.")

else:
    print("No has conseguido el premio. Inténtalo de nuevo")    