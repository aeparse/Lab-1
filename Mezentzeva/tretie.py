#Задание 3
from csv import reader

output = open('result.txt', 'w')

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[666:687]:
        output.write(f'{row[2]}. {row[1]} - {row[3]} \n')

output.close()
