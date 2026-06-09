vehiculos = 0
peso_pesado = 0
peso_ligero = 0

print("--------------------------------------------------")
print("---- SISTEMA DE REGISTRO DE FLOTA CORPORATIVA ----")
print("--------------------------------------------------")

cantidad_valida = False
while cantidad_valida == False:
    try:
        vehiculos = int(input("¿Cuántos vehículos desea registrar en esta sesión?: "))
        if vehiculos > 0:
            cantidad_valida = True
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo.")

# El ciclo FOR que repite TODO por cada vehículo
for i in range(vehiculos):
    print(f"\n--- REGISTRO DEL VEHÍCULO {i + 1} DE {vehiculos} ---")
    
    # 1. Bloque de la Patente
    placa_valida = False
    while placa_valida == False:
        placa = input("Ingrese la patente de su vehículo: ")
        if len(placa) >= 6 and " " not in placa:
            placa_valida = True
        else:
            print("¡Placa inválida! Debe tener al menos 6 caracteres y sin espacios.")

    # 2. Bloque de la Capacidad (Bien puesto adentro del FOR)
    capacidad_valida = False
    capacidad = 0
    while capacidad_valida == False:
        try:
            capacidad = int(input("Ingrese la cantidad de carga (en toneladas): "))
            if capacidad > 0:
                capacidad_valida = True
            else:
                print("Error logístico, Ingrese un numero entero positivo")
        except ValueError:
            print("Error logístico, Ingrese un numero entero positivo")

    # 3. Clasificación inmediata
    if capacidad > 55:
        peso_pesado = peso_pesado + 1
        print(f"Vehículo [{placa}] registrado como: PESADO")
    else:
        peso_ligero = peso_ligero + 1
        print(f"Vehículo [{placa}] registrado como: LIGERO")

# Informe final
print("\n==============================================")
print(f"¡La flota cuenta con {peso_pesado} vehículos Pesados y {peso_ligero} vehículos Ligeros! ¡Rutas asignadas!")
print("==============================================")