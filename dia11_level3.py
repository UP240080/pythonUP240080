#Level 3
#1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Escribe un numero: "))
if is_prime(n):
        print(f"{n} es un número primo.")
else :
    print(f"{n} no es un número primo.")


#2
def checking(lista):
    return len(lista) == len(set(lista))
    
mi_lista = [1, 2, 3, 5, 5]
if checking(mi_lista):
        print("Todos los elementos son únicos.")
else:
        print("Hay elementos repetidos en la lista.")

#3
def check_same_data(lst):
    if not lst:
        return 'No hay elementos'
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return 'Hay diferentes tipos de datos'
    return 'Todos los datos son del mismo tipo'
lst = [1, 2, 3, '4']
print(check_same_data(lst))

import keyword
#4
def is_valid_variable(name):
    if not name.isidentifier():
        return 'No es valido'
    if name in keyword.kwlist:
        return 'No es valido'
    if name[0].isdigit():
        return 'No es valido'
    return 'Es un nombre valido para una variable'
name = input("Escribe un nombre de variable: ")
print(is_valid_variable(name))

#5
#5.1
import keyword
from countries_data import paises
from collections import Counter
def most_popular_languages(dict):
    all_languages = [lang for country in dict for lang in country['languages']] 
    language_cout = Counter(all_languages)
    top10 = language_cout.most_common(10)
    return top10
print("Los 10 idiomas más populares son:")
print(most_popular_languages(paises))

#5.2
def most_populated_countries(dict):
    most_populated=[]
    top10_countries = sorted(dict, key=lambda x: x["population"], reverse=True)[:10]
    for country in top10_countries:
        most_populated.append(f"{country['name']} - {country['population']}")
    return most_populated
print("Los 10 países más poblados son:")
print(most_populated_countries(paises))