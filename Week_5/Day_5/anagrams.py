from anagram_minipj import AnagramChecker

def is_word_valid(word):
    return len(word.split()) == 1 and word.isalpha()

while True:
    user_choice = input('A. find a word\'s anagrams\nX. Exit\n')
    if user_choice in  'xX':
        print('byebye')
        break
    elif user_choice.upper() == "A":
            selected_word = input('give us a word to use for anagram')
            if is_word_valid(selected_word):
                clean_word = selected_word.strip()
                a = AnagramChecker()
                anagrams = a.get_anagrams(clean_word)
                message = f''''your word : "{clean_word}" 
                this is a valid english word yay.
                anagrams for your word:'''
                print(message, *anagrams)
            else:
                print('not a valid word')
