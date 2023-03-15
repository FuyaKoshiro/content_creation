#return youtube script

from youtube_transcript_api import YouTubeTranscriptApi as yt

class Script:
    
    def __init__(self, vcode):
        self.vcode = vcode
        self.script_list = []
        self.script = ""
    
    #to get a dictionary of the script from the video using youtube api
    def get_script_dict(self):
        self.script_dict = yt.get_transcript(self.vcode, languages=["en"])
        return self.script_dict
    
    #extract only words from the dictionry, and add them into a list
    #to avoid repetitive access to the YouTube video, define the self.dict first
    def get_script_list(self):
        self.dict = self.get_script_dict()
        for i in range(0, len(self.dict)):
            self.text = self.dict[i]["text"]
            self.script_list.append(self.text)
        return self.script_list
    
    #aggregate all items in the list to make a one string
    def get_script_string(self):
        self.script = "".join(self.get_script_list())
        # self.script.replace("\n", " ")
        return self.script

if __name__ == "__main__":
    vcode = input("input video code and press enter:") #e9-l34TcV_U
    script = Script(vcode=vcode).get_script_string()