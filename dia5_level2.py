#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("Edad minima:", ages[0])
ages.sort(reverse = True)
print(ages)
print("Edad maxima = ", ages[0])
ages.append(ages[0])
ages.append(ages[-2])
print(ages)
ages.sort()
print(ages)
media = (ages[5] + ages[6])/2
print("Edad mediana: ",media)
prom = sum(ages) / len(ages)
print("Promedio: ",prom)
rango = ages[-1] - ages[0]
print("Rango: ", rango)
min = abs(ages[0] - prom)
print("Diferencia entre la edad minima y el promedio: ", min)
max = abs(ages[-1] - prom)
print("Diferencia entre la edad maxima y el promedio: ", max)
#2
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(paises)
print(paises[3])
#3
primera = paises[0:4]
print(primera)
segunda = paises[4:7]
print(segunda)
#4
#primeros paises 
print(paises[0])
print(paises[1])
print(paises[2])
#demas paises
print(paises[3:7])