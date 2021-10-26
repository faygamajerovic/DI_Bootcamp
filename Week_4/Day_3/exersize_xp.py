# # NUMBER ONE
# from typing import KeysView

# # NUMBER ONE
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# for word,number in zip(keys, values):
#     print(word, number)

# # NUMBER TWO
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# # family_ages = input('how old are you guys?').split(',')
# total_price = []

# for name in family:
#     age =int(age)
#     if age < 3:
#         total_price.append(0)
#         continue
#     if 3 < age < 12:
#         total_price.append(10)
#         continue
#     else:
#         total_price.append(15)
#         continue
# print(total_price)

# family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# prices = total_price[]

# family_prices = {name: prices + prices for (name, age) in total_prices.items()}

# print(family_prices)

# # NUMBER THREE

# brand = {
#     'name': 'Zara', 
#     'creation_date': 1975, 
#     'creator_name': 'Amancio Ortega Gaona', 
#     'type_of_clothes': ['men', 'women', 'children', 'home'],
#     'international_competitors' : ['Gap', 'H&M', 'Benetton'], 
#     'number_stores': 7000,
#     'major_color':{ 
#         'France': 'blue', 
#         'Spain': 'red', 
#         'US': ['pink', 'green']
#     }
# }

# brand['number_stores'] = 2

# print("Zara is a company created in", brand['creation_date'], "by", brand['creator_name'] + "." +
#       "zara carries items for", brand['type_of_clothes'], "and their competitors are", brand['international_competitors'])

# brand['country_creation'] = 'spain'
# print(brand)

# if 'international_competitors' in brand:
#     brand['international_competitors'] += 'designul'
#     print(brand)
# brand.pop('creation_date')
# print(brand)

# # print(brand['international_competitors'][-1])

# # for i in brand['international_competitors']:
# #     len_comp = len(brand['international_competitors'])
# #     print(i[len_comp- 1])

# print(brand['major_color']['US'])

# print(len(brand))

# print(brand.keys())

# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }
# print(more_on_zara)

# new_brand = brand.update(more_on_zara)
# print(new_brand)
# print(brand)

# print(brand['number_stores'])



# NUMBER FOUR

#1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.


# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# new_user = dict(zip(users, range(len(users))))
# print(new_user)

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# new_user = dict(zip(range(len(users)),(users)))
# print(new_user)

# alph = users.iterkeys() 
# print(alph)

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# new_user = dict(zip(users, range(len (users))))
# print(new_user)

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# a = sorted(users)
# print(a)
# new_user = dict(zip(a, range(len(a))))
# print(new_user)

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

# new_users =[]
# for user in users:
#     if 'i' in user:
#         new_users.append(user)
# print(new_users) 

# new_user = dict(zip(new_users, range(len(new_users))))
# print(new_user)

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
new_mpuser = []

for user in users:
    if user[0] == 'M' or user[0] == 'P':
        new_mpuser.append(user)
print(new_mpuser)

new_user = dict(zip(new_mpuser, range(len(new_mpuser))))
print(new_user)