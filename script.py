#return youtube script

from youtube_transcript_api import YouTubeTranscriptApi as yt
 
#assume inputing only 1 url everytime.
#in case the script is too long, you need to split them into several pieces, and get together later

class Script:
    
    def __init__(self, url):
        self.url_parts = url.split("v=")
        self.vcode = self.url_parts[-1]
        self.script_list = []
        self.script = ""
    
    #to get a dictionary of the script from the video using youtube api
    def get_script_dict(self):
        self.script_dict = yt.get_transcript(self.vcode, languages=["en"])
        print("script_dict is done")
        return self.script_dict
    
    #extract only words from the dictionry, and add them into a list
    #to avoid repetitive access to the YouTube video, define the self.dict first
    def get_script_list(self):
        self.dict = self.get_script_dict()
        for i in range(0, len(self.dict)):
            self.text = self.dict[i]["text"]
            self.script_list.append(self.text)
            print(self.script_list)
        print("script_list is done")
        return self.script_list
    
    #aggregate all items in the list to make a one string
    def get_script_string(self):
        for script in self.get_script_list():
            self.script = self.script + script
        print("script_string is done")
        return self.script

if __name__ == "__main__":
    url = input("input url and press enter:")
    script = Script(url=url).get_script_string()
    print(script)
