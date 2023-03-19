from url  import GetVideo
from script import Script
from gpt import Gpt
from translator import Translator
from html_page import Html

import time
from tqdm import tqdm

if __name__ == "__main__":
    gv = GetVideo()
    vcode_list = gv.get_vcode()
    vtitle_list = gv.get_vtitle()

    for i in tqdm (range(len(vcode_list)), desc="Executing..."):
        
        vcode = vcode_list[i]

        s = Script(vcode=vcode)
        script = s.get_script_string()
        vcode = s.vcode

        g = Gpt(script=script)
        phrases_list = g.get_answer()

#add translator
        t = Translator(phrase_list=phrases_list)
        meaning_list = t.translate()

#need to update te words
        h = Html(phrase_list=phrases_list, meaning_list=meaning_list, vcode=vcode_list, v_title=vtitle_list)
        h.make_page()

        time.sleep(5)