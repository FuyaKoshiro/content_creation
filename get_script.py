"""
==================
recieve a list of video codes, and return the list of scripts of them
==================
"""


from youtube_transcript_api import YouTubeTranscriptApi as yt


class GetScript:
    
    def __init__(self, vcode):
        self.vcode = vcode
    
    def get_script_dict(self):
        script_dict = yt.get_transcript(video_id=self.vcode, languages=["en"])
        return script_dict
    
    def get_script_list(self, script_dict):
        script_list = []
        for i in range(0, len(script_dict)):
            text = script_dict[i]["text"]
            script_list.append(text)
        return script_list
    
    def get_script_string(self):
        script_dict = self.get_script_dict()
        script_list = self.get_script_list(script_dict)
        script = "".join(script_list)
        return script


if __name__ == "__main__":
    vcode = input("input video code and press enter:")
    get_script = GetScript(vcode=vcode)
    script = get_script.get_script_string()
    print(script)