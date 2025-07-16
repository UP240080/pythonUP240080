#Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

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