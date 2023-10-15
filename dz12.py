# TODO создать две таблицы в базе данных и связать их!
import psycopg2

conn = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = '12345' ,port = '5432')
cur = conn.cursor()
cur.execute('''CREATE TABLE students1(id serial PRIMARY key, book varchar(30), sex VARCHAR(30));''')
cur.execute('''CREATE TABLE students(id serial PRIMARY key, our_gtoups integer);''')
cur.execute('''INSERT INTO students1(book, sex) VALUES('gogol', 'man'), ('tolstoy', 'man'), ('chaikovski', 'man')''')
cur.execute('''INSERT INTO students(our_gtoups) VALUES(12), (1), (4)''')
cur.execute('''CREATE TABLE students_grop(students_id int REFERENCES students1(id), students_group int REFERENCES students(id), CONSTRAINT student_grop_pk PRIMARY KEY(students_id, students_group));''')
cur.execute('''INSERT INTO students_grop VALUES(1, 2), (1, 3), (2, 3)''')
conn.commit()
cur.close()
conn.close()
