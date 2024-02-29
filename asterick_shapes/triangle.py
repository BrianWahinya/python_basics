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

mid = int(columns / 2)

print("\nTop Middle\n")
for row in range(rows + 1):
    count = row + (row + 1)
    sub = mid - (row + 1)
    if sub < 0: break
    stars = "*" * count
    spaces = " " * sub
    print(spaces + stars)

print("\nBottom Middle\n")
for row in range(rows, -1, -1):
    count = row + (row + 1)
    sub = mid - (row + 1)
    if sub < 0 : continue
    stars = "*" * count
    spaces = " " * sub
    print(spaces + stars)

print("\nMiddle Left\n")
find_bigger = lambda x, y: (int(x / 2) if x < y else int(y / 2))
mod_mid = find_bigger(columns, rows)
for row in range(rows + 1):
    if row < mod_mid:
        no_stars = row + 1
        no_spaces = mod_mid - no_stars
        stars = "*" * no_stars
        spaces = " " * no_spaces
        print(spaces + stars)

    if row > mod_mid:
        no_spaces = row - mod_mid
        no_stars = mod_mid - no_spaces
        if no_stars <= 0: break
        stars = "*" * no_stars
        spaces = " " * no_spaces
        print(spaces + stars)



# if __name__ == "main":
#     clear_cmd()
#     print(clear_cmd())