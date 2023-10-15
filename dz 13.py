#создать две тиблицы и обьеденить их инер джоином

import psycopg2

conn = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = '12345' ,port = '5432')
cur = conn.cursor()
cur.execute('''CREATE TABLE shop(id int PRIMARY KEY, name varchar NOT NULL);''')
cur.execute('''CREATE TABLE products(id int PRIMARY KEY, product_fish varchar(30), product_meat varchar(100),price int, fk_products_shops int REFERENCES shop(id));''')
cur.execute('''INSERT INTO shop(name) VALUES ('vitalur'), ('hippo'), ('evroopt')''')
cur.execute('''INSERT INTO products( product_fish,product_meat,price, fk_products_shops) VALUES ('semga', 'govyadina',1000, 2), ('skumbria','chicken',500, 1), ('forel', 'svinina', 450, 3)''')
cur.execute('''SELECT products.*, shop.name FROM products INNER JOIN shop ON shop.id = products.id''')
cur.execute('''SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products''')
conn.commit()
cur.close()
conn.close()