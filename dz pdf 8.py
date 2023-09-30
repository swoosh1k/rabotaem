
#3
'''для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей по модулю,
 если радиусы равны
 ,то выводится точка класса Point'''


class Point:
    x = 8

class Circle:
    def __init__(self, r1, r2):
        self.radius1 = r1
        self.radius2 = r2
    def delta_dlin(self):
        P  = 3.14
        dlina_1 = self.radius1 * P * 2
        dlina_2 = self.radius2 * P * 2
        delta_dlin = abs(dlina_1) - abs(dlina_2)
        if abs(dlina_1) - abs(dlina_2) == 0:
                print(Point.x)
                return delta_dlin
        else:
            return delta_dlin


radius_pervu = int(input('введите значение первого радиуса'))
radius_vtory = int(input('введите значение второго радиуса'))
print(Circle(radius_pervu,radius_vtory).delta_dlin())













#1

'''Создать род класс auto, у которого есть атрибуты: brand, age, color, mark, weight
А также методы: move , birtday, stop. Методы move и стоп выводят сообщение на экран (move), (stop),
а birtday увеличивает атрибут age на 1. Атрибуты brand, age и марк являются обязательными при обьвленни обьекта.'''

import time

class auto:

    def __init__(self,  mark ,  weight,   color, brand = 'volvo', age = 35, maxload = 100):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
        self.maxload = maxload

    def __int__(self, max_load = 100):
        self.max_load = max_load


    def mover(self):
        print('attention!')



    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)
        print('load completed!')


    def move(self):
     print(f'{self.brand} движется')

    def stop(self):
        print(f'{self.brand} остановилась')

    def birtdday(self):
        self.age = self.age + 1
        return self.age



Car = auto('volvo', 'samsung', 1999)





#2
"""Создать два класса car  и truck , которые являются наследниками класса auto. Класс auto имеет дополнительный обязательный атрибут max load
. Переопределенный метод move перед появлением надписи move вывод надпись attention , его реализацию сделать при помощи оператора super . 
А также дополнительный метод load. При его вызове происходить пауза 1 сек, затем выдается сообщениен load и снова пауза 1 сек . Класс Car имеет 
дополнительный обязательный атрибут max_speed и при вызове метода move , после появление надписи move должна появиться надпись max_speed is <max_speed>
 Создать по 2 обьекта для каждого из классов car  и truck, проверитб все их методы и атрибуты    """


class Car(auto):
    def __init__(self,  brand, max_speed = '100'):
        self.max_speed = max_speed
        self.brand = brand
    def move(self):
        super().mover()
        print('maxspeed is', self.max_speed)
        print(f'{self.brand} движется')


class Truck(auto):
    def __init__(self,brand, max_speed='150', ):
        self.max_speed = max_speed
        self.brand = brand

    def move(self):
        super().mover()
        print('maxspeed is', self.max_speed)
        print(f'{self.brand} движется')





car1 = Car('lexus')

car1.move()


truck2 = Truck('ford')

truck2.move()


car1.load()

truck2.load()


car1.stop()

