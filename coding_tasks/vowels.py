import re
from utils import clear_cmd, userInput

clear_cmd()

# Vowels
# Print all vowels present in a string

print('''
############################
######### Vowels #########
############################
''')

user_input = userInput()

### Method 1: Loop ###
def loop_method(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    items = []
    for char in text:
        if char.lower() in vowels: items.append(char)
    return ''.join(items)

print("Loop: ", loop_method(user_input))

### Method 2: Regex ###
def regex_method(text):
    items = re.findall(r'[aeiouAEIOU]', text)
    return ''.join(items)

print("Regex: ", regex_method(user_input))

print("\nCase-insensitive")

### Method 3: Find ###
def find_method(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    items = []
    for char in vowels:
        if text.find(char) != -1: items.append(char)
    return ''.join(items)

print("Find: ", find_method(user_input.lower()))

### Method 4: Count ###
def count_method(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    items = {}
    for char in vowels:
        items[char] = text.count(char)
    return items

print("Count: ", count_method(user_input.lower()))