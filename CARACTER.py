localidades_vendidas = 0
opcion = 0
vender = 0
localidades = 200
devolucion = 0 

print ("***** MENU *****")
print ("1.- Localidades disponibles")
print("2.- Vender localidades")
print("3.- Devolver localidades")
print("4.- Historial de ventas")
print("5.- Salir")

while opcion !=5 :
    try:
        opcion = int(input("¿cual de estas opciones desea hacer?, porfavor ingrese un numero 1/5 de las opciones"))
        if opcion == 1:
            print(f"las localidades disponibles son: {localidades}")
        
        elif opcion == 2:
            vender = int(input("Ingrese la cantidad de localidades que desea vender: "))
            if (localidades_vendidas + vender)> localidades:
                print("Superaste el limite de localidades")
            else:
                localidades_vendidas = localidades_vendidas + vender
                print("Las localidades que compro son: {vender}")

        elif opcion == 3:
            devolucion = int(input("Ingrese las localidades que desea devolver: "))
            if devolucion <= 0:
             print("Error: la cantidad a devolver debe ser mayor a 0.")
            elif devolucion > 200:
                print("Error: No puede exceder las 200 localidades (maximo del teatro).")
            elif devolucion > localidades_vendidas:
                print (f"no puedes devolver más localidades de las que se han vendido ({localidades_vendidas}).")
            else:
             localidades_vendidas = localidades_vendidas - devolucion
             localidades = localidades + devolucion
             
             print(f"Se devolvieron correctamente sus localidades, las localidades que se devolvieron son: {devolucion}")

        elif opcion == 4:
            print(f"El historial de ventas hasta ahora es: {localidades_vendidas}")
        elif opcion == 5:
            print("Gracias por usar el sistema ")
        else:
            print("La opcion no es correcta")
    
    except ValueError:
        print("Error ingrese una opcion valida porfavor")
