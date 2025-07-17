#Level 1
#1
for i in range (11):
    print(i)

i=0
while i <= 10:
    print(i)
    i = i + 1

#2
for i in range(10, -1, -1):
    print(i)

x = 10
while x >= 0:
    print(x)
    x = x - 1

#3
w = '#'
while len(w) < 8:
    print(w)
    w = w + '#'

#4

z = 0
while z < 8:
    print('# # # # # # # #')
    z = z + 1

#5
numero = 0
while numero <= 10:
    print(numero,' x ',numero, ' = ', numero * numero)
    numero = numero + 1

#6
lst = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for item in lst:
    print(item) 
    print('-' *15)

#7
for i in range(101):
    if i % 2 == 0:
        print(i, 'es par')

#8
for i in range(101):
    if i % 2 != 0:
        print(i, 'es impar')
