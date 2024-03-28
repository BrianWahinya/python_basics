import sys
sys.path.append('./../')

from utils import clear_cmd, userInput

clear_cmd()

# Palindrome: a variable whose characters are in the 
# same order in both original and reversed state

print('''
############################
######## Palindrome ########
############################
''')

# Get input: any type
user_input = userInput()

### Method 1: Loop ###
def loopMethod(string):
    string2 = ''
    for char in string:
        string2 = char + string2
    return string == string2

print("Loop: ", loopMethod(user_input))

### Method 2: Slice notation ###
def sliceMethod(string):
    reversed_string = string[::-1]
    return string == reversed_string

print("Slice: ", sliceMethod(user_input))

### Method 3: List reverse ###
def listMethod(string):
    reversed_list = reversed(list(string))
    return string == ''.join(reversed_list)

print("List: ", listMethod(user_input))