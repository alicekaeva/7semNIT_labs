import sqlite3

con = sqlite3.connect("journal.sqlite")

# con.executescript('''
# CREATE TABLE IF NOT EXISTS genre(
#     genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     genre_name VARCHAR(30)
# );
#
# CREATE TABLE IF NOT EXISTS issue(
#     issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     issue_name VARCHAR(30),
#     deadline DATE
# );
#
# CREATE TABLE IF NOT EXISTS article(
#     article_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     article_name VARCHAR(30),
#     genre_id INTEGER,
#     FOREIGN KEY (genre_id) REFERENCES genre (genre_id) ON DELETE CASCADE
# );
#
# CREATE TABLE IF NOT EXISTS worker(
#     worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     worker_name VARCHAR(45)
# );
#
# CREATE TABLE IF NOT EXISTS work(
#     work_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     work_name VARCHAR(45)
# );
#
# CREATE TABLE IF NOT EXISTS work_worker(
#     work_worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     worker_id INTEGER,
#     work_id INTEGER,
#     FOREIGN KEY (worker_id) REFERENCES worker (worker_id) ON DELETE CASCADE,
#     FOREIGN KEY (work_id) REFERENCES work (work_id) ON DELETE CASCADE
# );
#
# CREATE TABLE IF NOT EXISTS issue_article(
#     issue_article_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     issue_id INTEGER,
#     article_id INTEGER,
#     FOREIGN KEY (issue_id) REFERENCES issue (issue_id) ON DELETE CASCADE,
#     FOREIGN KEY (article_id) REFERENCES article (article_id) ON DELETE CASCADE
# );
#
# CREATE TABLE IF NOT EXISTS issue_article_work(
#     issue_article_work_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     issue_article_id INTEGER,
#     work_worker_id INTEGER,
#     responsible_for_work_id INTEGER,
#     start_date DATE,
#     end_date DATE,
#     FOREIGN KEY (issue_article_id) REFERENCES issue_article (issue_article_id) ON DELETE CASCADE,
#     FOREIGN KEY (work_worker_id) REFERENCES work_worker (work_worker_id) ON DELETE CASCADE,
#     FOREIGN KEY (responsible_for_work_id) REFERENCES worker (worker_id) ON DELETE CASCADE
# );
#
# INSERT INTO genre(genre_name) VALUES
# ('Мода'),
# ('Отношения'),
# ('Путешествия'),
# ('Домашние животные'),
# ('Уход за собой'),
# ('Политика'),
# ('Искусство'),
# ('Наука'),
# ('Экономика');
#
# INSERT INTO article(article_name, genre_id) VALUES
# ('Откуда взялись звезды? Новые технологии позволят ученым подробно изучить историю появления нашей галактики', 8),
# ('Не можете сохранить отношения? Вините во всем свою мать, советуют ученые', 2),
# ('Французский режиссер, классик "новой волны" Жан-Люк Годар умер путем эвтаназии', 7),
# ('Кто взорвал "Северный поток"? Европа расследует мегадиверсию на главном газопроводе из России', 9),
# ('Цепляние за партнера', 2),
# ('9 невероятных мест Восточной Европы, которые стоит посмотреть', 3),
# ('Можно ли собакам молоко и другие молочные продукты', 4),
# ('Как небанально одеться на свадьбу, если вы гость', 1),
# ('WISH ЛИСТ: КУПИТЬ ЖЕНСКИЙ ПИДЖАК', 1);
#
# INSERT INTO worker(worker_name) VALUES
# ('Петров Игорь Васильевич'),
# ('Яковлева Анастасия Александровна'),
# ('Мельников Эрик Сергеевич'),
# ('Лазарев Эльдар Георгиевич'),
# ('Логинов Юлиан Тимурович'),
# ('Самойлова Раиса Егоровна'),
# ('Смирнова Алиса Игоревна'),
# ('Емельянова Ксения Ильинична'),
# ('Никифоров Тимофей Михайлович'),
# ('Булгакова Милана Артёмовна');
#
# INSERT INTO work(work_name) VALUES
# ('Корректор'),
# ('Верстальщик'),
# ('Дизайнер'),
# ('Звукорежиссер'),
# ('Видеооператор'),
# ('Фотограф'),
# ('Копирайтер');
#
# INSERT INTO issue(issue_name, deadline) VALUES
# ('На все времена', '2022-08-26'),
# ('Жить здорово!', '2022-09-26'),
# ('А как быть дальше?', '2022-10-26');
#
# INSERT INTO work_worker(worker_id, work_id) VALUES
# (1, 4),
# (1, 5),
# (2, 7),
# (2, 1),
# (3, 6),
# (3, 4),
# (10, 3),
# (4, 3),
# (5, 7),
# (9, 1),
# (6, 2),
# (6, 6),
# (7, 7),
# (7, 2),
# (9, 4),
# (8, 5);
#
# INSERT INTO issue_article(issue_id, article_id) VALUES
# (1, 1),
# (1, 2),
# (1, 3),
# (2, 4),
# (2, 5),
# (2, 6),
# (3, 7),
# (3, 8),
# (3, 9);
#
# INSERT INTO issue_article_work(issue_article_id, work_worker_id, responsible_for_work_id, start_date, end_date) VALUES
# (1, 1, 5, '2022-08-14', NULL),
# (4, 2, 7, '2022-09-02', '2022-09-17'),
# (7, 3, 8, '2022-09-28', '2022-10-12'),
# (1, 4, 1, '2022-08-12', '2022-08-15'),
# (4, 5, 2, '2022-09-17', NULL),
# (7, 6, 10, '2022-09-29', NULL),
# (1, 7, 3, '2022-08-01', '2022-08-15'),
# (4, 8, 9, '2022-09-12', '2022-09-22'),
# (7, 9, 6, '2020-10-10', NULL),
# (1, 10, 2, '2022-07-27', '2022-08-13'),
# (4, 11, 7, '2022-09-01', '2022-09-23'),
# (7, 12, 1, '2022-10-08', '2022-10-09'),
# (1, 13, 3, '2022-07-28', '2022-08-07'),
# (4, 14, 4, '2022-09-29', '2022-10-12'),
# (5, 15, 10, '2022-09-12', '2022-09-17'),
# (2, 16, 5, '2022-08-18', NULL),
# (7, 1, 3, '2022-10-09', '2022-10-10'),
# (8, 2, 9, '2022-10-13', NULL),
# (2, 3, 5, '2022-08-07', '2022-08-23'),
# (5, 4, 10, '2022-09-12', '2022-09-19'),
# (7, 5, 4, '2022-10-01', '2022-10-09'),
# (2, 6, 1, '2022-07-30', '2022-08-03'),
# (5, 7, 2, '2022-09-02', '2022-09-14'),
# (9, 8, 7, '2022-10-09', NULL),
# (3, 9, 6, '2022-08-03', '2022-08-15'),
# (6, 10, 8, '2022-09-10', '2022-09-23'),
# (7, 11, 10, '2022-10-10', '2022-10-15'),
# (3, 12, 5, '2022-08-01', '2022-08-05'),
# (6, 13, 9, '2022-09-13', '2022-09-21'),
# (9, 14, 2, '2022-10-01', NULL),
# (3, 15, 3, '2022-07-30', '2022-08-15'),
# (6, 16, 7, '2022-09-10', '2022-09-25');
# ''')

