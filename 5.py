# Solicitar una cadena de texto al usuario
cadena = input("Introduce una cadena de texto: ").lower()

# Definir las vocales
vocales = "aeiou"

# Contar las vocales en la cadena
contador_vocales = sum(1 for letra in cadena if letra in vocales)

# Mostrar el resultado
print(f"El número de vocales en la cadena es: {contador_vocales}")
