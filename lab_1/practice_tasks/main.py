import sqlite3
import pandas as pd

con = sqlite3.connect("library.sqlite")
cursor = con.cursor()
cursor.execute('''SELECT genre_name, COUNT(title), COUNT(return_date), MIN(year_publication)
FROM genre
JOIN book USING (genre_id)
JOIN book_reader USING (book_id)
WHERE return_date is not null
GROUP BY genre_id
ORDER BY genre_name'''
               )
result = cursor.fetchall()
for item in result:
    print(
        f'Жанр: {item[0]}\nКниг этого жанра представлено в библиотеке: {item[1]}\nКоличество доступных экзмепляров книг: {item[2]}\nСамый ранний год издания книги этого жанра: {item[3]}')

print("\n")
reader = input('Введите читателя: ')
cursor.execute('''
 SELECT title, borrow_date, return_date, (CASE WHEN return_date is null THEN 'Книга еще на руках' ELSE CAST(JULIANDAY(return_date) - JULIANDAY(borrow_date) AS int) END) as 'days'
 from book
 JOIN book_reader USING (book_id)
 JOIN reader USING (reader_id)
 WHERE reader_name = :reader
ORDER BY days DESC
''', {"reader": reader})
result = cursor.fetchall()
for item in result:
    print(
        f'Название книги: {item[0]}\nДата выдачи: {item[1]}\nДата сдачи: {item[2]}\nКоличество дней книга была на руках: {item[3]}')

print("\n")
cursor.execute('''SELECT genre_name,MAX(amount) 
FROM (SELECT genre_name, COUNT(book_id) amount
FROM genre
JOIN book USING (genre_id)
JOIN book_reader USING (book_id)
GROUP BY genre_id
ORDER BY genre_name)
'''
               )
result = cursor.fetchall()
for item in result:
    print(f'Жанр: {item[0]}\nСколько раз брали читатели: {item[1]}')

print("\n")
df = pd.read_sql('''
 SELECT
 title AS Название,
 reader_name AS Читатель,
 borrow_date AS Дата
 FROM book
 JOIN book_reader USING (book_id)
 JOIN reader USING (reader_id)
 WHERE borrow_date LIKE '%-10-%'
 ORDER BY borrow_date, reader_name, title
''', con)
print(df)

print("\n")
publisher = input("Введите издательство: ")
df = pd.read_sql('''
 SELECT
 title AS Название,
(CASE
            WHEN year_publication < 2014
                THEN 'III' 
            WHEN year_publication >= 2014 and year_publication <= 2017
                THEN 'II'
            WHEN year_publication > 2017
                THEN 'I'
       END) AS Группа
 FROM book
 JOIN publisher USING (publisher_id)
 WHERE publisher_name = :publisher
''', con, params={"publisher": publisher})
print(df)

print("\n")
df = pd.read_sql('''
 SELECT
 title AS Название,
 genre_name AS Жанр,
 year_publication AS Год,
(CASE
            WHEN year_publication < 2014
                THEN 'III' 
            WHEN year_publication >= 2014 and year_publication <= 2017
                THEN 'II'
            WHEN year_publication > 2017
                THEN 'I'
       END) AS Группа
 FROM book
JOIN genre USING (genre_id)
 JOIN publisher USING (publisher_id)
 WHERE publisher_name = :publisher
 ORDER BY Группа DESC, year_publication, title
''', con, params={"publisher": publisher})
print(df)

print("\n")
df = pd.read_sql('''
 SELECT
 title AS Название,
 available_numbers AS Количество,
 COUNT(borrow_date) AS Количество_выдачи
 FROM book
 LEFT JOIN book_reader USING (book_id)
 GROUP BY book_id
 ORDER BY Количество_выдачи DESC, title, Количество
''', con)
print(df)

con.close()
