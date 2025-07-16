#Level 3
#1

person={
    'nombre': 'Lizbeth',
    'apellido': 'Rodriguez',
    'edad': 18,
    'pais': 'Mexico',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'calle': 'Callejon de los tumbados',
        'codigo_postal': '99940'
    }
    }

if 'skills' in person:
    mitad = len(person['skills']) // 2
    print(person['skills'][mitad])
else:
    print("No hay skills en el diccionario.")

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python esta en la lista de skills")
else:
    print("No hay skills en el diccionario.")


if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print("El programador es front end developer")
    elif 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
        print("El programador es backend developer")
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("El programador es fullstack developer")
    else:
        print("Titulo no encontrado")
else:
    print("No hay skills en el diccionario.")


if person['is_marred'] == True and person['pais'] == 'Finlandia':
    print(person['nombre'], " esta casada y vive en ",person['pais'])
else:
    print(person['nombre'], " no esta casada y vive en ",person['pais'])