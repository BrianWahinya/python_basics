rows = 30
columns = 10

########### 90deg #############
print('''
#############################
########### 90deg ###########
#############################
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


# if __name__ == "main":
#     pass