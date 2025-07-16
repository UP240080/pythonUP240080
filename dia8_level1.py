#1
Dog = {}

#2
Dog['name'] = 'Yanki'
Dog['color'] = 'black'
Dog['raza'] = 'husky'
Dog['legs'] = 4
Dog['age'] = 3
print(Dog)

#3
student = {
    'name' : 'Lizbeth',
    'Last_name' : 'Rodriguez',
    'genero' : 'Femenino',
    'age' : 19,
    'marital_status' : 'En relacion',
    'hobbies' : ['Jugar videojuegos', 'leer', 'ver series y anime'],
    'country' : 'Mexico',
    'city' : 'Apozol',
    'address' : 'Callejon de los tumbados'
    }

print(student)

#4
print(len(student))

#5
print(student['hobbies'])
print(type(student['hobbies']))

#6
student['hobbies'].append('Jugar con sus mascotas')
student['hobbies'].append('Escuchar musica')
print(student['hobbies'])

#7
inicio = student.keys()
print(inicio)

#8
fin = student.values()
print(fin)

#9
tup = tuple(student.items())
print(tup)

#10
del Dog['legs']
print(Dog)

#11
del Dog
