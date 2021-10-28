# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world

user_sent = input('write a list of words separated by a comma')



words = ",".join([word for word in sorted(user_sent.split(","))])
print(words)

# print(type(words))


# user_sent = input('write a list of words separated by a comma')

# words = [word for word in user_sent.split(",")]
# print(",".join(sorted(list(set(words)))))