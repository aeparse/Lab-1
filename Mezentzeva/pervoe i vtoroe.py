#Вариант 7
from csv import reader


flag = 0
count = 0
searchAuthor = input('Введите автора для поиска книг: ')
print('Найденные книги с 2001 по 2003 год: \n')

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    #Пропускаем строку с названием столбцов
    headers = next(table)

    for row in list(table):

        #Задание 1. Книги с названием длиннее 30
        if len(row[1]) >= 30:
            count +=1
        #Задание 2. Поиск книг по автору с 2001 до 2003 года
        #(числа в варианте были другими, но в этой таблице книги только до 2004 года)
        try:
        #Там есть неправильно заполненные строки, поэтому приходится делать доп проверку
            year = int(row[3])
            if 2001 <= year <= 2003:
                lower_caseAuthor = row[2].lower()
                indexAuthor = lower_caseAuthor.find(searchAuthor.lower())
                if indexAuthor != -1:
                    print(row[1])
                    flag = 1

        except ValueError:
            pass

if flag == 0:
    print('Книг не найдено.')

print('----------------------------')

#Вывод результатов задания 1
print('Книг с названием длиннее 30 символов: ',count)