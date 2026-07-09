while True:
    alumnos = {'A01':['Juan', '3ro medio'],
                'A02':['Maria','4to medio'],
                 'A03':['Pedro','2do medio'],

               }
    notas = {'A01': [6.5, 5.8, 7.0],
                'A02': [5.0, 6.2, 6.8],
                'A03': [4.5, 5.0, 3.9],
             }
    codigo = input("Ingrese su codigo de alumno: ").upper()
    if codigo in alumnos:
        nombre = alumnos[codigo][0]
        lista_notas = notas[codigo]
        promedio = round(sum(lista_notas) / len(lista_notas),1)
        print(f"{nombre} tiene un promedio de : {promedio}")
    else:
        print("Alumno no encontrado")
        
