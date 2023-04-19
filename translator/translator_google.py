from googletrans import Translator
from google.cloud import translate_v2 as translate

class GoogleTranslator:
    def __init__(self, phrase_list):
        self.translator = Translator()
        self.phrase_list = phrase_list

    def translate(self):

        meaning_list = []
        api_key = "YOUR_OWN_KEY"

        translate_client = translate.Client(credentials=api_key)

        print("="*80, "\ntranslating...")
        for item in self.phrase_list:
            print(item)
            response = translate_client.translate(item, target_language="JA", source_language="EN")["translatedText"]
            meaning_list.append(response)
        print(f"""translate:
              \nthe length of the phrase_list: {len(self.phrase_list)}
              \nthe length of the meaning_list: {len(meaning_list)}
            """)
        return meaning_list
            
if __name__ == "__main__":

    phrase_list = ["Hello", "Good morning"]
    
    t = GoogleTranslator(phrase_list)
    meaning_list = t.translate()
    print(meaning_list)
