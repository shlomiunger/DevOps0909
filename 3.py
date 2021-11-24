isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if a == 2 and strOne == "One" or strThree == "Three":
    print("a is 2")
elif a == 3:
    print("a is 3")
else:
    print("a is not 2")

d = e = 1
print(d)

#if, or, and, not

names = ["yaniv", "tom", "liran", "ben"]

if names[0] == "shahar" or \
    names[1] == "shahar" or \
    names[2] == "shahar" or \
    names[3] == "shahar":
    print("we've found shahar")
#above is long but also,
#with below, you can add names later without adding more conditions.
if "shahar" in names:
    print("we've found shahar")
other_names = ["yaniv", "tom", "liran", "ben"]
a = 5
d = 5
if a == d:
    print("a euals d")
if a is d:
    print("a is d")

print(type(names))
print(list)

my_empty_list = []
if my_empty_list:
    print("empty list evaluates to False with Value list evaluates true")

if len(my_empty_list) + 3 < 5:
    print("List + 3 is less than 5")

print(list(range(100, 5, -5)))

# print each item in the list | it will print each item since the range equals
for i in range(len(names)):
    print(names[i])

while a < 10:
    print("a is not yet 10")
    a = a + 1
    if a == 5:
        break
# break will stop loop
a = 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print("5 will be skipped")
# continiue will skip this iteration and print only 9 times

# two ways to skip iteration in loop if i is divisible by 7 i.e. skips 7 14 21 70 etc.
for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)

print(7 * 7)

def print_name(name):
    print("Hi " + name)


print_name('shlomi')

number=2
if number == 1:
    print("summer")
elif number == 2:
    print("winter")
elif number == 3:
    print("fall")
elif number == 4:
    print("spring")

def name():
    your_name = input("What's your name?: ")
    print(your_name)


name()
input()