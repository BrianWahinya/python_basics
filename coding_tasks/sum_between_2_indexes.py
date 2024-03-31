from utils import clear_cmd, userInputInt

clear_cmd()

# Sum of all numbers between 2 indexes

print('''
############################
## SUM BETWEEN 2 INDEXES ###
############################
''')

### Method 1: Loop ###
# Time complexity: O(n)
def loop_method(num_1, num_2):
    cumulative_sum = num_1
    for i in range(num_1 + 1, num_2 + 1):
        cumulative_sum += i
    return cumulative_sum

### Method 2: Math ###
# Time complexity: O(1)
def math_method(num_1, num_2):
    return (num_1 + num_2)/2*(num_2 + 1 - num_1)

def display(num_1, num_2):
    print(f"Loop: {num_1}...{num_2} = {loop_method(num_1, num_2)}")
    print(f"Math: {num_1}...{num_2} = {math_method(num_1, num_2)}")
    

if __name__ == "__main__":
    # Get input: any type
    print("Number 1: \n")
    user_input_1 = int(userInputInt())

    print("Number 2: \n")
    user_input_2 = int(userInputInt())
    
    print("\n")
    display(min(user_input_1, user_input_2), max(user_input_1, user_input_2))
