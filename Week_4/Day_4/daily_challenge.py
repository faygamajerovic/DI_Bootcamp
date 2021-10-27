# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:
matrix=[
    [7,'i',3],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
]
encrypt = []
# first_column = list[0]
# second_column = list[1]
# third_column = list[2]
def decrypt_code():
    # print(matrix[1][1])
    for list in matrix:
        first_column = list[0]
        second_column = list[1]
        third_column = list[2]
        encrypt.append(first_column)
        encrypt.append(second_column)
        encrypt.append(third_column)
        
decrypt_code()
print(encrypt)

def arrange_items():
    for letters in encrypt:
        if letters == '%' or '#' or '$' or '^' or '!':
            letters.replace(" ")

arrange_items()
print(encrypt)
 
