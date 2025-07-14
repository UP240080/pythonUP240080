#Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies)) 

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update(["Samsung", "Instagram", "HP"])
print(it_companies)

#4
it_companies.pop()
print(it_companies)

#5 La diferencia entre remove causa error y discard no.

#Level 2

#1
C = A.union(B)
print(C)

#2
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
print(A.union(B))
print(B.union(A))

#6
print(A.symmetric_difference(B))

#7
del A
del B

#Level 3

#1
ages_set = set(age)
print(ages_set)
print(len(age))
print(len(ages_set)) #La lista de edades es mas grande.

#2, las listas pueden cambiar y estan ordenadas, mientras que las tuplas no pueden cambiar, los conjuntos son cambiables y desordenados, mientras las cadenas son incambiables.

#3
oracion = "I am a teacher and I love to inspire and teach people"
palabras = oracion.split()
palabras_set = set(palabras)
print(palabras_set)