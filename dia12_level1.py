#Level 1
#1
import random
import string
def random_user_id():
    caracteres = string.ascii_letters + string.digits
    random_user_id = ''.join((random.choice(caracteres)) for _ in range(6))
    return random_user_id
print('User ID:', random_user_id())

#2
def user_id_gen_by_user():
    caracteres = string.ascii_letters + string.digits
num_caracteres = int(input('Ingrese el número de caracteres que quiere en su usuario: '))
num_IDs = int(input('¿Cuántas opciones quieres? '))
    
def generate_random_user():
        caracteres = string.ascii_letters + string.digits
        return ''.join((random.choice(caracteres)) for _ in range(num_caracteres))
    
for i in range(num_IDs):
        random_user_id = generate_random_user()
        print("Random User ID:")
        print(random_user_id)

#3
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)
random_rgb = rgb_color_gen()
print("Random RGB Color:", random_rgb)