#recieve a youtube script
#input it into chat gpt
#ask gpt to create the html table component
#return the html table component


import os
import openai
import re

key = "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"
openai.api_key = key


#need to make them into a class to import some variables into another file 
#need to do a conversation to output two different list in a row 

class Gpt:
    def __init__(self, script):
        self.script = script
        self.input_messages = [
            {"role": "user", "content": f"can you make a list of phrases and words that might be hard for non-native English speakers from the script? and make a python list of these phrases and words. \nOutput should look like: \n'phrases_list = ['phrase_1', 'phrase_2',...]' \nthe script is {script}."},
        ]
        self.conv_history = []
        self.completion = None
        self.chat_response = None
        self.phrase_list = []

    def get_answer(self):
        print("="*80, "\ngpt-3.5-turbo is generating an answer...")
        for input_message in self.input_messages:
          self.conv_history.append(input_message)
          self.completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=self.conv_history
              )
          #print(f"input_message is: \n{input_message['content']}\n", "="*80)
          self.chat_response = self.completion.choices[0].message.content
          #print(f"chat_reponse is: \n{self.chat_response}\n", "="*80)
          self.conv_history.append({"role": "assistant", "content": self.chat_response})
        self.answer = self.conv_history[-1]["content"]
        print("="*80, f"\nself.answer is :{self.answer}\n")
        return self.answer
    
    def remove_backslash(self):
        #proorfread first and remove backslash
        #figure out if the string has a backslash
        string = self.get_answer()
        while True:
            if "\'" in string:

                #get the position (index) of the backslash
                index = string.index("\'")

                #locate the ' forward
                index_forward = index
                while True:
                    if string[index_forward+2] == "'":
                        break
                    else:
                        index_forward += 1

                #locate the ' backwawrd
                index_backward = index
                while True:
                    if string[index_backward-1] == "'":
                        break
                    else:
                        index_backward -= 1
                
                #remove item in between
                string = string[:index_backward] + string[index_forward+1:]
            
            else:
                break
        
        return string
    
    #need to extract only [] part from the response
    def get_phrases(self):
        #output is overlapped with "" in a list
        self.phrase_list_dq = re.findall(r'\[(.*?)\]', self.remove_backslash(), re.DOTALL)
        self.phrase_list_dq = '"""' + self.phrase_list_dq[0] + '"""' #output is either "value1", "value2",... or 'value1', 'value2',...
        print("="*80, f"\nself.phrase_list_dq: {self.phrase_list_dq}\n")

        #need to split by "" or '' and put them into a list
        #how to tell if each item is wrapped by either "" or ''? -> get the one with larger number of items in the list
        # Use a regular expression to match quoted substrings
        pattern_double = re.compile(r'"(.*?)"')
        # Use the pattern to extract the quoted substrings
        phrase_items_double = pattern_double.findall(self.phrase_list_dq)

        pattern_single = re.compile(r"'(.*?)'")
        phrase_items_single = pattern_single.findall(self.phrase_list_dq)

        if len(phrase_items_double) > len(phrase_items_single):
            self.phrase_list = phrase_items_double
        elif len(phrase_items_double) < len(phrase_items_single):
            self.phrase_list = phrase_items_single
        else:
            print("self.phrase_items_single and self.phrase_items_double has the same length")

        print("="*80, f"\nself.phrase_list: {self.phrase_list} \nobject type of self.phrase_list: {type(self.phrase_list)}")
        return self.phrase_list

if __name__ == "__main__":
    #need to add a script
    script = """
    Medieval Europe.Where unbathed, sword-wielding knights 
ate rotten meat,thought the Earth was flat,
defended chastity-belt wearing maidens,and tortured their foes
with grisly gadgets.Except... this is more fiction than fact.So, where do all the myths 
about the Middle Ages come from?And what were they actually like?The “Middle Ages” refers 
to a 1,000-year timespan,stretching from the fall of Rome 
in the 5th centuryto the Italian renaissance in the 15th.Though it’s been applied 
to other parts of the world,the term traditionally refers
specifically to Europe.One misconception is that medieval people
were all ignorant and uneducated.For example, a 19th century biography 
of Christopher Columbusincorrectly purported that medieval 
Europeans thought the Earth was flat.Sure, many medieval scholars describe 
the Earth as the center of the universe—but there wasn't much debate
as to its shape.A popular 13th century text was literally
called “On the Sphere of the World.”And literacy rates gradually increased
during the Middle Agesalongside the establishment 
of monasteries, convents and universities.Ancient knowledge was also not “lost”;Greek and Roman texts continued
to be studied.The idea that medieval people ate rotten
meat and used spices to cover the tastewas popularized in the 1930s
by a British book.It misinterpreted one medieval recipeand used the existence of laws 
barring the sale of putrid meatas evidence it was regularly consumed.In fact, medieval Europeans 
avoided rancid foodsand had methods for safely 
preserving meats,like curing them with salt.Spices were popular.But they were oftentimes pricier 
than meat itself.So if someone could afford them, 
they could also buy unspoiled food.Meanwhile, the 19th century 
French historian Jules Micheletreferred to the Middle Ages as 
“a thousand years without a bath.”But even small towns boasted well-used
public bathhouses.People lathered up with soaps 
made of thingslike animal fat, ash, and scented herbs.And they used mouthwash, teeth-scrubbing
cloths with pastes and powders,and spices and herbs 
for fresh-smelling breath.So, how about medieval torture devices?In the 1890s, a collection of allegedly
“terrible relics of a semi-barbarous age”went on tour.Among them: the Iron Maiden, which
fascinated viewers with its spiked doors—but it was fabricated, 
possibly just decades before.And there’s no indication Iron Maidens
actually existed in the Middle Ages.The “Pear of Anguish,” meanwhile, 
did exist—but probably later on and 
it couldn’t have been used for torture.It may have just been a shoe-stretcher.Indeed, many ostensibly medieval torture
devices are far more recent inventions.Medieval legal proceedings were overall
less gruesome than these gadgets suggest.They included fines, imprisonment,
public humiliation,and certain forms of corporal punishment.Torture and executions did happen,but especially violent punishments,
like drawing and quartering,were generally reserved
for crimes like high treason.Surely chastity belts were real, 
though, right?Probably not.They were first mentioned by a 15th
century German engineer, likely in jest,alongside fart jokes 
and a device for invisibility.From there, they became 
popular subjects of satirethat were later mistaken 
for medieval reality.Ideas about the Middle Ages have varieddepending on the interest 
of those in later times.The term— along with the
pejorative “Dark Ages”—was popularized during
the 15th and 16th centuriesby scholars biased toward the 
Classical and Modern periodsthat came before and after.And, as Enlightenment thinkers celebrated
their dedication to reason,they depicted medieval people 
as superstitious and irrational.In the 19th century, some Romantic
European nationalist thinkers— well—romanticized the Middle Ages.They described isolated, white,
Christian societies,emphasizing narratives 
of chivalry and wonder.But knights played minimal roles
in medieval warfare.And the Middle Ages saw 
large-scale interactions.Ideas flowed into Europe along Byzantine,
Muslim, and Mongol trade routes.And merchants, intellectuals, 
and diplomats of diverse originsvisited medieval European cities.The biggest myth may be
that the millennium of the Middle Agesamounts to one distinct, cohesive period 
of European history at all.Originally defined less by what they were
than what they weren’t,the Middle Ages became 
a ground for dueling ideas—fueling more fantasy than fact.
    """
    gpt = Gpt(script=script)
    phrase_list = gpt.get_phrases()
    print(phrase_list)