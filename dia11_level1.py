#level 1
#1
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(2 , 3))

#2
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle((float(input("Escribe el radio: ")))))

#3
def add_all_nums(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(add_all_nums(1, 2, 3, 4, 5))

#4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(float(input("Escribe la temperatura en Celsius: "))))

#5
def check_season(mes):
    if mes == "noviembre" or mes == "diciembre" or mes == "enero" or mes == "Novimbre" or mes == "Diciembre" or mes == "Enero":
        print("En ",mes, "es Invierno")
    elif mes == "febrero" or mes == "marzo" or mes == "abril" or mes == "Febrero" or mes == "Marzo" or mes == "Abril":
        print("En ",mes, "es Primavera")
    elif mes == "mayo" or mes == "junio" or mes == "julio" or mes == "Mayo" or mes == "Junio" or mes == "Julio":
        print("En ",mes, "es Verano")
    elif mes == "agosto" or mes == "septiembre" or mes == "octubre" or mes == "Agosto" or mes == "Septiembre" or mes == "Octubre":
        print("En ",mes, "es Otoño")
    else:
        print("Error")
        return check_season
print(check_season(input("Escribe el mes: ")))

#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        print("Error: division por cero")
    else:
        return (y2 - y1) / (x2 - x1)

x1 = float(input("Escribe el valor de x1: "))
y1 = float(input("Escribe el valor de y1: "))
x2 = float(input("Escribe el valor de x2:  "))
y2= float(input("Escribe el valor de y2: "))
slope = calculate_slope(x1, y1, x2, y2)
print("La pendiente de la ecuacion lineal es:", slope)

#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Una solución: x = {x}"
    else:
        x1 = (-b + (discriminant)**(0.5)) / (2*a)
        x2 = (-b - (discriminant)**(0.5)) / (2*a)
        return f"Dos soluciones: x1 = {x1}, x2 = {x2}"

a = float(input("Escribe el valor de a: "))
b = float(input("Escribe el valor de b: "))
c = float(input("Escribe el valor de c: "))

resultado = solve_quadratic_eqn(a, b, c)
print("El conjunto de soluciones es:", resultado)

#8
def print_list(lista):
    for item in lista:
        print(item)
my_lista = ["Juego del calamar", "Sweet Home", "La gloria", "JJBA", "Los diarios de la boticaria"]

print(print_list(my_lista))

#9
def reverse_list(lista):
    reverse_lista= []
    for item in lista:
        reverse_lista.insert(0, item)
    return reverse_lista
my_lista = ["Juego del calamar", "Sweet Home", "La gloria", "JJBA", "Los diarios de la boticaria"]
print(reverse_list(my_lista))

#10
def capitalize_lista_items(lista2):
    capitalized_lista = []
    for item in lista2:
        capitalized_lista.append(item.upper())
    return capitalized_lista
my_lista2 = ["Juego del calamar", "Sweet Home", "La gloria", "JJBA", "Los diarios de la boticaria"]
print(capitalize_lista_items(my_lista2))

#11
def add_item(lst, item):
    lst.append(item)
    return lst
my_lista = ["Juego del calamar", "Sweet Home", "La gloria", "JJBA", "Los diarios de la boticaria"]
print(add_item(my_lista, "Nuevo item"))


#12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
my_lista = ["Juego del calamar", "Sweet Home", "La gloria", "JJBA", "Los diarios de la boticaria"]
print(remove_item(my_lista, "JJBA"))

#13
def suma_numeros(num):
    total = 0
    for i in range(0, num + 1):
        total += i
    return total
print(suma_numeros(5))
print(suma_numeros(10))
print(suma_numeros(100))

#14
def suma_numeros_impares(num):
    total = 0
    for i in range(0, num + 1):
        if i % 2 != 0:
            total += i
    return total
print(suma_numeros_impares(5))
print(suma_numeros_impares(10))
print(suma_numeros_impares(100))

#15
def suma_numeros_pares(num):
    total = 0
    for i in range(0, num + 1):
        if i % 2 == 0:
            total += i
    return total
print(suma_numeros_pares(5))
print(suma_numeros_pares(10))
print(suma_numeros_pares(100))