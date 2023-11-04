#Доп задание 6
from csv import reader

print("Двадцать самых популярных книг: \n")
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    headers = next(table)
    table = list(table)
    sorted_table = (sorted(table, key=lambda x: int(x[5]), reverse=True))
    for row in sorted_table[:20]:
       print(row[1])
