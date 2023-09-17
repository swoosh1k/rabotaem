#2
import datetime


def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr = i * pr
    return pr

print(factorial(4))




#1
first_dict = {
    'рука': 'нога',
    'нос': 'палец',
    'спина': 'бицепс',
}

second_dict = {
    value: key for key, value in first_dict.items()
}
print(second_dict)






#3


def calculate_count1(lst):
    slovar = {}
    for item in lst:
        if item in slovar:
            slovar[item] = 1 + slovar[item]
        else:
            slovar[item] = 1

    return slovar





spisoc = [1, 23, 23, 45, 45, 65, 65, 67 ,67 ,68, 69, 68 , 1 ,2 ,3 ,1, 1, 2, 3, 4, 4 ,5,  6, 5 ,6 ]
result = calculate_count1(spisoc)
for item, count in result.items():
    if count > 1:
        print(f'элемент {item} встречается {count} раз')



















#4

import datetime

def vremya(k):

    date_now = datetime.datetime.now()
    date_1 = datetime.timedelta(seconds=1)
    for i in range(1, k):
        date_now = date_now + date_1
        print(date_now)


    return date_now + date_1





k = int(input('введите количество дат'))
ne_spisoc_a_prosto = vremya(k)
print(ne_spisoc_a_prosto)








