print("======================================================================================================")
print("============== ¡Bienvenido al sistema de gestión de localidades del Teatro Municipal! ================")
print("======================================================================================================")
localidades = 200
opcion = 0
historial = 0
while opcion !=5:
    try:
        print("\n----Menu principal-----")
        print("1.-Localidades disponibles")
        print("2.-Vender localidades")
        print("3.-Devolver localidades")
        print("4.-Historial de ventas")
        print("5.-Salir")

        opcion = int(input("Ingrese la opcion que desea hacer (1/5): "))
        if opcion == 1:
            print(f"Las localidades dispoibles son: {localidades}")
        elif opcion ==2:
            vender = int(input("Ingrese las localidades que desea vender: ")) 
            if vender > localidades :
                print("Error no puede vender mas localidades de las que hay disponible. ")
            elif vender <=0:
                print("Debe ingresar un numero positivo")
            else:
                localidades = localidades - vender
                historial = historial + vender 
        elif opcion == 3:
            devolucion = int(input("Ingrese las localidades que desea devolver: "))
            if devolucion <=0:
                print("Error, debe ingresar un numero positvo.")
            elif (devolucion < + localidades) > 200:
                print("No puede devolver mas localidades de las que ya hay") 
            else:
                localidades = localidades + devolucion
                historial = historial + devolucion    
                print (f"Sus localidades de devolvieron correctamente, las localidades que se devolvieron son: {devolucion}")
        elif opcion ==4:
            print(f"El historial de ventas hasta ahora es de : {historial}")
        elif opcion ==5:
            ("Gracias por entar al sistema.") 
        else:
            print("Error,Ingrese una opcion valida porfavor. ")     
    except ValueError:
        print("Error logistico, debe ingresar un numero entero positivo porfavor.")                     






