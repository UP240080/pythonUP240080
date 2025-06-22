#1
Dia = "Treinta"
Space = " "
dias = "Dias"
En = "En"
Py = "Python"
oracion = Dia + Space + dias + Space + En + Space + Py
print(oracion)
#2
Co = "Coding"
por = "For"
Todo = "All"
#3
Company = Co + Space + por + Space + Todo
#4
print(Company)
#5
print(len(Company))
#6
print(Company.upper())
#7
print(Company.lower())
#8
print(Company.capitalize())
print(Company.title())
print(Company.swapcase())
#9
print(Company.strip("Coding"))
#10
print(Company.index("Coding"))
print(Company.find("Coding"))
#11
print(Company.replace("Coding", "Python"))
#12
Eve = "Everyone"
Pyt = Py + Space + por + Space + Eve
print(Pyt)
print(Pyt.replace("Everyone","All"))
#13
print(Company.split())
#14
Go = "Google"
Face = "Facebook"
Micro = "Microsoft"
Apple = "Apple"
Ibm = "IBM"
Ora = "Oracle"
Ama = "Amazon"
Apps = Face + Space + Go + Space + Micro + Space + Apple + Space + Ibm + Space + Ora + Space + Ama
print(Apps.split())
#15
Com = Company[0]
print(Com)
#16
Ult = Company[12]
print(Ult)
#17
Va = Company[10]
print(Va)
#18 
Acro = Py[0] + por[0] + Eve[0]
print(Acro)
#19
Acro2 = Co[0] + por[0] + Todo[0]
print(Acro2)
#20
print(Company.index("C"))
#21
print(Company.index("F"))
#22
Personas = "People"
Sub_Company = Company + Space + Personas
print(Sub_Company.rfind("l"))
#23
Segunda_oracion = "You cannot end a sentence with because because because is a conjunction"
print(Segunda_oracion.find("because"))
#24
print(Segunda_oracion.rindex("because"))
#25
print(Segunda_oracion.replace(' because', ''))
#26
print(Segunda_oracion.index("because"))
#27
print(Segunda_oracion.replace(' because', ''))
#28
#cuando se habla de que la oracion Coding For All comienza con la subcadena Coding es correcto, incluso al ponerlo con el fin para encontrar posicion a este lo marca como el primero 
print(Company.find("Coding"))
#29
#Caso contrario aqui pues aun si uno quiero verlo como que esta al final, en la oraciòn sigue apareciendo al inicio, entonces coding no esta al final
print(Company.rfind("Coding"))
#30
Tri_Company = Space + Company + Space
print(Tri_Company)
print(Tri_Company.strip(" "))
#31
Uno =  "30DaysOfPython"
Dos = "thirty_days_of_python"
print(Uno.isidentifier()) #False, lo marca porque empieza por numero, cosa que no se puede
print(Dos.isidentifier()) #True, al iniciar con letras este es el correcto
#32
Lista =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(Lista)
print(" ".join(Lista))
#33
print("I am enjoying this challenge. \nI just wonder what is next.")
#34
print("Name    \tAge  \tCountry   \tCity")
print("Asabeneh\t250\tFinland   \tHelsinki")
#35
Radio = 10
area = 3.14 *Radio**2
formando = "The area of circle with a radius %d is %.2f." %(Radio, area)
print(formando)
#36
d = 8
f = 6
print('{} + {} = {}'.format(d, f, d + f))
print('{} - {} = {}'.format(d, f, d - f))
print('{} * {} = {}'.format(d, f, d * f))
print('{} / {} = {}'.format(d, f, d / f)) 
print('{} % {} = {}'.format(d, f, d % f))
print('{} // {} = {}'.format(d, f, d // f))
print('{} ** {} = {}'.format(d, f, d ** f))

