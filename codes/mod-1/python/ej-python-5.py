print("A continuación debe ingresar las calificaciones, cuando ya estén todas oprima ENTER...")
suma = 0
cantidad = 0

while True:
    calificacion = input()
    if calificacion == "":
        break
    suma += float(calificacion)
    cantidad += 1

promedio = suma / cantidad
print(f"El promedio es: {promedio}")
