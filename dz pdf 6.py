#1

# TODO
'''Декорировать в строку байтовое значение(b'r\xc3\xa9sum\xc3\xa9'), затем результат преобразовать в байтовый вид
в виде кодировки'Latin' и затем результат снова декорировать в строку '''


b = b'r\xc3\xa9sum\xc3\xa9'
c = b.decode('utf-8')
print(c)
f = c.encode('Latin1')
print(f)
g = f.decode('Latin1')
print(g)


#2
'''ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные .
 Создать файл и записать в него первые 2 строки и закрыть файл . Затем открыть файл на редоктирование и дозаписать оставшиеся 2 строки .
  В итоговом файле должны быть 4 строки ,
каждая из которых должна начинатьсяс новой строки'''


first = input('введите первую строкуу')
second = input('введите вторую строку')
third = input('введите третью  строкуу')
fourth = input('введите четвертую строкуу')



with open(r'C:\Users\User\PycharmProjects\pythonProject3\будем записывать сюда.py', 'w' ,encoding='utf-8') as file:
    file.write(first + '\n')
    file.write(second + '\n')
    file.close()
with open(r'C:\Users\User\PycharmProjects\pythonProject3\будем записывать сюда.py', 'a', encoding= 'utf-8') as file:
    file.write(third + '\n')
    file.write(fourth  + '\n')
    file.close()



# 3
''' Создать словарь в качестве ключа которого будет 6 значное айди,
 а значение будет состоять из кортежа (имя , возраст) 
 Записать данный словарь на диск в json файл '''


import json
slovar = {
          'id: 456789': ('ярослав', 38),
          'id: 231890': ('дима', 20),
          'id: 456789': ('артем', 16),
          'id: 378908': ('даник', 22),
          'id: 809765': ('владимир', 46),
          'id: 232787': ('ева', 10)
          }
with open('slovar1.json', 'w', encoding='utf-8') as file1:
    file1.write(json.dumps(slovar, indent=4, ensure_ascii= False))




#4
'''Прочитать сохраеннный json-файл  и записать данные на диск в cvs-файл
 , первой строкой которого озоглавив каждый столбец
  и добавив новый столбец' телефон'''
import csv

with open('slovar1.json.', 'r') as file1, open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    slovar = json.load(file1)
    writer = csv.writer(csv_file)

    writer.writerow(['ID', 'Имя', 'Возраст', 'Телефон'])

    for id, (name, age) in slovar.items():
        writer.writerow([id, name, age, ''])




