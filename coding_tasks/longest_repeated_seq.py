from utils import clear_cmd, userInput

clear_cmd()

# Longest Non-Single Repeated Sequence
# Example: In "202011211345555"
# Repeated Items: {'555': 2, '55': 3, '20': 2, '11': 2}
# Result: {'555': 2}

print('''
##########################################
## Longest Non-Single Repeated Sequence ##
##########################################
''')

# Get input: any type
user_input = userInput().replace(" ","")

### Method 1: Loop ###
# Time complexity (O(n*n))
def loop_method(string):
    char_dict = {}
    count = 0
    while count < len(string):
        for i in range(count, len(string)):
            elem = string[count:i+1]
            if len(elem) < 2: continue
            if elem in char_dict:
                char_dict[elem] += 1
            else:
                char_dict[elem] = 1
        count += 1
    
    chars_list = list(char_dict.items())

    repeated_items = [item for item in chars_list if item[1] > 1]
    if not repeated_items: return None

    sorted_items = sorted(repeated_items, key=lambda x: (len(x[0]), x[1]), reverse=True)

    sorted_dict = {item[0]:item[1] for item in sorted_items}
    print(f"\nRepeated Items: {sorted_dict}")

    longest_items = [tup for tup in sorted_items if (len(tup[0]), tup[1]) == (len(sorted_items[0][0]), sorted_items[0][1])]

    return {item[0]:item[1] for item in longest_items}

print(f"\nResult: {loop_method(user_input)}\n")