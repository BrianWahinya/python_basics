from utils import clear_cmd, userInputInt

clear_cmd()

# Fibonacci
# In a series of numbers, the next number is a result of the previous 2 numbers before it
# Example: 0, 1, 1, 2, 3, 
# Next number is 2+3=5

print('''
############################
######### Fibonacci ########
############################
''')

def fibonacci(arr):
    arr_len = len(arr)
    return arr[arr_len - 1] + arr[arr_len - 2]

def display(num):
    arr = [0, 1, 3]
    for _ in range(0, num + 1):
        elem = fibonacci(arr)
        arr.append(elem)
        print(elem, arr, sep=": ")

if __name__ == "__main__":
    # Get input: any type
    user_input = userInputInt()
    display(int(user_input))
