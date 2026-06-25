def mostrar_menu():
    print("======== MENÚ REFUGIO ========")
    print("1. Registrar animal")
    print("2. Buscar animal")
    print("3. Eliminar animal")
    print("4. Evaluar aptitud")
    print("5. Mostrar animales")
    print("6. Salir")
    print("==============================")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("seleccione un opción: "))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opcion 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero")
    return opcion

def validar_nombre(name):
    return name.strip() 

def validar_edad(edad):
    return edad.isdigit() and int(edad) >= 0

def validar_peso(peso):
    return peso.isdigit() and float(peso) > 0



    

#opcion1
def registrar_animal(lista):
    nombre = input("Ingrese el nombre del animal: ")
    correcta = validar_nombre(nombre)
    if not correcta:
        print("El nombre no puede estar en Blanco")
        return
    edad = input("Ingrese la edad del animal: ")
    correcta = validar_edad(edad)
    if not correcta:
        print("Debe ser un numero entero mayor a 0")
        return
    peso = input("Ingrese el peso del animal: ")
    correcta = validar_peso(peso)
    if not correcta:
        print("Debe Ingresar un numero entero mayor a 0")
        return
    animal = {
        "nombre": nombre.strip(),
        "edad": int(edad),
        "peso": float(peso),
        "apto": False
}
    lista.append(animal)
    print("Animal correctamente ingresado")
#opcion2
def buscar_animal(lista, nombre_buscar):
     for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre_buscar.lower():
            return i  
        return -1
#opcion4
def evaluar_aptitud(lista):
    # Recorremos cada diccionario (cada animal) dentro de la lista
    for animal in lista:
        # Aplicamos la regla lógica basada en la edad
        if animal["edad"] >= 1:
            animal["apto"] = True
        else:
            animal["apto"] = False
#codigo principal
datos_animal = []
op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()

    if op == 1:
        registrar_animal(datos_animal)

    elif op == 2:
        print("======== BUSCAR ANIMAL ========")
        nombre_buscar = input("Ingrese el nombre del animal a buscar: ")
        
        posicion = buscar_animal(datos_animal, nombre_buscar)
        
        if posicion != -1:
            animal_encontrado = datos_animal[posicion]
            print(f"\n¡Animal encontrado en la posición {posicion}!")
            print(f"Nombre: {animal_encontrado['nombre']}")
            print(f"Edad: {animal_encontrado['edad']} años")
            print(f"Peso: {animal_encontrado['peso']} kg")
        else:
            print(f"\nEl animal '{nombre_buscar}' no se encuentra registrado.")

    elif op == 3:
        print("======== ELIMINAR ANIMAL ========")
        nombre_eliminar = input("Ingrese el nombre del animal que desea eliminar: ") 
    
        posicion = buscar_animal(datos_animal, nombre_eliminar) 
        
        # Evaluamos si el animal existe
        if posicion != -1:
            animal_borrado = datos_animal.pop(posicion) 
            print(f"\nEl animal '{animal_borrado['nombre']}' ha sido eliminado correctamente.")
        else:
            print(f"\nEl animal '{nombre_eliminar}' no se encuentra registrado.") 
    elif op == 4:
        print("======== EVALUAR APTITUD ========")
        evaluar_aptitud(datos_animal)
        print("\nSe ha evaluado la aptitud de todos los animales con éxito.")
    elif op == 5:
        print("======== LISTA DE ANIMALES ========")
        
        evaluar_aptitud(datos_animal)
        
        if len(datos_animal) == 0:
            print("\nNo hay animales registrados en el refugio actualmente.")
        else:
            for animal in datos_animal:
                # Determinamos el texto del estado según el booleano
                if animal["apto"]:
                    estado_texto = "APTO PARA ADOPCIÓN"
                else:
                    estado_texto = "EN OBSERVACIÓN"
                
                print(f"\nNombre: {animal['nombre']}")
                print(f"Edad: {animal['edad']} años")
                print(f"Peso: {animal['peso']} kg")
                print(f"Estado: {estado_texto}")
                print("\n" + "*" * 44)  # Línea separadora
    elif op == 6:
        print("Gracias por usar el sistema. Vuelva pronto")