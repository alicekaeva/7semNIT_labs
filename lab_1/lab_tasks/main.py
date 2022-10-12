import sqlite3
import pandas as pd
con = sqlite3.connect("lib.sqlite")
cursor = con.cursor()

# con.executescript('''
#  CREATE TABLE IF NOT EXISTS genre(
#  genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
# name_genre VARCHAR(30)
#  );
#
# INSERT INTO genre (name_genre)
# VALUES
#  ('Роман'),
#  ('Приключения'),
# ('Детектив'),
# ('Поэзия'),
#  ('Лирика'),
# ('Фантастика'),
#  ('Фэнтези');
#  ''')

# Заполнение и создание таблиц

# con.executescript('''
#  CREATE TABLE IF NOT EXISTS publisher(
#  publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
# publisher_name VARCHAR(30)
#  );
#
#  INSERT INTO publisher (publisher_genre)
# VALUES
#  ('ЭКСМО'),
#  ('ДРОФА'),
# ('АСТ');
#  ''')

# con.executescript('''
#  CREATE TABLE IF NOT EXISTS book(
#  book_id INTEGER PRIMARY KEY AUTOINCREMENT,
# title VARCHAR(50),
# genre_id INT,
# publisher_id INT,
# year_publication INT,
# available_numbers INT,
# FOREIGN KEY (genre_id)  REFERENCES genre (genre_id) ON DELETE CASCADE,
# FOREIGN KEY (publisher_id)  REFERENCES publisher (publisher_id) ON DELETE CASCADE
#  );
#
#  INSERT INTO book (title, genre_id, publisher_id, year_publication, available_numbers)
# VALUES
# ('Мастер и Маргарита', 1, 2, 2014, 5),
# ('Таинственный остров', 2, 2, 2015, 10),
# ('Бородино', 4, 3, 2015, 12),
# ('Дубровский', 1, 2, 2020, 7),
# ('Вокруг света за 80 дней', 2, 2, 2019, 5),
# ('Убийства по алфавиту', 1, 1, 2017, 9),
# ('Затерянный мир', 2, 1, 2020, 3),
# ('Герой нашего времени', 1, 3, 2017, 2),
# ('Смерть поэта', 4, 1, 2020, 2),
# ('Поэмы', 4, 3, 2019, 5);
#  ''')
# con.commit()

# Выполнение запросов с параметрами

print('Вывести книги (указать их жанр), количество которых принадлежит интервалу от a \nдо b, включая границы (границы интервала передать в качестве параметра).')
a = int(input('Введите первую границу: '))
b = int(input('Введите вторую границу: '))
cursor.execute('''
 SELECT title, name_genre
 FROM
 genre
 JOIN book USING (genre_id)
 WHERE available_numbers >= :first and available_numbers <= :second
''', {"first": a, "second": b})
result = cursor.fetchall()
for item in result:
    print(f'Книга: {item[0]}\nЖанр: {item[1]}')

print("\n")
print('Вывести книги (указать их издательство), название которой состоит из одного \nслова, и книга издана после заданного года (год передать в качестве параметра).')
year = int(input('Введите год: '))
cursor.execute('''
 SELECT title, publisher_name
 FROM
 publisher
 JOIN book USING (publisher_id)
 WHERE book.year_publication > :year and title NOT LIKE "% %"
''', {"year": year})
result = cursor.fetchall()
for item in result:
    print(f'Книга: {item[0]}\nИздательство: {item[1]}')

print("\n")
print('Вычислить, сколько экземпляров книг каждого жанра \nпредставлены в библиотеке.Учитывать только книги, изданные после заданного года (год передать в качестве параметра).')
year = int(input('Введите год: '))
cursor.execute('''
 SELECT name_genre, SUM(available_numbers)
 FROM
 book
 JOIN genre USING (genre_id)
 WHERE book.year_publication > :year
 GROUP BY genre_id
''', {"year": year})
result = cursor.fetchall()
for item in result:
    print(f'Жанр: {item[0]}\nКоличество: {item[1]}')

#Pandas

df = pd.read_sql('''
 SELECT
 title AS Книга,
genre_id AS Жанр,
 publisher_id AS Издательство,
available_numbers AS Количество
 FROM book
 WHERE available_numbers > :amount
''', con, params={"amount": 3})

print("\n")
print(df)
print("\n")
print(df["Книга"])
print("\n")
print(df.loc[3])
print("\n")
print("Количество строк:", df.shape[0])
print("Количество столбцов:", df.shape[1])
print("\n")
print(df.dtypes.index)
print("\n")

#f-strings

publishers = ("АСТ", "ДРОФА")
df = pd.read_sql(f'''
 SELECT
 title AS Книга,
 publisher_name AS Издательство
 FROM publisher
 JOIN book USING (publisher_id)
 WHERE publisher_name in {publishers}  and  (year_publication >= 2016 and year_publication <= 2019)
''', con)
print(df)

con.close()
