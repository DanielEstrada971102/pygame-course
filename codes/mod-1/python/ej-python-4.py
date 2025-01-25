print("Ingrese un número:")
numero = int(input())

mensaje = "El numero es "
complemento_1 = "negativo "
complemento_2 = "e impar"

if numero == 0:
    complemento_1 = "cero"
    complemento_2 = ""
else:
    if numero > 0:
        complemento_1 = "positivo "
    if numero % 2 == 0:
        complemento_2 = "y par"

print(mensaje + complemento_1 + complemento_2)
