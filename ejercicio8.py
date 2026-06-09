import random
nombre = input("Ingrese su nombre").upper()
inf = int(input("limite inferior: "))
sup = int(input("limite superior: "))


#generar numero aleatorio
numero_secreto = random.randint(1,10)

# Logica especial: si es Par, pasarlo a Impar 
if numero_secreto % 2== 0:
    if numero_secreto + 1 <=sup:
        numero_secreto += 1
    else:
        numero_secreto -= 1

# Variables de estado 
intentos = 4
puntaje = 120 
adivino = False

for i in range(1,intentos + 1):
    print(f"'\n--- Intento {i} de {intentos} ---")
    intento_usuario = int(input("Adivinia el numero: "))
    if intento_usuario == numero_secreto:
        print(f"Acceso Concedido,{nombre}")
        adivino = true 
        break
    else:
        distancia = abs(numero_secreto - intento_usuario)

        if distancia > 20:
            puntaje -= 30
        elif 10 <= distancia <= 20:
            puntaje -= 20
        else:
            puntaje = 10 
        
        #Pistas
        if intento_usuario < numero_secreto:
            print("El codigo secreto es MAYOR.")
        else:
            print("El codigo secreto es MENOR.")
        print(f"puntaje actual:{puntaje}")
        
        if not adivino:
            print(f"\nGame over. El codigo era: {numero_secreto}")
        
# clasificacion final
        print(f"\nRESULTADO FINAL")
        print(f"Jugador: {nombre}")
        print(f"Puntaje final: {puntaje}")
        
        if puntaje >= 90:
            print("clasificacion: Nivel experto")
        elif puntaje >= 50:
            print("clasificacion: Nivel novato")
        else:
            print("Clasificacion: Reprobado")