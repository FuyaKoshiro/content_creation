"""
==================
recieve 1. a list of phrases, 2. a list of meaning of the phrases, 3. the video code, 4. the video title.
and return an html file.
==================
"""


class MakeHTML:

    def __init__(self, phrase_list, meaning_list, vcode, vtitle):
        self.phrase_list = phrase_list
        self.meaning_list = meaning_list
        self.vcode = vcode
        self.vtitle = vtitle

    #add data, url, and the title of the video to a table in a page
    def add_table_rows(self):
        html_table_rows = ""
        for i in range(len(self.phrase_list)):
            html_table_rows += f'<li class="table-row"> <div class="col col-1" data-label="Index">{str(i+1)}</div> <div class="col col-2" data-label="Phrase">{self.phrase_list[i]}</div> <div class="col col-3" data-label="Meaning">{self.meaning_list[i]}</div> </li>'
        html_page = f'<!DOCTYPE html> <html><head> <meta charset="UTF-8"> <title>My Website</title> <link rel="stylesheet" href="/static/css/video.css"> </head><body> <header> <h1>{self.vtitle}</h1> </header> <main> <div class="container"> <ul class="responsive-table"> <li class="table-header"> <div class="col col-1">No.</div> <div class="col col-2">Phrases</div> <div class="col col-3">Meaning</div> </li>{html_table_rows} </ul> </div> <div class="iframe-container"> <iframe width="560" height="315" src="https://www.youtube.com/watch?v={self.vcode}" frameborder="0" allowfullscreen></iframe> </div> </main> <footer> </footer> </body></html>'
        return html_page
    
    def make_html_page(self):
        html_table = self.add_table_rows()
        self.f = open(f'../web_dev/templates/{self.vcode}.html', 'w')
        self.f.write(html_table)
        self.f.close()


if __name__ == "__main__":
    phrase_list = ["Hello", "Good morning"]
    meaning_list = ["こんにちは", "おはようございます"]
    vcode = "X7xOEez75B0" #test but acutual video code
    v_title = "test title"
    make_html = MakeHTML(phrase_list=phrase_list, meaning_list=meaning_list, vcode=vcode, vtitle=v_title)
    make_html.make_html_page()