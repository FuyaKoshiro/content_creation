#input channel id and return the list of urls of the vidoes

import scrapetube
from googleapiclient.discovery import build

class GetVideo:
    def __init__(self):
        self.channel_url = input("input the url of the channel: \n")
        self.vcode_list = []
        self.vtitle_list = []
        #get the video objects in the channel
        self.response_list = scrapetube.get_channel(channel_url=self.channel_url, limit=2) #10 is just for a test

    def get_vcode(self):
        for response in self.response_list:
            self.vcode_list.append(response["videoId"])
        return self.vcode_list
    
    #the scrapetube does not support getting video title. need to use another api or scrape by myself
    def get_vtitle(self):
        api_key = 'AIzaSyCKLts0Rip9Fq9elFG9X2ZwPNVxQLvnfPg'
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        
        for vcode in self.vcode_list:
            response = self.youtube.videos().list(part='snippet',id=vcode).execute()
            video_title = response['items'][0]['snippet']['title']
            self.vtitle_list.append(video_title)
        return self.vtitle_list

if __name__ == "__main__":
    gv = GetVideo()
    vcode_list = gv.get_vcode()
    vtitle_list = gv.get_vtitle()
    print(f"vcode_list: {vcode_list}\n", "="*80, f"\nvtitle_list: {vtitle_list}")
