"""
==================
recieve a pair of a video code and video title, and insert it to a database.
==================
"""


# insert the newly added videos' data into the database
import sqlite3


class UpdateDB:

    def __init__(self, vcode, vtitle, phrase_list, meaning_list):
        self.vcode = vcode
        self.vtitle = vtitle
        self.phrase_list = phrase_list
        self.meaning_list = meaning_list

    def insert_value_video(self):
        try:
            conn = sqlite3.connect("database.db")
            c = self.conn.cursor()
            c.execute("""
                            INSERT INTO videos (video_code, video_title)

                            VALUES ("{}", "{}")
                    """.format(self.vcode, self.vtitle))
            conn.commit()
            conn.close()

        except sqlite3.IntegrityError:
            print("values already exit in the database")

    def insert_value_video_vcode(self):
        for i in range(len(self.phrase_list)):
            phrase_id = self.vcode + str(i)
            try:
                conn = sqlite3.connect("database.db")
                c = conn.cursor()
                c.execute("""
                                INSERT INTO videos_{}(phrase_id, video_code, phrase, meaning)

                                VALUES ("{}", "{}", "{}", "{}")
                        """.format(self.vcode, phrase_id, self.vcode, self.phrase_list[i], self.meaning_list[i]))
                conn.commit()
                conn.close()
            except sqlite3.IntegrityError:
                print("values already exit in the database")


if __name__ == "__main__":
    vcode = "vcode1"
    vtitle = "vtitle1"
    udb = UpdateDB(vcode, vtitle)
    udb.insert_value()
    udb.check_progress()
