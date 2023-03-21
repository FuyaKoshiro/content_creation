from video  import GetVideo
from script import Script
from gpt import Gpt
from translator import Translator
from html_page import Html
from update_db import UpdateDB
from extract_db import ExtractDB
from home_page_update import UpdateHome

import time

if __name__ == "__main__":
    gv = GetVideo()
    vcode_list = gv.get_vcode()
    vtitle_list = gv.get_vtitle()

    for i in range(len(vcode_list)):
        
        vcode = vcode_list[i]
        vtitle = vtitle_list[i]

        s = Script(vcode=vcode)
        script = s.get_script_string()
        vcode = s.vcode

        gpt = Gpt(script=script)
        phrase_list = gpt.get_phrases()

        #add translator
        tl = Translator(phrase_list=phrase_list)
        print("="*80, "\ntranslating...")
        meaning_list = tl.translate()
        print(f"meaning_list is {meaning_list}.")

        #need to update te words
        h = Html(phrase_list=phrase_list, meaning_list=meaning_list, vcode=vcode, v_title=vtitle)
        h.make_page()

    #add new videos' data to database
    udb = UpdateDB(vcode_list, vtitle_list)
    udb.insert_value()
    udb.check_progress()

    edb = ExtractDB()
    df = edb.get_df()

    #add home page updator
    uh = UpdateHome(df)
    uh.make_page()

    time.sleep(5)

    print("="*80, "\ndone")