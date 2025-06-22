#1
Edad = 18
#2
Estatura_en_metros = 1.62
#3
Complejo = 3 + 4j

#4, Ahora vamos a calcular el area de un triangulo
Base = float(input("Escribe la longitud de la base "))
Altura = float(input("Escribe la longitud de la altura "))
Area_del_triangulo = Base * Altura * 0.5
print("El area del triangulo es: ",Area_del_triangulo)

#5, Perimetro del triangulo
Lado_a = float(input("Ingresa la longitud del primer lado "))
Lado_b = float(input("Ingresa la longitud del segundo lado "))
Lado_c = float(input("Ingresa la longitud del tercer lado "))
Perimetro = Lado_a + Lado_b + Lado_c
print("El perimetro del triangulo es de: ",Perimetro)

#6, Rectangulo
Largo = float(input("Escribe la longitud del largo de tu rectangulo "))
Ancho = float(input("Escribe la longitud del ancho de tu rectangulo "))
Area_Rectangulo = Largo * Ancho
Perimetro_Rectangulo = 2 * (Largo + Ancho)
print("El area del rectangulo es: ",Area_Rectangulo)
print("El perimetro del rectangulo es: ",Perimetro_Rectangulo)

#7, circulo
Radio = float(input("Ingresa la longitud del radio del circulo: "))
pi = 3.14
Area_circulo = pi * Radio**2
circunferencia = 2 * pi * Radio
print("El area de nuestro circulo es: ",Area_circulo)
print("La circunferencia de nuestro circulo es: ",circunferencia)

#8 Pendiente, interseccion x e interseccion y
#y = 2x -2
#y = mx + b
pendiente = 2
interseccion_y = -2
interseccion_x = -interseccion_y/pendiente
print("La pendiente es: ",pendiente)
print("La interseccion del eje y es: ",interseccion_y)
print("La interseccion del eje x es: ",interseccion_x)

#9, Pendiente y distancia euclidiana
#(2,2)  (6,10)
X1 = 2
Y1 = 2
X2 = 6
Y2 = 10
m = (Y2 - Y1)/ (X2 - X1)
distancia_e = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5
print("La pendiente entre los puntos es: ",m)
print("La distancia euclidiana entre los puntos es: ",distancia_e)

#10, comparar pendientes
if pendiente == m:
    print("Las pendientes son iguales")
else:
    print("Las pendientes no son iguales")
    print("Una mide ",pendiente," y la otra ",m)

#11, valor de y
x = float(input("ingresa un valor para x "))
y = x**2 +6*x + 9
print("El valor de y es: ",y)  #El valor de y no podra ser 0 por el simple hecho de que lo negativo se vuelve positivo

#12, longitud de python y dragon 
longitd_python = len("python")
longitud_dragon = len("dragon")
if longitd_python != longitud_dragon:
    print("Las longitudes no son iguales")
else:
    print("Las longitudes son iguales")

#13, on, and
str_Py = "Python"
str_Dr = "Dragon"
if "on" in str_Py and "on" in str_Dr:
    print("Hay on en las palabras Python y Dragon")

#14, comprobar
oracion = "I hope this course is not full of jargon"
if "jargon" in oracion:
    print("Se encontro jargon en la oracion")

#15, no hay
if "on" not in str_Dr and "on" not in str_Py:
    print("on no se encuentra en las palabras python y dragon")
else:
    print("Si se encuentra on en las palabras python y dragon")
    
#16, python a float y string
tamano = len("python")
C_float = float(tamano)
C_String = str(C_float)
print("EL conteo transformado a float es ",C_float)
print("Y este mismo transformado a string es ",C_String)

#17, par
numero = int(input("Ingresa un numero "))
Par = numero%2
if Par == 0:
    print(numero," es par")
else:
    print(numero," es impar")

#18, 7//3
residuo = 7//3
int_valor = int(2.7)
if residuo == int_valor:
    print("Los resultados son los mismos")
else:
    print("Los resultados no son los mismos")

#19, tipo 10 y "10"
primer_tipo = type(10)
Segundo_tipo = type("10")
if primer_tipo == Segundo_tipo:
        print("El 10 es del mismo tipo que '10' ")
else:
        print("El 10 no es del mismo tipo que'10' ")           

#20, int
valorint = int(9.8)
if valorint == 10:
        print("int(9.8) es igual a 10")
else:
        print("int(9.8) no es igual a 10")

#21, Salario
Horas = float(input("Ingresa las horas trabajadas: "))
Tarifa = float(input("Tarifa por hora: "))
Salario = Horas * Tarifa
print("EL salario es de: ",Salario)

#22, años vividos a segundos
Anio = float(input("Escribe los años vividos: "))
Segundos = Anio * 60 * 60 * 24 *365
print("Los segundos que ha vivido son: ",Segundos)

#23 Tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")