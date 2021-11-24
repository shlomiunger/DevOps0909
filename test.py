x = ""
y = "#"
spaces = "     "
# print(len(spaces))
for i in range(7):
    if len(spaces) > 1:
        print(x + y + spaces + y)
        x += " "
        for x in range(len(x)):
            if len(spaces) >= 1:
                spaces = spaces.replace(spaces[0: -1], "")

# spaces = spaces.replace(spaces[0: -1], "")
print(f"-{spaces}-")
