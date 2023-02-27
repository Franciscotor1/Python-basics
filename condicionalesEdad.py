edad = int(input("ingrese su edad: "))
if(edad < 0):
    print("error: Ingresó una edad negativa")
elif(edad>=18):
    print("es mayor de edad")
    if(edad>=60):
        print("Hace parte de la tercera edad")
else:
    print("es menor de dad") 
       