from utils import clear_cmd, userInputInt

clear_cmd()

# FizzBuzz
# Print integers one-to-N, but print 
# “Fizz” if an integer is divisible by three, 
# “Buzz” if an integer is divisible by five, and 
# “FizzBuzz” if an integer is divisible by both three and five

print('''
############################
######### FizzBuzz #########
############################
''')

def fizzbuzz(num):
    if not num % 3 and not num % 5: return "FizzBuzz"
    if not num % 3: return "Fizz"
    if not num % 5: return "Buzz"
    return "__"

def display(num):
    for i in range(num + 1):
        print(i, fizzbuzz(i), sep=": ")

if __name__ == "__main__":
    # Get input: any type
    user_input = userInputInt()
    display(int(user_input))
