def calcular_area(base, altura):
    return base * altura / 2

print("Ingrese la base del rectángulo:")
base = float(input())
print("Ingrese la altura del rectángulo:")
altura = float(input())
print(f"El área del rectángulo es: {calcular_area(base, altura)}")
