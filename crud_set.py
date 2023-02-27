# conjuntos con add, remove, len


set_countries = {"col", "mex", "bol"} #conjunto

size = len(set_countries)
print(size) #metodo para medir la longitud de una secuencia

print("col" in set_countries)
print("pe" in set_countries)

# add

set_countries.add("pe")
print(set_countries)

# update
set_countries.update({"ar", "ecua", "pe"})
print(set_countries)

# remove, eloiminacion

set_countries.clear()
print(set_countries)
print(len(set_countries))




