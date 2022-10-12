import sqlite3

con = sqlite3.connect("library.sqlite")

con.executescript('''
CREATE TABLE archive as
SELECT book_id, title , GROUP_CONCAT(author_name,', ') authors, available_numbers as lost
FROM book
JOIN book_author USING (book_id)
JOIN author USING (author_id)
WHERE available_numbers = 0
GROUP BY book_id;

INSERT INTO archive(book_id, title, authors, lost)
SELECT book_id, title, authors , COUNT(*) lost
FROM
(SELECT book_id, title , GROUP_CONCAT(author_name,', ') authors, available_numbers as lost
FROM book
JOIN book_author USING (book_id)
JOIN author USING (author_id)
WHERE available_numbers != 0
GROUP BY book_id)
JOIN book_reader USING (book_id)
WHERE return_date is null
GROUP BY book_id;

DELETE FROM book
WHERE available_numbers = 0;

UPDATE book
SET available_numbers = available_numbers - lost
FROM archive
WHERE book.book_id = archive.book_id
''')
con.commit()

con.close()
