#Level 1
#1
tupla = tuple()
#2
Hermanos = ("Edgar", "Juan", "Manuel", "Isaid")
Hermanas = ("Lizbeth", "Leslie", "Montserrat", "Dayana")
print(Hermanos)
print(Hermanas)
#3
Siblings = Hermanos + Hermanas
print(Siblings)
#4
print("Tengo ",len(Siblings)," Hermanos y hermanas (Imaginarios)")
#5
Miembros_de_la_familia = list(Siblings)
Miembros_de_la_familia.append("Jose Manuel")
Miembros_de_la_familia.append("Veronica")
print(Miembros_de_la_familia)

#Level 2
#1
Padres = Miembros_de_la_familia[-2:]
print("Padres: ",Padres)
print("Hermanos: ",Siblings)
#2
Frutas = ("Manzana", "Pera", "Naranja", "Sandia")
Verduras = ("Lechuga", "Cebolla", "Ajo", "Zanahoria")
Productos_animales = ("Carne", "Huevo", "Leche", "Queso")
food_stuff = Frutas + Verduras + Productos_animales
print(food_stuff)
#3
food_stuff_it = list(food_stuff)
#4
del food_stuff_it[5:7]
print(food_stuff_it)
#5
del food_stuff_it[0:3]
print(food_stuff_it)
del food_stuff_it[-1] 
del food_stuff_it[-1] 
del food_stuff_it[-1]
print(food_stuff_it)
#6
tuple(food_stuff_it)
del food_stuff_it
print("food_stuff_it ha sido eliminado")
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)