#input channel id and return the list of urls of the vidoes

import scrapetube

class Vcode:
    def __init__(self):
        self.channel_url = input("input the url of the channel: \n")
        self.video_urls = []

    def get_vcode(self):
        self.videos = scrapetube.get_channel(channel_url=self.channel_url)
        for video in self.videos:
            self.video_urls.append(video["videoId"])
        return self.video_urls


if __name__ == "__main__":
    url_list = Vcode()
    videos = url_list.get_vcode()
    for video in videos:
        print(video['videoId'])

