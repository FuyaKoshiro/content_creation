#create a database which containes titles and video codes.

import sqlite3

conn = sqlite3.connect('db.sqlite3') 
c = conn.cursor()

c.execute('''
          CREATE TABLE video_db
          ([video_code] TEXT PRIMARY KEY, [video_title] TEXT)
          ''')                 

conn.commit()