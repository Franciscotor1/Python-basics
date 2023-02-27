# Inicializar una variable para almacenar la suma
suma = 0

# Usar un bucle while para pedir y sumar números
while True:
    # Pedir un número al usuario
    numero = input("Introduce un número para sumar (o 'q' para salir): ")
    
    # Si el usuario introduce 'q', salir del bucle
    if numero == 'q':
        break
    
    # Convertir el número a un entero y sumarlo a la variable de suma
    suma += int(numero)

# Imprimir el resultado
print("La suma total es:", suma)