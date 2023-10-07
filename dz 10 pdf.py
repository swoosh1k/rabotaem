def calculate(first, second, znak):
    if znak == '+':
        return f' вот ваша суммам{first  + second}'
    elif znak =='-':
        return f'вот ваша разность {first - second}'

    elif znak == '*':
        return f'вот результат умножения {first * second}'
    elif znak == '/':
        return f'вот результат деления {first / second}'

    elif znak == '^2':
        return first ** 2
    elif znak == 'fac':
        factorial = int(input('введите значение факториала'))
        b = 1
        summa = 0
        for i in range(1, factorial + 1):
            b = b * i
            summa = summa + b
        return f'{summa} ваш факториал числа'

try:
    znak = input('введите значение вашего знака')
    first = int(input('введитье значение первое'))
    second = int(input('введите второе значение'))
except:
    print('вы ввели неправильное значение')


try:
    print(calculate(first, second, znak))

except:
    print('вы ввели неправильное значение и из за этого не запуститься ваша функция ')



#3 сделать свое исключение и подключить к try/except

class terminal:
    def vidachya(self, summa):
        self.obrabotka_card(summa)
        print(f'вот ваши денеги сэр, {summa}')



    def obrabotka_card(self, summa):
        if not self.proverka_card(summa):
            raise Exception('у вас карта заблокирована, мы не можем вам выдать ваши деньги')



    def proverka_card(self, summa):
        return False

card1 = terminal()
try:
    card1.vidachya(2000)

except:
    print('ваша карта заблокирована ')