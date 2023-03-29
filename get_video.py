"""
==================
input an url of the YouTube channel that you like to extract script from, and the number of videos.
You need to provide your own YouTube API key to execute this code.
==================
"""


import scrapetube
from googleapiclient.discovery import build
import sqlite3


class GetVideo:
    def __init__(self):
        self.channel_url = input("channel_url: \n")
        self.num_new_item = int(input("num_new_item: \n"))

    def get_vcode_scrape(self, num_item_to_add):
        scrape_object_list = scrapetube.get_channel(channel_url=self.channel_url, limit=num_item_to_add)
        scrape_vcode_list = []
        for item in scrape_object_list:
            scrape_vcode_list.append(item["videoId"])
        return scrape_vcode_list

    def get_vcode_db(self):
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        c.execute("SELECT video_code FROM video_db")
        db_object_list = c.fetchall()
        db_vcode_list = []
        for item in db_object_list:
            db_vcode_list.append(item[0])
        return db_vcode_list
    
    def get_overlap(self, scrape_vcode_list, db_vcode_list, num_item_to_add):
        overlap_list = []
        for i in range(len(scrape_vcode_list)):
            if scrape_vcode_list[i] in db_vcode_list:
                overlap_list.append(scrape_vcode_list[i])
        num_overlap_list = len(overlap_list)
        num_not_overlap_list = num_item_to_add - num_overlap_list
        return [overlap_list, num_not_overlap_list]
    
    def remove_overlap(self, scrape_vcode_list, overlap_list):
        for item in scrape_vcode_list:
            if item in overlap_list:
                scrape_vcode_list.remove(item)
        vcode_list = scrape_vcode_list
        return vcode_list
        
    def get_vcode(self):
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()

        num_not_overlap_list = 0
        num_item_to_add = self.num_new_item

        while self.num_new_item > num_not_overlap_list:

            scrape_vcode_list = self.get_vcode_scrape(num_item_to_add=num_item_to_add)
            db_vcode_list = self.get_vcode_db()

            get_overlap_return = self.get_overlap(scrape_vcode_list, db_vcode_list, num_item_to_add)
            overlap_list = get_overlap_return[0]
            num_not_overlap_list = get_overlap_return[1]

            print("="*80, f"\nnum_item_to_add: {num_item_to_add}\nnum_not_overlap_list: {num_not_overlap_list}")

            num_item_to_add = num_item_to_add + self.num_new_item - num_not_overlap_list

        print("="*80, "\nnum_not_overlap_list = num_new_item\nexited the loop")
        vcode_list = self.remove_overlap(scrape_vcode_list=scrape_vcode_list, overlap_list=overlap_list)

        return vcode_list
    
    def get_vtitle(self, vcode_list):
        api_key = 'AIzaSyCKLts0Rip9Fq9elFG9X2ZwPNVxQLvnfPg'
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        vtitle_list = []

        for vcode in vcode_list:
            response = youtube.videos().list(part='snippet',id=vcode).execute()
            video_title = response['items'][0]['snippet']['title']
            vtitle_list.append(video_title)
        return vtitle_list

if __name__ == "__main__":
    get_video = GetVideo()
    vcode_list = get_video.get_vcode()
    vtitle_list = get_video.get_vtitle(vcode_list=vcode_list)
    print("="*80, f"\nvcode_list: {vcode_list}\n", "="*80, f"\nvtitle_list: {vtitle_list}")