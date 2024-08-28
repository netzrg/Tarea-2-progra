# Solicitar un número al usuario
numero = int(input("Introduce un número: "))

# Verificar si el número es primo
if numero > 1:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
else:
    print(f"El número {numero} no es primo.")
