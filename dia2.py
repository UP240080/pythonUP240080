"Dia 2 de 30 días de programación en python"
Nombre = input("Escribe tu nombre")
Apellido=  input("Escribe tu apellido") 
Pais = input("Escribe tu país favorito")
Ciudad = input("Escribe tu ciudad favorita")
Edad = input("Escribe tu edad")
Anio = input("Escribe el año actual")
Casado = input("Estas casado?")
Verdad = input("¿Es verdad?")
Encendida = input("Esta la luz prendida?")
A,B,C = input("Escribe varios valores")
Nombre_completo = Nombre + Apellido

print(type(Nombre))
print(type(Apellido))
print(type(Nombre_completo))
print(type(Pais))
print(type(Ciudad))
print(type(Anio))
print(type(Casado))
print(type(Verdad))
print(type(Encendida))
print(type((A, B, C)))

#parte 2

Pi = 3.14
print(len(Nombre))
print(type(Pi))
print("longitud de nombre:",len(Nombre))
print("longitud del apellido:", len(Apellido))
num_uno, num_dos=5,4
total= num_uno + num_dos
resta= num_uno - num_dos
multipicacion= num_uno * num_dos
division= num_uno / num_dos
porciento= num_dos % num_uno
elevar= num_uno ** num_dos
floor_division=num_uno // num_dos
radio=30
circumference= Pi * radio
circuferencia= 2 * Pi * radio
radio= float(input("ingresa el radio del circulo"))
circulo= Pi* radio ** 2

entrada = input('Escribe tu nombre, apellido, pais y edad')
print(entrada)