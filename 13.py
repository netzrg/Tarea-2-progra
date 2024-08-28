# Solicitar una cadena de texto y un carácter específico al usuario
cadena = input("Introduce una cadena de texto: ").lower()
caracter = input("Introduce el carácter que deseas contar: ").lower()

# Contar el número de veces que aparece el carácter en la cadena
contador_caracter = cadena.count(caracter)

# Mostrar el resultado
print(f"El carácter '{caracter}' aparece {contador_caracter} veces en la cadena.")
