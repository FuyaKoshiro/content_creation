#recieve the html table compoent
#embed the table into the html template
#add css and javascript template
#return the page

class Html:

    def __init__(self, html, vcode):
        self.html_table = html
        self.html_template = f"""
        <!doctype html>
        <html>
        <head>
        <title>Title</title>
        </head>
        <body>
        <h2>This is the table</h2>
        {self.html_table}
        </body>
        </html>
        """
        self.vcode = vcode
    
    def write_html(self):
        self.f = open(f'{self.vcode}.html', 'w')
        self.f.write(self.html_template)
        self.f.close()




# from gpt import gpt
# from script import Script

# class Gpt():
#     def __init__(self):
#         self.url = input("enter the url of the video and press enter:")
    
#     def write_html(self):
#         f = open(f"{self.vcode}.html", "w")
#         self.html_page = html_template = f"""<html>

    
# gpt = gpt("https://www.youtube.com/watch?v=SbIpWHQI-tE")
# html = gpt.gpt_get_answer()

# #from gpt import html
# from script import Script

# url = input("input the url of the YouTube video and press enter:\n")
# vcode = Script(url).vcode
# f = open(f'{vcode}.html', 'w')

# html = "<p>this is a test paragraph</p>"
  
# # the html code which will go in the file GFG.html

  
# # writing the code into the file
# f.write(html_template)
  
# # close the file
# f.close()