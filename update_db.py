# insert the newly added videos' data into the database

import sqlite3

class UpdateDB:
    def __init__(self, vcode, vtitle):
        self.vcode = vcode
        self.vtitle = vtitle
        self.conn = sqlite3.connect("db.sqlite3")
        self.c = self.conn.cursor()

    def insert_value(self):
        self.c.execute("""
                        INSERT INTO video_db (video_code, video_title)

                        VALUES
                        (?, ?)
                """, (self.vcode, self.vtitle))
        self.conn.commit()
    
    def check_progress(self):
        self.c.execute("SELECT count(video_code) FROM video_db")
        result = self.c.fetchall()[0][0]
        print(f"the number of rows in the database: {result}")

if __name__ == "__main__":
    vcode = "vcode1"
    vtitle = "vtitle1"
    udb = UpdateDB(vcode, vtitle)
    udb.insert_value()
    udb.check_progress()
