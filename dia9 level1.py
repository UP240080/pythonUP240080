#1
edad = int(input("Introduce tu edad: "))
if edad < 18:
    faltante = 18 - edad
    print("Te faltan ", faltante, "años para ser mayor de edad y asi conducir legalmente")
else:
    print("Eres mayor de edad, puedes conducir legalmente")


#2
anio = int(input("Introduce tu edad: "))
mi_edad = 18
if anio > mi_edad:
    dif = anio - mi_edad
    if dif == 1:
        print("Eres ", dif, " año mas grande que yo")
    else:
        print("Eres ", dif, " años mas grande que yo")
elif anio < mi_edad:
    dif = mi_edad - anio
    if dif == 1:
        print("Soy ", dif, " año mas grande que tu")
    else:
        print("Soy ",dif, " años mas grande que tu")
else:
    print("Eres de la misma edad que yo")

#3
a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))

if a> b:
    print(a, " es mayor que ", b)
elif a < b:
    print(a, " es menor que ", b)
else:
    print(a, " es igual a ", b)