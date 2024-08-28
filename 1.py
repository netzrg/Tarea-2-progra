# Inicializar la variable suma
suma = 0

# Sumar los números pares del 1 al 100
for numero in range(1, 101):
    if numero % 2 == 0:
        suma += numero

# Mostrar el resultado
print(f"La suma de los números pares del 1 al 100 es: {suma}")
