# Solicitar un número al usuario
numero = int(input("Introduce un número entre 1 y 20: "))

# Verificar que el número esté en el rango
if 1 <= numero <= 20:
    factorial = 1
    contador = 1

    # Calcular el factorial utilizando un ciclo while
    while contador <= numero:
        factorial *= contador
        contador += 1

    # Mostrar el resultado
    print(f"El factorial de {numero} es: {factorial}")
else:
    print("El número debe estar entre 1 y 20.")
