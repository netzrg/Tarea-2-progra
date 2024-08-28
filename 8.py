# Solicitar una lista de números al usuario
numeros = input("Introduce una lista de números separados por comas: ").split(',')

# Convertir la lista de cadenas a números
numeros = [float(numero) for numero in numeros]

# Encontrar el mayor y menor número en la lista
mayor = max(numeros)
menor = min(numeros)

# Mostrar los resultados
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
