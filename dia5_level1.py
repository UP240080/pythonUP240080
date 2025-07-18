#1
vacio = []
#2
Frutas = ["fresa", "platano", "manzana", "kiwi", "naranja", "sandia", "mango"]
#3
print(len(Frutas))
print(len(vacio))
#4
print(Frutas[0])
print(Frutas[3])
print(Frutas[6])
#5
mixed_data_types = ["Gaby", 18, 1.62, "soltera", "San Gerardo, 5207"]
#6
it_companies = ["Facebook"," Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7
print(it_companies)
#8
numero_companies = len(it_companies)
print(numero_companies)
#9
first, second, third, middle, fifth, sixth, last = it_companies
print(first)
print(middle)
print(last)
#10
it_companies[1] = "Instagram"
print(it_companies)
#11
it_companies.insert(2, "Twitter")
print(it_companies)
#12
it_companies.insert(4, "Samsung")
print(it_companies)
#13
mayus = [company.upper() for company in it_companies]
print(mayus)
#14
string = ["#; "]
print(it_companies + string)
#15
print('Twitter' in it_companies)
print('Snapchat' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse=True)
print(it_companies)
#18
primeras = it_companies[0:3]
print(primeras)
#19
del it_companies[-3::]
print(it_companies)
#20
del it_companies[2:4]
print(it_companies)
#21
it_companies.remove("Twitter")
print(it_companies)
#22
del it_companies[1:2]
print(it_companies)
#23
del it_companies[1:2]
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
print("Esta lista a sido eliminada")
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
nueva = front_end + back_end
print(nueva)
#27
full_stack = nueva.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)
