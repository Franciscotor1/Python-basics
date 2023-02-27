# OPERACIONES DE CONJUNTOS: UNION DE DOS CONJUNTOS O MÁS

set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}

set_c = set_a.union(set_b) #METODO UNION .union
print(set_c) # SE IMPRIME UNA NUEVA UNION
print(set_a | set_b) #TAMBIEN HACEN LA UNION DE LOS DOS SET

# INTERSECCIÓN

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# diferencias

#ELIMINA A LOS QUE SON REPETIDOS Y DEJA NORMAL AL CONJUNTO DE

countries = {"MX", "COL", "ARG", "USA"}
northAM = {"USA", "CANADA"}
centraLAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries.union(northAM, centraLAm, southAm)
print(new_set)

x =(1,2,3,4)
print(type(x))