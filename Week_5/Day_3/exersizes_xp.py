# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

# NUMBER ONE


# class Newclass:
   
#     def __init__(self):
#         pass

#     def __abs__(self):
#         print("this is absolute")

#     def __int__(self):
#         print("this is int")

# object1 = Newclass()
# print(Newclass.__doc__)
# print(object1.__doc__)

# object1.__abs__()
# object1.__int__()

# NUMBER TWO

class Currency():
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount 

def __str__(self):
    return f'{self.amount} {self.currency}'

def __int__(self):
    return f'{self.amount}'

def __repr__(self):
     return f'{self.amount} {self.currency}'


def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount + self.currency
            else:
                raise Exception("Cannot add between Currency type <dollar> and <shekel>")
        else:
            raise Exception("Cannot add except objects and ints")

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
