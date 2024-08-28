# Solicitar una lista de números al usuario
numeros = input("Introduce una lista de números separados por comas: ").split(',')

# Convertir la lista de cadenas a números
numeros = [float(numero) for numero in numeros]

# Sumar todos los elementos de la lista
suma = sum(numeros)

# Mostrar el resultado
print(f"La suma de los elementos en la lista es: {suma}")
