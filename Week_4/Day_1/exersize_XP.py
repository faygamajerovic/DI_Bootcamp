# # # # NUMBER ONE

# # # # print('hello world\n' * 4)

# # # # NUMBER TWO
# # # # Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

# # # # num = (99^3) * 8
# # # # print(num)

# # # # NUMBER THREE

# # # >>> 5 < 3 FALSE
# # # >>> 3 == 3 TRUE
# # # >>> 3 == "3" FALSE
# # # >>> "3" > 3 FALSE
# # # >>> "Hello" == "hello" FALSE

# # # NUMBER FOUR
# # # Create a variable called computer_brand which value is the brand name of your computer.
# # # Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

# # computer_brand = 'lenovo'
# # comp_sen = f'i have a {computer_brand} computer'
# # print(comp_sen)

# # NUMBER FIVE
# # Create a variable called name, and set it’s value to your name.
# # Create a variable called age, and set it’s value to your age.
# # Create a variable called shoe_size, and set it’s value to your shoe size.
# # Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# # Have your code print the info message.
# # Run your code

# # name = 'fayga'
# # age = 27
# # shoe_size = 8
# # info = f'my name is {name} and i am a {age} year old who wears size {shoe_size} shoes'
# # print(info)

# # NUMBER SIX
# # Create two variables, a and b.
# # Each variables value should be a number.
# # If a is bigger then b, have your code print Hello World.

# # a = 8
# # b = 5
# # if a > b:
# # 	print('hello world')

# # # NUMBER SEVEN
# # Write code that asks the user for a number and determines whether this number is odd or even.

# # num = int(input('pick a number'))
# # if num % 2 == 0:
# # 	print('even')
# # if num % 2 != 0:
# # 		print('odd')

# # NUMBER EIGHT
# # Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
# user_name = input('what is your name?')
# if user_name == 'fayga':
# 	print('hey we have the same name that is dope af')
# if user_name != 'fayga':
# 	print('dont you wish your name was fayga')

# NUMBER NINE
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input('how tall are you in cm?'))
if height > 145:
	print('enjoy the ride!')
if height < 145:
	print('drink your milk and come back')
