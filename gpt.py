#recieve a youtube script
#input it into chat gpt
#ask gpt to create the html table component
#return the html table component

import os
import openai


#in actual case, it is not written. main.py covers all.
script = "Right? So here we are in this infinite data source. There's an infinite number of things that we could think about, but we edit and delete. We choose what to think about, what to pay attention to. We make up a story ... to make sense of what's going on, and we all get it wrong. Because we're all trying to navigate with our own skewed compasses, and we all have our own baggage, but the stories themselves are utterly convincing. And we all do this, and a lot of the stories that we live by aren't even our own. The first ones we inherit at a young age from our parents, who of course have their own skewed beliefs, their own frustrations, their own unlived lives. And for better or worse, we take all that onboard, and then we go out into the world thinking maybe we have to be successful to be loved; or that we always have to put other people's needs first; or that we have some big terrible secret we couldn't possible tell people. And it's just fiction, it's just stories, and we'd worry a lot less about what other people think of us if we realized how seldom they do."
key = "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"
openai.api_key = key


input_messages = [
    {"role": "user", "content": f"can you extract phrases and words that might be difficult for non-native speakers from this script '{script}'"},
    {"role": "user", "content": "can you turn it into HTML table with the columns of phrases and explanation in Japanese?"},
]

conv_history = []

for input_message in input_messages:

    conv_history.append(input_message)
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=conv_history
    )

    chat_response = completion.choices[0].message.content
    print("-"*80)
    print(f'ChatGPT: {chat_response}')
    conv_history.append({"role": "assistant", "content": chat_response})

print("="*80\n Output:)
print(conv_history[-1]["content"], end="")
html = conv_history[-1]["content"]
