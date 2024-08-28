# Solicitar una lista de números al usuario
numeros = input("Introduce una lista de números separados por comas: ").split(',')

# Convertir la lista de cadenas a números
numeros = [float(numero) for numero in numeros]

# Ordenar la lista de menor a mayor
numeros_ordenados = sorted(numeros)

# Mostrar la lista ordenada
print(f"La lista ordenada es: {numeros_ordenados}")
