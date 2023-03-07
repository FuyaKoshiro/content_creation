from url  import Vcode
from script import Script
from gpt import Gpt
from html_page import Html


if __name__ == "__main__":
    u = Vcode()
    vcode_list = u.get_vcode()

    for vcode in vcode_list:
        s = Script(vcode=vcode)
        script = s.get_script_string()
        vcode = s.vcode

        g = Gpt(script=script)
        html = g.get_answer()

        hp = Html(html=html, vcode=vcode)
        html_page = hp.write_html()
