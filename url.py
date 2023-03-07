#input channel id and return the list of urls of the vidoes

import scrapetube

class List:
    def __init__(self):
        self.channel_url = input("input the url of the channel: \n")
        self.video_urls = []

    def get_urls(self):
        self.videos = scrapetube.get_channel(channel_url=self.channel_url)
        print(f"type of the self.videos is {type(self.videos)}")
        for video in self.videos:
            self.video_urls.append(video)
        return self.video_urls


if __name__ == "__main__":
    url_list = List()
    videos = url_list.get_urls()
    for video in videos:
        print(video['videoId'])

