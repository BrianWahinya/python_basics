from utils import clear_cmd

clear_cmd()

length = 20
width = 20
border = 3

print('''
############################
####### Square/ Rect #######
############################
''')

print("\nFull\n")
for row in range(width):
    stars = "*" * length
    print(stars)

print("\nHollow\n")
for row in range(width + 1):
    if length - (border*2) <= 0 or width - (border*2) <= 0: 
        print("Error: length and width should be larger than double the border \n")
        break

    content = ""
    if row <= border - 1 or row > width - border:
        content = "*" * length
    else:
        spaces = " " * (length - border*2)
        stars_border = "*" * border
        content = f"{stars_border}{spaces}{stars_border}"   
   
    print(content)



