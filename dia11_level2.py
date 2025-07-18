#level 2
#1
def par_impa(num):
    pares = 0
    impares = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
num = int(input("Escribe un número positivo: "))
pares, impares = par_impa(num)
print(f"El número de pares es: {pares}")
print(f"El número de impares es: {impares}")

#1.1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "El factorial no está definido para números negativos."
    else:
        return n * factorial(n - 1)
n = int(input("Escribe un número para calcular su factorial: "))
print(f"El factorial de {n} es: {factorial(n)}")

#1.2

def is_empty(param):
    return not bool(param)

param = input("Escribe algo (o deja vacío): ")
if is_empty(param):
    print("El parámetro está vacío.")
else:
    print("El parámetro no está vacío.")

#1.3
def c_mean(lista):
    return sum(lista) / len(lista)
def c_median(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]
def c_mode(lista):
    from collections import Counter
    contador = Counter(lista)
    max_count = max(contador.values())
    modes = [num for num, count in contador.items() if count == max_count]
    return modes if len(modes) > 1 else modes[0]
def c_range(lista):
    return max(lista) - min(lista)
def c_variance(lista):
    mean = c_mean(lista)
    return sum((x - mean) ** 2 for x in lista) / len(lista)
def c_std(lista):
    return c_variance(lista) ** 0.5
data = [1,2,3,4,5,6,7,8,9,10]
mean = c_mean(data)
median = c_median(data)
mode = c_mode(data)
range_value = c_range(data)
variance = c_variance(data)
std_dev = c_std(data)
print("Media:", mean)
print("Mediana:", median)
print("Moda:", mode)
print("Rango:", range_value)
print("Varianza:", variance)
print("Desviación estándar:", std_dev)
