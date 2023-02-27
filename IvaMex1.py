import math

print("Ingrese el nombre del producto")
p1 = input()
print("Cantidad comprada de ",p1)
p1_cant = int(input())
print("Valor o costo de la unidad de ",p1) 
p1_vu = int(input()) #vu: es igual a valor o costo de la unidad como entero
 
print("ingrese el nombre del segundo producto")
p2 = input()                        
print("cantidad comprada de ",p2)
p2_cant = int(input())
print("valor de la unidad de ",p2)
p2_vu = int(input())

print("ingrese el nombre del tercer producto")
p3 = input()
print("cantidad comprada de ",p3)
p3_cant = int(input())
print("valor o costo de la unidad de ",p3)
p3_vu = int(input())

p1_st = p1_cant * p1_vu
p2_st = p2_cant * p2_vu
p3_st = p3_cant * p3_vu

subtotal = p1_st + p2_st + p3_st
IVA = subtotal * 0.19
Total = subtotal + IVA

print("el total a pagar por ",p1, "es: ",p1_st)
print("el total a pagar por ",p2, "es: ",p2_st)
print("el total a pagar por ",p3, "es: ",p3_st)

print("El Iva mexicano fue: ",IVA)
print("El costo subtotal fue: ",subtotal)
print("el total es: ",Total)

