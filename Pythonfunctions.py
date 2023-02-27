set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 445, 23}

set_types = {1, "hola", False, 12.12}
print(set_types)

set_from_string = set("hoola")
print(set_from_string)

set_from_tuples = set(("abc", "cbv", "as", "abc")) # los conjuntos no repiten (Se pueden modificar no tienen un orden No pueden tener elementos duplicados)
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)



