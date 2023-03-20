#create a database which containes titles and video codes.

import sqlite3

conn = sqlite3.connect('db.sqlite3') 
c = conn.cursor()

c.execute('''
          CREATE TABLE video_db
          ([video_code] TEXT PRIMARY KEY, [video_title] TEXT)
          ''')
          
c.execute('''
          INSERT INTO video_db (video_code, video_title)

                VALUES
                ("X7xOEez75B0", "What would happen if you lost your sense of touch? - Antonio Cataldo"),
                ("test_vcode1", "test_vtitle1"),
                ("test_vdode2", "test_vtitle2")
          ''')                     

conn.commit()