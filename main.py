from url  import Vcode
from script import Script
from gpt import Gpt
from html_page import Html

import time
from tqdm import tqdm

if __name__ == "__main__":
    u = Vcode()
    vcode_list = u.get_vcode()

    for i in tqdm (range(len(vcode_list)), desc="Executing..."):
        
        vcode = vcode_list[i]

        s = Script(vcode=vcode)
        script = s.get_script_string()
        vcode = s.vcode

        g = Gpt(script=script)
        html = g.get_answer()

        hp = Html(html=html, vcode=vcode)
        html_page = hp.write_html()

        time.sleep(5)
