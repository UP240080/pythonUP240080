#Level 1
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
filtered_list = [item for sublist in list_of_lists for item in sublist[0]]
print(filtered_list)

#3
numberss = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0, 11)]
print(numberss)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
filtered_countries = [[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)] in countries]
print('Nueva lista : ',filtered_countries)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': item[0][0].upper(), 'city': item[0][1].upper()} for item in countries]
print("El diccionario es: ",dict_list)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_names = [item[0][0] + " " + item[0][1] for item in names]
print("La lista de nombres es:", list_names)    

#7
pendiente = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
interseccion_y = lambda m, x1, y1: y1 - m * x1
x1, y1, x2, y2 = 1, 2, 3, 4
m = pendiente(x1, x2, y1, y2)
print('La pendiente es:', m)
b = interseccion_y(m, x1, y1)
print('La intersección es:', b)
