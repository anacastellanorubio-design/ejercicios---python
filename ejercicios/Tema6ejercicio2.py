#crear una lista con los 12 meses del año
meses_año= ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

#Pedir a la usuaria que elija un número del 1 al 12 
numero = int(input("Introduce un número del 1 al 12: "))

if numero >= 1 and numero <= 12:
    mes = meses_año[numero - 1]
    print("El mes es:", mes)

if mes == "Junio":
        print("EL MEJOR MES")    