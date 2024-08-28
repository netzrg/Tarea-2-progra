import random

# Solicitar el número de números aleatorios a generar al usuario
n = int(input("Introduce cuántos números aleatorios quieres generar: "))

# Generar una lista de n números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(n)]

# Mostrar la lista generada
print(f"Los {n} números aleatorios generados son: {numeros_aleatorios}")
