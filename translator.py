import deepl

class Translator:
    def __init__(self, phrase_list):
        self.translator = deepl.Translator("17564543-319e-0393-2a2b-fae6158b5598:fx")
        self.phrase_list = phrase_list
        self.meaning_list = []

    def translate(self):
        for item in self.phrase_list:
            print(item)
            response = self.translator.translate_text(item, target_lang="JA")
            translated_item = response.text
            self.meaning_list.append(translated_item)
        return self.meaning_list
            
if __name__ == "__main__":
    phrase_list = ["Hello", "Good morning"]
    t = Translator(phrase_list)
    meaning_list = t.translate()
    print(meaning_list)