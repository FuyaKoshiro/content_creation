# extract the all vtitle and vcode dataframe from the db.sqlite3
import sqlite3
import pandas as pd


class ExtractDB:
    def __init__(self):
        self.vtitle_list_all = []
        self.conn = sqlite3.connect("db.sqlite3")
        self.c = self.conn.cursor()
        self.df = None

    def get_df(self):
        self.c.execute("SELECT video_code, video_title FROM video_db")
        self.df = pd.DataFrame(self.c.fetchall(), columns=["vcode", "vtitle"])
        print(self.df)
        return self.df

if __name__ == "__main__":
    edb = ExtractDB()
    df = edb.get_df()