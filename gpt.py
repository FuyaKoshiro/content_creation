#recieve a youtube script
#input it into chat gpt
#ask gpt to create the html table component
#return the html table component

import os
import openai

key = "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"
openai.api_key = key

#need to make them into a class to import some variables into another file  

class Gpt:
    def __init__(self, script):
        self.script = script
        self.input_messages = [
            {"role": "user", "content": f"can you extract phrases and words that might be difficult for non-native speakers from this script '{script}'"},
            {"role": "user", "content": "can you turn it into HTML table with the columns of phrases and some explanations in Japanese?"},
        ]
        self.conv_history = []
        self.completion = None
        self.chat_response = None
        self.html = None

    def get_answer(self):
       for input_message in self.input_messages:
          self.conv_history.append(input_message)
          self.completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=self.conv_history
              )
          self.chat_response = self.completion.choices[0].message.content
          print("-"*80)
          print(f'ChatGPT: {self.chat_response}')
          self.conv_history.append({"role": "assistant", "content": self.chat_response})
       self.html = self.conv_history[-1]["content"]
       return self.html

if __name__ == "__main__":
    gpt = gpt("ttps://www.youtube.com/watch?v=SbIpWHQI-tE")
    print("="*80, "Output:")
    html = gpt.conv_history[-1]["content"]
    print(html)
