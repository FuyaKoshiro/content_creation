from script import Script
from gpt import Gpt
from html_page import Html


if __name__ == "__main__":
    url = input("input the url of the video and press enter:\n")

    s = Script(url=url)
    script = s.get_script_string()
    vcode = s.vcode

    g = Gpt(script=script)
    html = g.get_answer()

    hp = Html(html=html, vcode=vcode)
    html_page = hp.write_html()
    