diccionario = {'nombre':'Vicente','edad': 19, 'ciudad': 'Santiago'}
print(diccionario)

print(diccionario['ciudad'])

print(diccionario['nombre'])

diccionario['edad'] = 18
print(diccionario)
     
print()
capitales = {"Chile":"Santiago", "Mexico":"Ciudad de Mexico", "España":"Madrid"}
for pais in capitales.items():
    print(pais,capitales)
    
