#input channel id and return the list of urls of the vidoes

import scrapetube
from googleapiclient.discovery import build
import sqlite3

class GetVideo:
    def __init__(self):
        self.channel_url = input("input the url of the channel: \n")
        #get the video objects in the channel

    def get_vcode(self):
        num_item_to_add = 100 #depends on how many items you want to add
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()

        num_response = num_item_to_add
        num_not_overlap_list = 0

        print("="*80)
        print(f"num_item_to_add: {num_item_to_add}")
        print(f"limit: {num_response}")
        print(f"num_not_overlap_list: {num_not_overlap_list}")

        while num_item_to_add > num_not_overlap_list:

            print(num_item_to_add > num_not_overlap_list)
            print("="*80)
            
            print(f"num_item_to_add: {num_item_to_add}")

            #get response_list
            print(f"limit: {num_response}")
            response_object = scrapetube.get_channel(channel_url=self.channel_url, limit=num_response)
            response_list = []
            for item in response_object:
                response_list.append(item["videoId"])

            #get db_list
            c.execute("SELECT video_code FROM video_db")
            db_object = c.fetchall()
            db_list = []
            for item in db_object:
                db_list.append(item[0])

            #check the number of overlap
            overlap_list = []
            for i in range(len(response_list)):
                if response_list[i] in db_list:
                    overlap_list.append(response_list[i])
            num_overlap_list = len(overlap_list)
            num_not_overlap_list = num_response - num_overlap_list
            print(f"num_not_overlap_list: {num_not_overlap_list}")

            #set the number for the next iteration
            num_response = num_item_to_add + num_item_to_add - num_not_overlap_list

        #get a list of items which don't overlap
        for item in response_list:
            if item in overlap_list:
                response_list.remove(item)
        not_overlap_list = response_list
        self.vcode_list = not_overlap_list

        return self.vcode_list
    
    #the scrapetube does not support getting video title. need to use another api or scrape by myself
    def get_vtitle(self):
        api_key = 'AIzaSyCKLts0Rip9Fq9elFG9X2ZwPNVxQLvnfPg'
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        
        vtitle_list = []

        for vcode in self.vcode_list:
            response = self.youtube.videos().list(part='snippet',id=vcode).execute()
            video_title = response['items'][0]['snippet']['title']
            vtitle_list.append(video_title)
        return vtitle_list

if __name__ == "__main__":
    gv = GetVideo()
    vcode_list = gv.get_vcode()
    vtitle_list = gv.get_vtitle()
    print(f"vcode_list: {vcode_list}\n", "="*80, f"\nvtitle_list: {vtitle_list}")
