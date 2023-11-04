#Доп задание 5
from csv import reader

publishers = list()

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    headers = next(table)
    #Пропускаем строку с названием столбцов
    for row in list(table):
        publ = str(row[4])
        if publ not in publishers:
            publishers.append(publ)

print('Список всех издательств: \n', publishers)



