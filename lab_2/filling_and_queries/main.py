import sqlite3

con = sqlite3.connect("journal.sqlite")

con.executescript('''
CREATE TABLE IF NOT EXISTS genre(
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS issue(
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_name VARCHAR(30),
    deadline DATE
);

CREATE TABLE IF NOT EXISTS article(
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_name VARCHAR(30),
    genre_id INTEGER,
    FOREIGN KEY (genre_id) REFERENCES genre (genre_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS worker(
    worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_name VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS work(
    work_id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_name VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS work_worker(
    work_worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER,
    work_id INTEGER,
    FOREIGN KEY (worker_id) REFERENCES worker (worker_id) ON DELETE CASCADE,
    FOREIGN KEY (work_id) REFERENCES work (work_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS issue_article(
    issue_article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_id INTEGER,
    article_id INTEGER,
    FOREIGN KEY (issue_id) REFERENCES issue (issue_id) ON DELETE CASCADE,
    FOREIGN KEY (article_id) REFERENCES article (article_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS issue_article_work(
    issue_article_work_id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_article_id INTEGER,
    work_worker_id INTEGER,
    responsible_for_work_id INTEGER,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (issue_article_id) REFERENCES issue_article (issue_article_id) ON DELETE CASCADE,
    FOREIGN KEY (work_worker_id) REFERENCES work_worker (work_worker_id) ON DELETE CASCADE,
    FOREIGN KEY (responsible_for_work_id) REFERENCES worker (worker_id) ON DELETE CASCADE
);

INSERT INTO genre(genre_name) VALUES
('Мода'),
('Отношения'),
('Путешествия'),
('Домашние животные'),
('Уход за собой'),
('Политика'),
('Искусство'),
('Наука'),
('Экономика');

INSERT INTO article(article_name, genre_id) VALUES
('Откуда взялись звезды? Новые технологии позволят ученым подробно изучить историю появления нашей галактики', 8),
('Не можете сохранить отношения? Вините во всем свою мать, советуют ученые', 2),
('Французский режиссер, классик "новой волны" Жан-Люк Годар умер путем эвтаназии', 7),
('Кто взорвал "Северный поток"? Европа расследует мегадиверсию на главном газопроводе из России', 9),
('Цепляние за партнера', 2),
('9 невероятных мест Восточной Европы, которые стоит посмотреть', 3),
('Можно ли собакам молоко и другие молочные продукты', 4),
('Как небанально одеться на свадьбу, если вы гость', 1),
('WISH ЛИСТ: КУПИТЬ ЖЕНСКИЙ ПИДЖАК', 1);

INSERT INTO worker(worker_name) VALUES
('Петров Игорь Васильевич'),
('Яковлева Анастасия Александровна'),
('Мельников Эрик Сергеевич'),
('Лазарев Эльдар Георгиевич'),
('Логинов Юлиан Тимурович'),
('Самойлова Раиса Егоровна'),
('Смирнова Алиса Игоревна'),
('Емельянова Ксения Ильинична'),
('Никифоров Тимофей Михайлович'),
('Булгакова Милана Артёмовна');

INSERT INTO work(work_name) VALUES
('Корректор'),
('Верстальщик'),
('Дизайнер'),
('Звукорежиссер'),
('Видеооператор'),
('Фотограф'),
('Копирайтер');

INSERT INTO issue(issue_name, deadline) VALUES
('На все времена', '2022-10-09'),
('Жить здорово!', '2022-11-09'),
('А как быть дальше?', '2023-01-01');

INSERT INTO work_worker(worker_id, work_id) VALUES
(1, 4),
(1, 5),
(7, 6),
(10, 7),
(8, 2),
(6, 1),
(8, 3);

INSERT INTO issue_article(issue_id, article_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(1, 4),
(3, 5),
(2, 6),
(1, 7),
(3, 8),
(1, 9);

INSERT INTO issue_article_work(issue_article_id, work_worker_id, responsible_for_work_id, start_date, end_date) VALUES 
(2, 1, 2, '2022-10-15', '2022-10-31'),
(3, 3, 7, '2022-12-02', NULL),
(5, 6, 3, '2022-12-01', '2022-12-14'),
(7, 4, 9, '2022-09-25', '2022-10-01'),
(7, 2, 8, '2022-09-15', '2022-09-29'),
(1, 5, 10, '2022-10-01', NULL),
(8, 1, 2, '2022-10-29', NULL),
(4, 4, 1, '2022-10-03', NULL),
(5, 7, 4, '2022-12-13', '2022-12-22'),
(9, 7, 9, '2022-10-05', NULL),
(6, 3, 10, '2022-10-26', '2022-11-05'),
(1, 2, 3, '2022-10-01', '2022-10-05'),
(8, 3, 5, '2022-11-15', '2022-11-29');
''')
