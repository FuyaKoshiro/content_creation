"""
==================
Recieve a list phrases and return a list of meanings using openAI API.
You need to provide your own API key to execute this code.
==================
"""

import openai
from get_phrase import GetPhrase

class gptTranslator:
    def __init__(self, phrase_list) -> None:
        self.phrase_list = phrase_list

    def translate(self):
        conv_history = []
        input_messages = [
            {"role": "user",
                "content": f"Can you translate the list in Japanese and return as a python list \nthe list is {self.phrase_list}."},
        ]
        for input_message in input_messages:
            conv_history.append(input_message)
            completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=conv_history
              )
            answer = completion.choices[0].message.content

        get_phrase = GetPhrase(script=None)
        answer_bs_removed = get_phrase.remove_backslash(answer=answer)
        meaning_list = get_phrase.get_phrase_list(answer_bs_removed=answer_bs_removed)

        return meaning_list