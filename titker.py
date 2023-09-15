#1

sentence = input("Введите предложение состоящее из двух слов: ")
words = sentence.split()
reversed_words = words[::-1]
znak = "!"
result = ' ! '.join(reversed_words)
final_sentence = znak + result + znak

print(final_sentence)


print('{}{}{}'.format(znak, result, znak))
print(f'{znak}{result}{znak}')




#2
imya = input('введите ваше имя')
age = int(input('введите ваш возраст'))
if age > 0 and age  < 10:
    print('привет, шкет', imya)
elif 10 < age < 18:
    print('как жизнь', imya)
elif age > 18 and age < 100:
    print('что желаете', imya)
elif age > 100:
    print(imya, 'вы лжете, столько не жиувут')
elif age < 0 or age == 0 or age != int:
    print('ошибка, повторите ввод ')



#4
sum = 0
n = int(input('введите число '))
for i in range(1, n+1):
    pr = i ** 3
    sum = sum + pr
    print(sum)



b = int(input('введите число'))
i = 0
sum = 0
while i < b:
    i = i + 1
    kub = i ** 3
    sum = kub + sum



    print(sum)













#5
import random
numb = random.randint(1,10)
popitka = 1
a = int(input('введите предпологаемое число '))
if a == numb:
    print('вы угадали с первого раза и с одной попытки')
while a != numb:
    a = int(input('введите предпологаемое число, вы не угадали '))
    popitka = popitka + 1
    if a < numb:
        print('загаданное число большле')
    elif a > numb:
        print('загаданное число меньше ')
    elif a == numb:
        print(f'вы угадали число {a} за {popitka} попыток')



#3
rt = 0
while rt < 6:
    imya = input('введите ваше имя')
    age = int(input('введите ваш возраст'))
    if age > 0 and age  < 10:
            print('привет, шкет', imya)
    elif 10 < age < 18:
            print('как жизнь', imya)
    elif age > 18 and age < 100:
            print('что желаете', imya)
    elif age > 100:
            print(imya, 'вы лжете, столько не жиувут')
    elif age < 0 or age == 0 or age != int:
            print('ошибка, повторите ввод ')
