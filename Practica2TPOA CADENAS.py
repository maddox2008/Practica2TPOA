frase = input('Ingresa una frase: ')
lista_palabras = frase.split()
print('Lista de palabras:', lista_palabras)

for palabra in lista_palabras:
    print(palabra.upper())

palabra_buscar = input('\n¿Que palabra quieres contar en la frase?: ')
cantidad = frase.count(palabra_buscar)
print('La palabra \'' + palabra_buscar + '\' aparece ' + str(cantidad) + ' veces.')

palabra_original = input('\n¿Que palabra quieres reemplazar?: ')
palabra_nueva = input('¿Por cual palabra la quieres reemplazar?: ')
frase_modificada = frase.replace(palabra_original, palabra_nueva)
print('Frase modificada:', frase_modificada)