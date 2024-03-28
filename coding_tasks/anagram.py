import sys
sys.path.append('./../')

from utils import clear_cmd, userInput, remove_special_characters

clear_cmd()

# Anagram: two or more variables whose characters 
# are the same regardless of the order.

print('''
############################
########## Anagram #########
############################
''')

# Get input: any type
user_input_1 = userInput()
print("\nSecond Input\n")
user_input_2 = userInput()

### Method 1: Sort ###
def sortMethod(string_a, string_b):
    if not len(string_a) == len(string_b): return False

    list_a = sorted(list(string_a))
    list_b = ''.join(sorted(list(string_b)))
    sorted_string_a = ''.join(list_a)
    sorted_string_b = ''.join(list_b)
    return sorted_string_a == sorted_string_b

### Method 2: Set Count ###
def setCountMethod(string_a, string_b):
    if not len(string_a) == len(string_b): return False
    merged_set = set(string_a + string_b)

    for char in merged_set:
        count_a = string_a.count(char)
        count_b = string_b.count(char)
        if not count_a == count_b:
            return False
    return True

print("\nAll characters considered")
print("Sort: ", sortMethod(user_input_1, user_input_2))
print("Set Count: ", setCountMethod(user_input_1, user_input_2))

print("\nCase insensitive and special characters ignored")

clean_input_1 = remove_special_characters(user_input_1.replace(" ","")).casefold()
clean_input_2 = remove_special_characters(user_input_2.replace(" ","")).casefold()

print("Sort: ", sortMethod(clean_input_1, clean_input_2))
print("Set Count: ", setCountMethod(clean_input_1, clean_input_2))
