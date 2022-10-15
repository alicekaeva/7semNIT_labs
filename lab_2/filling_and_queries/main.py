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
''')
