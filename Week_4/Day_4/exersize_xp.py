# # Number one

# def calculation(a,b):
#     return a+b, a-b
# res = calculation(40, 10)
# print(res)

# def display_message():
#     print('hey im trying to learn python')

# display_message()


# # Number 2

# def favorite_book(title):
#     print(f'my fav book is: {title}')

# favorite_book('alice in wonderland')

# # number three
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.

# def describe_city(name, country= 'Iceland'):
#     print(f'{name} is in {country}')

# describe_city('reykjavik')

# NUMBER FOUR


# import random
# def random_num ():
#     return random.randint(1,101)
# def number ():
#     user_num = int(input('pick a number from 1-100'))
#     if user_num == random_num():
#         print('great minds thuink alike!')
#     else:
#         print(f'numbers didnt match! computer num is {random_num()} and your num is {user_num}')

# number()

# NUMBER FIVE

# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# # Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(size='large', text='i love python'):
#     print(f'the shirt size is{size} and the words are {text}')

# make_shirt()
# make_shirt('medium')
# make_shirt('small', 'eat me')

# # NUMBER SIX

# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the funcyion show_magicians() to see that the list has actually been modified.

# magicians = ['ross', 'rachel', 'monica', 'pheobe', 'chandler', 'joey']
# great = ' the great'

# def show_magicians():
#     for name in magicians:
#         print(name)
#         return name
# show_magicians()

# def make_great():
#     list2 = list(map(lambda orig_string: orig_string + great, magicians))
#     print(list2)
# make_great()





























# gold #1,#2
# import random
# random.randint(1, 6)

# def throw_dice():
#     return random.randint(1,6)

# def throw_until_doubles():
#     d1 = throw_dice()
#     d2 = throw_dice()
#     count =0
#     while d1 != d2:
#         count += 1
#         d1 = throw_dice()
#         d2 = throw_dice()
#     return count
# print(f'it took {throw_until_doubles()} tries to get doubles')

# def results_avg(res_list):
#     return sum(res_list)/len(res_list)


# def main():
#     results = []
#     for num in range(0,100):
#         results.append(throw_until_doubles())
#     print(f'it took{sum(results)} tries to get 100 doubles')
#     print(f'the average it took was {results_avg(results)} throws to get a double')

# main()