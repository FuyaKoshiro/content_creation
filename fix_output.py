"""
==================
Recieve a list of phrases and fix some items and then return a fixed version of list of phrases
==================
"""


class FixOutput:
    def __init__(self, phrase_list):
        self.phrase_list = phrase_list

    def fix_phrase_list(self):

        for item in self.phrase_list:

            #remove too long items
            words = item.split(" ")
            if len(words) > 4:
                self.phrase_list.remove(item)
                print(f"fix: a long item got removed\nThe removed item: {item}")
                return
            
            #remove space items
            if item.isspace():
                self.phrase_list.remove(item)
                print(f"fix: an empty item got removed\nThe removed item: {item}")
                return
            
            #remove empty items
            if item == "":
                self.phrase_list.remove(item)
                print(f"fix: an empty item got removed\nThe removed item: {item}")             
                return
            
            #remove single letter items
            if len(item) < 3:
                self.phrase_list.remove(item)
                print(f"fix: an item which has one or two letters got removed\nThe removed item: {item}")               
                return
        
        print(f"fixed phrase_list: {self.phrase_list}")
        
        return self.phrase_list