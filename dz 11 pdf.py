import re


#2 СОздать генератор геометрической прогрессии
def geom_progress(q, bn ,n):
    for i in range(n):
        yield bn
        bn = bn * q



q = int(input('введите занчение q'))
bn = int(input('введите значение первого члена'))
n = int(input('введите количество членов '))
go = geom_progress(q, bn, n)
print(next(go))
print(next(go))
print(next(go))




#3Сдлеать функцию для проверки имэйла регуляркой
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")



isValid('artewmlozko4@gmaidl.com')


# Todo Метод re.compile() компилирует шаблон регулярного выражения в объект регулярного выражения.
#  В основном он используется из-за эффективности, когда мы планируем сопоставлять шаблон более одного раза.

