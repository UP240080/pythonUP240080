#Level 2
#1
calificacion = int(input("Ingrese su calificación del 0 al 100: "))
if calificacion >= 90:
    print("Con ",calificacion, " su calificacion es A.")
elif calificacion >= 70:
    print("Con ",calificacion, " su calificacion es B.")
elif calificacion >= 60:
    print("Con ",calificacion, " su calificacion es C.")
elif calificacion >= 50:
    print("Con ",calificacion, " su calificacion es D.")
else:
    print("Con ",calificacion, " su calificacion es F.")

#2
mes = input("Ingrese el mes (con mayuscula al inicio): ")
if mes == "Diciembre" or mes == "Enero" or mes == "Febrero":
    print("En ",mes, " es invierno.")
elif mes == "Marzo" or mes == "Abril" or mes == "Mayo":
    print("En ",mes, " es primavera.")
elif mes == "Junio" or mes == "Julio" or mes == "Agosto":
    print("En ",mes, " es verano.")
elif mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre":
    print("En ",mes, " es otoño.")
else:
    print("Error")

#3
fruits = ['platano', 'naranja', 'mango', 'limon']

fruta = input("Ingrese una fruta: ")
if fruta in fruits:
    print("La fruta ", fruta, " está en la lista.")
else:
    fruits.append(fruta)
    print(fruits)