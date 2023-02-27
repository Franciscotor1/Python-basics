numbers = []
for element in range(1, 11): # ITERACION  DE 1 HASTA 11 DENTRO DEL CICLO FOR
    numbers.append(element) #
    
    
    print(numbers)
    

    
    import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)

fruits = ["manzana", "banana", "kiwi", "pera"]
for fruit in fruits:
    print(fruit)
    
    n = 10
while n > 0:
    print(n)
    n -= 1
    

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("¡Guau! ¡Guau!")

# Creando un objeto a partir de la clase Perro
mi_perro = Perro("Fido", "Labrador")

# Llamando al método ladra() del objeto mi_perro
mi_perro.ladra()