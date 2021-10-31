# # NUMBER ONE
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def oldest_cat(cat_list):
#     # max([cat.age for cat in cat_list])
#     # age = 0
#     # for cat in cat_list:


#     cats_sorted = sorted(cat_list,key=lambda cat:cat.age)[-1]
#     return cat

# data_list = [('rex', 34), ('mr bubbles', 12), ('meow', 8)]

# cats = [Cat(*data) for data in data_list]

# oldest = oldest_cat(cats)
# print(oldest.name, oldest.age)

# NUMBER TWO

# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#         def bark():
#             print(f'{self.name} goes woof!')
#         def jump():
#             print(f'{self.name} jumps ({self.height}*2) cm high!')
#             return Dog
# davids_dog = Dog('rex', 50)
# print(davids_dog.bark(), davids_dog.jump())

# sarahs_dog = Dog('teacup', 20)


# NUMBER THREE



# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         for elem in self.lyrics:
#             print(elem)


# mcDonald = Song(["old Mc Donald hha a farm, EIEIO, and on his farm he had a goat, EIEIO"])

# mcDonald.sing_me_a_song()

# # NUMBER FOUR

# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        animal_list = []
    def add_animal(self, new_animal):
        self.animal_list.append(new_animal)
    def get_animal(self):
        for i in self.animal_list:
            print(i)
    def sell_animal(self, animal_sold):
        self.animal_sold = animal_sold
        if i in animal_list:
            del i
    def sort_animals(self):
        self.animal_list.sort()

    def get_groups(self):
        print(self.animal_list)


ramat_gan_safari = ["lion", "tiger", "zebra", "monkey", "cheetah"]
print(Zoo.add_animal(ramat_gan_safari, 'leopard'))
print(Zoo.get_animals(ramat_gan_safari))
print(Zoo.sell_animal(ramat_gan_safari))
print(Zoo.sort_animals(ramat_gan_safari))

            









# # gold1
# import math

# class Circle:
#     def __init__(self, radius=1.0):
#         self.radius = radius
#     def perimeter(self):
#         return self.radius/2 * math.pi
#     def area(self):
#         return self.radius **2 *math.pi
#     def definition(self):
#         print('a circle is a plane figure etc')


# circle = Circle()
# print(circle.radius)
# print(circle.area())
# print(circle.perimeter())

# circle2 =

# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.
# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.
# Add a method called show_call_history. This method should print the call_history.
# Add another attribute called messages to your __init__() method which value is an empty list.
# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to
# from
# content
# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
# Test your code !!!

# class Phone:
#     def __init__(self, phone_number):
#         self.number = phone_number
#         self.call_history = []
#         self.messages = []

#     def phone_call(self, other_phone):
#         call_string = f'call from: {self.number} to: {other_phone.number}'
#         self.call_history.append(call_string)

#     def show_call_history(self):
#         for record in self.call_history:
#             print(f'\n {record}')
#     def send_message(self, destination, content):
#         message = {
#             'to': destination,
#             'from': self.number,
#             'content': content
#         }
#         self.messages.append(message)
#     def show_outgoing_messages(self):
#         for message in self.messages:
#             if message ['from'] == self.number:
#                 print(message)
#     def show_incoming_messages(self):
#         for message in self.messages:
#             if message ['to'] == self.number:
#                 print(message)
#     def show_messages_from(self, other_number):
#         for message in self.messages:
#             if message ['from'] == other_number:
#                 print(message)

# phone1 = Phone(1234567890)
# phone2 = Phone(9987654321)
# phone1.phone_call(phone2)
# phone2.phone_call(phone1)
# print(phone1.call_history)
# print(phone2.call_history)
# phone1.show_call_history()
# phone1.send_message('9987654321', 'heyy')
# print(phone1.messages)


