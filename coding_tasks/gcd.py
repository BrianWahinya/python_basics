from utils import clear_cmd, userInputInt
from functools import reduce

clear_cmd()

# Greatest Common Denominator
# two or more integers (at least one of which is not zero), 
# is the largest positive integer that divides the numbers without a remainder

print('''
############################
############ GCD ###########
############################
''')
divisors = [2, 3, 5, 7]

def find_common_divisors(div_a, div_b):
    common_divisors = []
    set_a = set(div_a)
    set_b = set(div_b)
    merge = set_a.intersection(set_b)
    for char in merge:
        smallest_count = min(div_a.count(char), div_b.count(char))
        for _ in range(smallest_count):
            common_divisors.append(char)
    return common_divisors

def find_divisors(num):
    arr_divisors = []
    while num > 1:
        if not num == int(num): break
        prev_num = num
        for dv in divisors:
            if num % dv == 0:
                num = num / dv
                arr_divisors.append(dv)
                break
        if prev_num == num: 
            arr_divisors.append(int(num)) 
            arr_divisors.append(1) 
            break
    return arr_divisors

def display(num_1, num_2):
    divisors_1 = find_divisors(num_1)
    divisors_2 = find_divisors(num_2)
    common_divisors = find_common_divisors(divisors_1, divisors_2)
    gcd = reduce((lambda x, y: x * y), common_divisors)

    print(num_1, divisors_1, sep=": ")  
    print(num_2, divisors_2, sep=": ")  
    print("Common: ", common_divisors)
    print("GCD: ", gcd)  
    

if __name__ == "__main__":
    # Get input: any type
    print("Number 1: \n")
    user_input_1 = userInputInt()

    print("Number 2: \n")
    user_input_2 = userInputInt()
    
    print("\n")
    display(int(user_input_1), int(user_input_2))
