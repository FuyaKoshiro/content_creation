"""
==================
Recieve a list phrases and return a list of meanings using DeepL API.
You need to provide your own API key to execute this code.
==================
"""


import deepl


class DeepLTranslator:

    def __init__(self, phrase_list):
        self.translator = deepl.Translator(auth_key="17564543-319e-0393-2a2b-fae6158b5598:fx")
        self.phrase_list = phrase_list

    def translate(self):
        print("="*80, "\ntranslating...")
        meaning_list = []
        for item in self.phrase_list:
            response_object = self.translator.translate_text(text=item, target_lang="JA")
            translated_item = response_object.text
            meaning_list.append(translated_item)
        print("="*80, "\ntranslation is completed")
        return meaning_list
            

if __name__ == "__main__":
    phrase_list = ["Hello", "Good morning"]
    deepl_translator = DeepLTranslator(phrase_list)
    meaning_list = deepl_translator.translate()
    print(meaning_list)