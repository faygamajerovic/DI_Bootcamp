user_phrase = input('write a 10 character input')
# print(len(user_phrase))
if (len(user_phrase)) < 10:
    print('string not long enough')
    exit()
if (len(user_phrase)) > 10:
    print('string too long')
    exit()
else:
    print(user_phrase)

print(user_phrase[0] + user_phrase[-1])

print(user_phrase[0])
print(user_phrase[1])
print(user_phrase[2])
print(user_phrase[3])
print(user_phrase[4])
print(user_phrase[5])
print(user_phrase[6])
print(user_phrase[7])
print(user_phrase[8])
print(user_phrase[9])

shuff =list(user_phrase) 
random.shuffle(shuff)
result = ''.join(shuff)
print(shuff)


