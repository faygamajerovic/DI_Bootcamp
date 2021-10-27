# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, the user entries the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.


# Hint:for letter in text:
#     cypher_text += chr(ord(letter) + 3)
# c = (x + n) % 26
result = ""
user_msg = input('would you like to encrypt a message? write yes or no.')
if user_msg =="yes":
    input2 = input('write message to encrypt')
# print(input2)

for letter in input2:
    # char = letter[]
    # if (letter.isupper()):
       result = chr((ord(letter) + letter-65) % 26 + 65)
    # else: 
    #     result += chr((ord(letter) + letter - 97) % 26 + 97)
print(result)


# def encrypt(text,s):
# result = ""
#    # transverse the plain text
#    for i in range(len(text)):
#       char = text[i]
#       # Encrypt uppercase characters in plain text
      
#       if (char.isupper()):
#          result += chr((ord(char) + s-65) % 26 + 65)
#       # Encrypt lowercase characters in plain text
#       else:
#          result += chr((ord(char) + s - 97) % 26 + 97)
#       return result
# #check the above function
# text = "CEASER CIPHER DEMO"
# s = 4

# print "Plain Text : " + text
# print "Shift pattern : " + str(s)
# print "Cipher: " + encrypt(text,s)

def calculation(a, b)
