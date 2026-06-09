saldo = 1000
print("\t--Menu--")
print("1.-Ingresar dinero en la cuenta ")
print("2.-Retirar dinero de la cuenta")
print("3.-Mostrar dinero de la cuenta ")
print("4.-Transferir a otra cuenta ")
print("5.-Salir")
print()
try :
        opcion =int(input("Elija una opcion de menu:  "))
        if opcion==1:
                extra =float(input("Ingrese el dinero que ingresara a su cuenta: "))
                saldo += extra
                print(f"SU saldo es : {saldo}")
        elif opcion==2:
                resta =float(input("Cuanto dinero desea retirar:")) 
                if resta>saldo :
                        print("No tienes el saldo suficiente")  
                else:
                        saldo-=resta
                        print(f"Su saldo es {saldo}") 
        elif opcion ==3:
                print(f"SU saldo es : {saldo}")
        elif opcion ==4:
                cuenta = input("Escriba el nombre de la cuenta que desea transferir: ")
    
                transferencia_monto = int(input("¿Cual es el monto que desea transferir:  "))
                total = transferencia_monto - saldo
                print(f"El saldo de su cuenta quedo en {total}")
                print()
                print("Se ah realizado la transferencia correctamente")
        elif opcion ==5 :
                print("Gracias por entrar al cajero automatico")
        else:
                print("La opcion escogida no es la correcta ")
             
except ValueError  :
 print("Error porfavor ingrese un NUMERO")