from utils import clear_cmd, userInputInt

clear_cmd()

# Smallest integer whose sum of elements is double N
# N is sum of elements in integer X.
# Example: X = 12 then N = 1+2 = 3
# Smallest integer Y elements are m,n
# m + n + ... = 2*N
# Assumption an integer can't start with 0. Example 2 cant be represented as 02

print('''
############################
##### Smallest integer #####
############################
''')

def find_smallest_int(num):
    count = 10
    while True:
        y_sum = find_sum_integers(count)
        print(f"{count} = {y_sum}")
        if y_sum == num:
            return count
        count += 1

def find_sum_integers(num):
    num_integers_list = list(map(int, str(num)))
    ## alternative
    # num_integers_list = [int(num) for char in str(num)]
    sum_integers = sum(num_integers_list)
    return sum_integers

def display(num):
    sum_integers = find_sum_integers(num)
    double_n = 2 * sum_integers
    print(f"\nSum: {str(num)} = {sum_integers}")
    print(f"Target: {double_n}\n")

    result = find_smallest_int(double_n)
    print(f"Result: {result}")

if __name__ == "__main__":
    # Get input: any type
    user_input = userInputInt()
    display(int(user_input))
