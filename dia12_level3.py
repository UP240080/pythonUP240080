#Level 3
#1
import random
def shuffle_list(lst):
    r_lst = lst[:]
    random.shuffle(r_lst)
    return r_lst
print('Lista original:', list(range(1, 11)))

#2
def random_num():
    lst_random_num = set()
    while len(lst_random_num) < 7:
        random_n = random.choice('123456789')
        lst_random_num.add(random_n)
    return list(lst_random_num)
print('Lista random de numeros: ',random_num())

