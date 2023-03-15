#recieve the html table compoent
#embed the table into the html template
#add css and javascript template
#return the page


#need to fix the layout. any method to fix this??
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
        self.f = open(f'html_files/{self.vcode}.html', 'w')
        self.f.write(self.html_template)
        self.f.close()