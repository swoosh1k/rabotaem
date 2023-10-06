import time
#1, 2 , 3, 4
#создать свой класс данных
from dataclasses import dataclass
@dataclass
class worker:

    job: str
    age = 23
    name: str
    @classmethod     # добавить классметод
    def age1(cls):
        i = 0
        k = int(input('введите количество которое вы хотите чтобы ваш возраст увеличевался '))
        while i < k:
            i = i + 1
            cls.age = cls.age + 1
            if i == k:
                stop = (f'stop, ващ возраст примерно будет таким вот  {cls.age}')
                time.sleep(1)
                print('щас проверю все ли хорошо тут')
                time.sleep(1)
                print('да все четко впринципе')
                time.sleep(1)
                return stop
    @staticmethod #добавить статикметод
    def static():
        k = 10
        print('процесс закончился, можем идти дальше')
        g = k ** 10
        print(g)

#4 создать метакласс

meta = type('classAcccount', (), {'name': 'artem', 'surname': 'lozko'})
b = meta()
print(b.name)


# это был простейший пример метакеласса
# также мы можем его создать использую лямбда функцию

meta2 = type('qwerty', (), {'name': 'artem', 'yt': 10 , 'method1': lambda self : self.yt ** self.yt * 10})

c = meta2()
print(c.method1())
