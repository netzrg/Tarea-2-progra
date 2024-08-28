# Solicitar el valor de n al usuario
n = int(input("Introduce un número entre 1 y 50: "))

# Verificar que n esté en el rango
if 1 <= n <= 50:
    fibonacci = [0, 1]

    # Generar la secuencia de Fibonacci
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    # Mostrar los primeros n números de la secuencia
    print(f"Los primeros {n} números de la secuencia de Fibonacci son: {fibonacci[:n]}")
else:
    print("El número debe estar entre 1 y 50.")
