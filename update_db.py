"""
==================
recieve a pair of a video code and video title, and insert it to a database.
==================
"""


# insert the newly added videos' data into the database
import sqlite3


class UpdateDB:

    def __init__(self, vcode, vtitle):
        self.vcode = vcode
        self.vtitle = vtitle
        self.conn = sqlite3.connect("db.sqlite3")
        self.c = self.conn.cursor()

    def insert_value(self):
        try:
            self.c.execute("""
                            INSERT INTO video_db (video_code, video_title)

                            VALUES
                            (?, ?)
                    """, (self.vcode, self.vtitle))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("values already exit in the database")


if __name__ == "__main__":
    vcode = "vcode1"
    vtitle = "vtitle1"
    udb = UpdateDB(vcode, vtitle)
    udb.insert_value()
    udb.check_progress()
