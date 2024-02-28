from utils import clear_cmd

clear_cmd()

rows = 10
columns = 10

print('''
############################
########### 90deg ##########
############################
''')

print("\nTop Left\n")
for row in range(rows + 1):
    col = columns - row
    if col <= 0: continue
    print("*" * col)

print("\nBottom Left\n")
for row in range(rows + 1, 0, -1):
    col = columns - row
    if col <= 0: continue
    print("*" * col)

print("\nTop Right\n")
for row in range(rows + 1):
    col = columns - row
    if col <= 0: continue
    stringA = " " * (columns - col)
    stringB = "*" * col
    print(stringA + stringB)

print("\nBottom Right\n")
for row in range(rows + 1, 0, -1):
    col = columns - row
    if col <= 0: continue
    stringA = " " * (columns - col)
    stringB = "*" * col
    print(stringA + stringB)

print('''
############################
###### Dynamic Angles ######
############################
''')

# print('''
# ---*----
# --***---
# -*****--
# *******-

# ''')

print("\nTop Middle\n")
mid = int(columns / 2)
for row in range(rows + 1):
    count = row + (row + 1)
    sub = mid - (row + 1)
    if sub < 0: break
    stars = "*" * count
    spaces = " " * sub
    print(spaces + stars)

print("\nBottom Middle\n")
mid = int(columns / 2)
for row in range(rows, -1, -1):
    count = row + (row + 1)
    sub = mid - (row + 1)
    if sub < 0 : continue
    stars = "*" * count
    spaces = " " * sub
    print(spaces + stars)








# if __name__ == "main":
#     clear_cmd()
#     print(clear_cmd())