cursor = con.cursor()

"""
Вывести активные работы в текущем месяце
"""

cursor.execute('''
SELECT worker_name, work_name, start_date, end_date
FROM issue_article_work
JOIN work_worker USING (work_worker_id)
JOIN worker USING (worker_id)
JOIN work USING (work_id)
WHERE strftime('%m', start_date) = strftime('%m', DATE())
ORDER BY start_date;
''')
result = cursor.fetchall()
for item in result:
    print(f'ФИО работника: {item[0]}\nРабота: {item[1]}\nНачал: {item[2]}\nЗакончил: {item[3]}\n')

"""
Вывести работников, которые выполняли определенную работу 
"""

work_type = input('Введите вид работы: ')
cursor.execute('''
SELECT worker_name, start_date, end_date
FROM issue_article_work
JOIN work_worker USING (work_worker_id)
JOIN worker USING (worker_id)
JOIN work USING (work_id)
WHERE work_name = :work_type and end_date IS NOT NULL
''', {'work_type': work_type})
result = cursor.fetchall()
for item in result:
    print(f'ФИО работника: {item[0]}\nНачал: {item[1]}\nЗакончил: {item[2]}\n')

"""
Вывести опубликованные статьи определеннего жанра и названия выпусков, содержащих эти статьи
"""

genre = input('Введите жанр: ')
cursor.execute('''
SELECT DISTINCT article_name, issue_name
FROM article
JOIN genre USING (genre_id)
JOIN issue_article USING (article_id)
JOIN issue_article_work USING (issue_article_id)
JOIN issue USING (issue_id)
WHERE genre_name = :genre AND issue_article_id NOT IN ( SELECT issue_article_id
                                                        FROM issue_article_work
                                                        WHERE end_date IS NULL);
''', {'genre': genre})
result = cursor.fetchall()
for item in result:
    print(f'Статья: {item[0]}\nВыпуск: {item[1]}\n')
