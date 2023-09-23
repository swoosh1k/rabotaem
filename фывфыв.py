import time

#1

function  = lambda x: 'число четное ' if x % 2 == 0  else 'число нечетное'
print(function(int(input('введите чило'))))



#2

s = list(map(lambda fry: str(fry), [1, 2, 3 ,4, 54, 54]))
print(s)




#3
def function_polidron(polidron):
    return polidron == polidron[::-1]



tolko = tuple(filter(function_polidron , ('привет как дела', 'как жизнь', 'шалаш', 'опрпо', 'аыда')))
print(tolko)









#4


import time
def feunction(functions_time):
    def wrapped():
       print('start')
       start = time.time()
       functions_time()
       end = time.time()
       result = end - start
       print(f'{result} время функции {functions_time}')
    return wrapped



@feunction
def time1():
    time.sleep(3)

@feunction
def rabota4():
    time.sleep(4)

time1()
rabota4()





#5

def decorator(original_function):
    def wrapper(k):
        tochka = '.'
        if  k[0] == '-' and tochka in k:
            print(f'{k} вы ввели отрицательное дробное число')
            return k
        elif tochka in k:
            print(f'вы ввели десятичную дробь {k}')
            return k
        elif k.isdigit:
            print('вы ввели целое положительное число')
            return k
        else:
            print('вы ввели некоректное число ')
    return wrapper



@decorator
def func(k):
    return k



k = input('введите значение')
func(k)







