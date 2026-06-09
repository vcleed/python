saldo = 1000

print("\t.:MENU:.")
print("1. ingresar dinero en la cuenta")
print("2. retirar dinero en la cuenta")
print("3. Mostar dinero en la cuenta")
print("4. Salir ")
opcion = int(input("Digite una opcion de menu: "))

print()

if opcion==1:
    extra = float(input("cuanto dinero desea ingresar -> "))
    saldo += extra
    print(f"Dinero en la cuneta: {saldo}")
elif opcion==2:
    retirar = float(input("cuanto dinero desea retirar -> "))
    if retirar>saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo -= retirar
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==4:
    print("Gracias por ultilizar su cajero automatico")
else:
    print("Se equivoco de opcion")