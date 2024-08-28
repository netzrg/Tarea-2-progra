# Solicitar un número al usuario
numero = int(input("Introduce un número para generar su tabla de multiplicar: "))

# Generar la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
