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
from datetime import datetime
import datetime




def vremya_43(k):
    spisoc = []
    result = [datetime.datetime.now() + datetime.timedelta(seconds=i) for i in range(0, k)]
    for j in range(0, len(result)):

        spisoc.append(datetime.datetime.strftime(result[j], '%Y-%m-%d %H %M %S'))
    return spisoc


k = int(input('введите количество дат'))
print(vremya_43(k))









