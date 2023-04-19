"""
==================
recieve a dataframe with a column of video titles and update the index page
==================
"""


#update the home.index corresponding to the update of the drop down menu.
import pandas as pd


class UpdateIndexHTML:
      
     def __init__(self, df):
        self.vtitle_list_all = df["vtitle"]
           
     def add_options(self):
        html_option_row = ""
        for item in self.vtitle_list_all:
            html_option_row += f'<option value="{item}">'
        html = f'<!DOCTYPE html> <html><head> <title>My Website</title> <link rel="stylesheet" href="/static/css/home.css"> </head><body> <header> </header> <main> <div class="first-row-container"> <form action="/home" method="post"> <input type="text" id="cars" list="car-list" name="video_title" placeholder="select a video to learn with" class="input-box"> <datalist id="car-list" class="datalist"> {html_option_row} </datalist> <input type="submit" class="submit-button" value="Go"> </form> </div> <div class="second-row-container"> <div class="text-container"> <h1>Have fun & learn</h1> <div>learn phrases before watching</div> </div> <img src="/static/images/20230214_art_no_bg.png" alt="Image" class="image"> </div> </div> </main> <footer> <div class="expanded-box"> <p class="copy-right">@Copy Right: Fuya 2023</p> </div> </footer> </body></html>'
        return html
     
     def overwrite_page(self):
        html = self.add_options()
        f = open('../web_dev/templates/home.html', 'w')
        f.write(html)
        f.close()


if __name__ == "__main__":
    df = pd.DataFrame(columns=["vcode", "vtitle"])
    df_to_append = pd.DataFrame(columns=["vcode", "vtitle"], data=[["test_vcode1", "test_vtitle1"], ["test_vcode1", "test_vtitle2"]])
    df = df.append(df_to_append, ignore_index = True)
    update_index_html = UpdateIndexHTML(df)
    print("-"*80, "\n", f"extracted vtitle of the dataframe: \n{update_index_html.vtitle_list_all}\nthe data type: {type(update_index_html.vtitle_list_all)}")
    update_index_html.overwrite_page()