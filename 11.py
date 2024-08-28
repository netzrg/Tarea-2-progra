# Solicitar un número entero al usuario
numero = input("Introduce un número entero: ")

# Sumar los dígitos del número
suma_digitos = sum(int(digito) for digito in numero)

# Mostrar el resultado
print(f"La suma de los dígitos es: {suma_digitos}")
