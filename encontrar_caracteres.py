def contar_caracteres(cadena):
    # Crear un diccionario para almacenar la frecuencia y posición de cada carácter
    frecuencia_caracteres = {}
    print(enumerate(cadena))

    # Recorrer la cadena
    for i, caracter in enumerate(cadena):
        # Si el carácter ya está en el diccionario, actualizar la frecuencia y la posición
        if caracter in frecuencia_caracteres:
            frecuencia_caracteres[caracter]['frecuencia'] += 1
            frecuencia_caracteres[caracter]['posiciones'].append(i)
        else:
            # Si el carácter no está en el diccionario, agregarlo con frecuencia 1 y posición
            frecuencia_caracteres[caracter] = {'frecuencia': 1, 'posiciones': [i]}

    # Imprimir los resultados
    for caracter, info in frecuencia_caracteres.items():
        print(f"El carácter '{caracter}' se repite {info['frecuencia']} veces en las posiciones {info['posiciones']}.")

# Ejemplo de uso
cadena_ejemplo = "abracadabra"
contar_caracteres(cadena_ejemplo)
