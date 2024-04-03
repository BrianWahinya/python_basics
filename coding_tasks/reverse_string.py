from utils import clear_cmd, userInput

clear_cmd()

# Reverse string or number

print('''
############################
###### Reverse String ######
############################
''')

# Get input: any type
user_input = userInput()

### Method 1: Loop ###
def loopMethod(string):
    string2 = ''
    for char in string:
        string2 = char + string2
    return string2

print("Loop: ", loopMethod(user_input))

### Method 2: Slice notation ###
def sliceMethod(string):
    reversed_string = string[::-1]
    return reversed_string

print("Slice: ", sliceMethod(user_input))

### Method 3: List reverse ###
def listMethod(string):
    reversed_list = reversed(list(string))
    return ''.join(reversed_list)

print("List: ", listMethod(user_input))