#Level 2
#1
suma = 0
for i in range (101):
    suma = suma + i
    print(suma)
    i = i + 1

#2
suma_par = 0
suma_impar = 0
for i in range(101):
    if i % 2 == 0:
        suma_par = suma_par + i
        print(suma_par,' es la suma de los pares')
        i = i + 1
    else:
        suma_impar += i
        print(suma_impar,' es la suma de los impares')
        i = i + 1