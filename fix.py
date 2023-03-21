#leave a log to check if the output of gpt is good. if not, edit text.

from datetime import datetime

class Fix:
    def __init__(self, phrase_list):
        self.phrase_list = phrase_list

    def fix_phrase_list(self):

        for item in self.phrase_list:
            #remove too long items
            words = item.split(" ")
            if len(words) > 4:
                self.phrase_list.remove(item)
                print("fix: a long item got removed")
                print(f"removed item {item}")
                return
            
            #remove space items
            if item.isspace():
                self.phrase_list.remove(item)
                print("fix: an empty item got removed")
                print(f"removed item {item}")
                return
            
            #remove empty items
            if item == "":
                self.phrase_list.remove(item)
                print("fix: an empty item got removed")
                print(f"removed item {item}")                
                return
            
            #remove single letter items
            if len(item) < 3:
                self.phrase_list.remove(item)
                print("fix: an item which has one or two letters got removed")
                print(f"removed item {item}")                
                return
        
        print(f"fixed phrase_list: {self.phrase_list}")
        return self.phrase_list