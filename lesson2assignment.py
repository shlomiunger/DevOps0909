import MyMethods

# A.

X = 1
Y = 2
if X > Y:
    print("BIG")
elif X < Y:
    print("small")

# B.

for i in range(1, 6):
    print(i)

# C.

num = 3
if num == 1:
    print("summer")
elif num == 2:
    print("winter")
elif num == 3:
    print("fall")
elif num == 4:
    print("spring")

# D.
# 1. The loop will run 10 times
# 2. 10 will be printed last

# E.

age = 25
lastname_firstletter = "u"
usd_nis_rate = 3.22
fly_abroad = True
apartment_num = 1
info = [age,
        lastname_firstletter,
        usd_nis_rate,
        fly_abroad,
        apartment_num]

print(info)
age_currency = age + usd_nis_rate
print(age_currency)

# F.

# phone_num = input("What is your phone number? ")
# print("phone number " + phone_num)

# G.


def printHello():
    print("hello")


def calculate(age, usd_nis_rate):
    print(age+usd_nis_rate)


# H.


def print_name(name):
    print(name)


def divide_number(num):
    print(num / 2)


# I.


def addition(num1, num2):
    result = num1 + num2
    return result


def string_space(str1, str2):
    full_str = str1 + " " + str2
    return full_str


# Challenges:
# K.

string = "#"
for i in range(5):
    print(string)
    string = string + "#"

# L.

string = "#" + "     " + "#"
for i in range(0, 7):
    print(string[i])
    # string = string - string[0,1,2]

# K.

x = ""
y = "#"
spaces = "     "
spaceslen = len(spaces)
for i in range(7):
    if len(spaces) > 1:
        print(x + y + spaces + y)
        x += " "
        spaces = spaces(char[:-1] for char in spaces)

# M. Sum of a number's digits

def num_sum():
    result = 0
    number = input("Number: ")
    for x in range(len(number)):
        result = result + int(number[x])
    return result
