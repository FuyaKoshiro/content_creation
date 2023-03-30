"""
==================
extract the all vtitle and vcode dataframe from the db.sqlite3
==================
"""


import sqlite3
import pandas as pd


class ExtractDB:

    def get_df(self):
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        c.execute("SELECT video_code, video_title FROM video_db")
        df = pd.DataFrame(c.fetchall(), columns=["vcode", "vtitle"])
        print(df)
        return df

if __name__ == "__main__":
    extract_db = ExtractDB()
    df = extract_db.get_df()