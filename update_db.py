# insert the newly added videos' data into the database

import sqlite3

class UpdateDB:
    def __init__(self, vcode_list, vtitle_list):
        self.vcode_list = vcode_list
        self.vtitle_list = vtitle_list
        self.conn = sqlite3.connect("db.sqlite3")
        self.c = self.conn.cursor()

    def insert_value(self):
        for i in range(len(self.vcode_list)):
            self.c.execute("""
                            INSERT INTO video_db (video_code, video_title)

                            VALUES
                            (?, ?)
                    """, (self.vcode_list[i], self.vtitle_list[i]))

        self.conn.commit()
    
    def check_progress(self):
        result = self.c.execute("""
        SELECT count(video_code) FROM video_db
        """)
        result = self.c.fetchall()[0][0]
        print(f"the number of rows in the database: {result}")

if __name__ == "__main__":
    vcode_list = ["vcode1", "vcode2"]
    vtitle_list = ["vtitle1", "vtitle2"]
    udb = UpdateDB(vcode_list, vtitle_list)
    udb.insert_value()
    udb.check_progress()
