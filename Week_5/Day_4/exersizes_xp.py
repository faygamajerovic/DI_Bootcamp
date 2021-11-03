# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:
# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

# import random
# num_of_words  = int(input('how many words should be in the sentence? '))
# def get_words_from_file():
#     words = []
     
#     with open('sowpods.txt', 'r') as f:
#         for line in f:
#             words.append(line.rstrip('\n'))
#         f.close()
#         return(words)
# word_list = get_words_from_file ()
# print(word_list[:5])

            

# def get_random_sentence(length):
#     sentence = ''
#     get_words = get_words_from_file()
#     rand_word = random.choices(get_words, k=num_of_words)
#     for word in rand_word:
#         sentence += word+' '
#     print(sentence.lower())
# get_random_sentence(num_of_words)

# def main():
#     print('the program creates a random incoherent sentence accoring to however many words youd like')


# def get_num():
#     num = input('Enter a number of words should create your sentence: ')
#     if 2 <= int(num) <= 20:
#         get_random_sentence(int(num))
#         main()
#     else:
#         SyntaxError
# def main():
#     print('The program job is to take random words and make a sentence in a length YOU CHOOSE!')
# get_num()


# NUMBER TWO:

import json

with open('xp.json', 'r') as f:
    info = json.load(f)
print(info['company']['employee']['payable']['salary'])

print(info['company']['employee']['payable'])

info['company']['employee']["birth_date"] =24
with open('xp.json', 'w') as f:
    json.dump(info, f)

print(info)