# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
# a classmethod that returns a Text instance but with a text file: >>> Text.from_file('the_stranger.txt')

import re

class Text():
    def __init__(self):
        pass

    def wordInText(self):
        frequency = {}
        document_text = open('theStranger_text.txt', 'r')
        text_string = document_text.read().lower()
        match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        frequency_list = frequency.keys()

        for words in frequency_list:
            print(words, frequency[words])

    wordInText("and")