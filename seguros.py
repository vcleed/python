vehiculos = 0
peso_pesado = 0
peso_ligero = 0
carga_toneladas = 0
print("----------------------------------")
print("-------Flota de vehiculos---------")
print("----------------------------------")
cantidad_valida = False
while cantidad_valida == False:
   try:
        vehiculos = int(input("¿Cuantos vehiculos desea registrar en esta sesion: "))
        if vehiculos > 0 :
            cantidad_valida = True 
        else:
            print("¡Cantidad invalida!")       
   except ValueError:
        print("!Cantidad invalida! Ingresa un entero positivo para continuar")
 
for i in range (vehiculos):
    print(f"\n---REGISTRO DEL VEHICULO {i + 1} DE {vehiculos}----")
    placa_valida = False
    while placa_valida == False :
        placa = input("\nIngrese la patente de su vehiculo: ")    
    if (len(placa)) >= 6 and " " not in placa :
        placa_valida = True
    else: 
            print("¡Placa invalida! Debe tenr al menos 6 caracteres")  
        
while placa_valida == False :
    capacidad_valida = False
    capacidad = 0 
try: 
        capacidad = int(input("Ingrese la cantidad de carga (en toneladas): "))
        if capacidad > 0 :
            capacidad_valida = True
        else:
            print("Error logistico, Ingrese un numero entero positivo para la capacidad de carga.")  
except ValueError:
        print("Error logistico, Ingrese un numero entero positivo para la capacidad de carga.")
if capacidad >55:
    peso_ligero = peso_ligero + 1
    print(f"Vehiculo {placa} registrado como: PESADO")
    peso_pesado = peso_pesado + 1 
    print(f"Vehiculo {placa} registrado como: LIGERO")

#-----informe final-----
print("\n===========================================================================================================")
print(f"¡La flota de cuenta con {peso_pesado} vehiculos pesados y {peso_ligero} vehiculos Ligeros ¡Rutas asignadas! ")
print("=============================================================================================================")





