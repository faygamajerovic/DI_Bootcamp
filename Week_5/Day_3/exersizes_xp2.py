# NUMBER ONE

# from datetime import date

# today = date.today()
# print("Today's date:", today)

# NUMBER TWO

# from datetime import datetime

# # datetime object containing current date and time
# now = datetime.now()
 
# print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

# jan_date = datetime.datetime.strptime('%Y-%m-%d %H:%M:%S')

# print(jan_date - now)

# NUMBER THREE

import datetime

timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
deadline = "2021-01-01 00:00:00"
start = datetime.datetime.strptime(timenow,'%Y-%m-%d %H:%M:%S')
ends = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
print(start - ends)

# NUMBER FOUR

# Write a function that display today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

# from datetime import date

# today = date.today()
# print("Today's date:", today)

# # NUMBER FIVE

# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

# nuMBER SIX

from faker import Faker

fake = Faker()
user = {"name":fake.name(), "adress":fake.address(), "language code":fake.language_code()}
print(user)