#create a database

import sqlite3

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)
          ''')
          
c.execute('''
          INSERT INTO products (product_id, product_name, price)

                VALUES
                (1,'Computer',800),
                (2,'Printer',200),
                (3,'Tablet',300),
                (4,'Desk',450),
                (5,'Chair',150)
          ''')                     

conn.commit()