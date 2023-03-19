#recieve the html table compoent
#embed the table into the html template
#add css and javascript template
#return the page


#need to fix the layout. any method to fix this??
class Html:

    def __init__(self, phrase_list, meaning_list, vcode, v_title):
        self.phrase_list = phrase_list
        self.meaning_list = meaning_list
        self.html_table_row = ""
        self.html = ""
        self.vcode = vcode
        self.v_title = v_title

#add table data, url, and the title of the video
    def add_items(self):
        for i in range(len(self.phrase_list)):
            self.html_table_row += f'<tr><td>{str(i)}</td> <td>{self.phrase_list[i]}</td> <td>{self.meaning_list[i]}</td></tr>'
        self.html = f'<!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <title>My Website</title> <link rel="stylesheet" href="/static/css/video.css"> </head> <body> <header> <h1>{self.v_title}</h1> </header> <main> <div class="table-container"> <table> <tr> <th class="header-1">No.</th> <th class="header-2">フレーズ</th> <th class="heaeer-3">意味</th> </tr> {self.html_table_row} </table> </div> <div class="iframe-container"> <iframe width="560" height="315" src="https://www.youtube.com/watch?v={self.vcode}" frameborder="0" allowfullscreen></iframe> </div> </main> <footer> </footer> </body> </html>'
        return self.html
    
    def make_page(self):
        self.f = open(f'../web_dev/templates/{self.vcode}.html', 'w')
        self.f.write(self.add_items())
        self.f.close()

if __name__ == "__main__":
    phrase_list = ["Hello", "Good morning"]
    meaning_list = ["こんにちは", "おはようございます"]
    vcode = "X7xOEez75B0" #test but acutual video code
    v_title = "test title"
    h = Html(phrase_list, meaning_list, vcode, v_title)
    h.make_page()