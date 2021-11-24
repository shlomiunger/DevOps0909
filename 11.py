from time import sleep
import io

my_file = open("read_my_contents.txt")
contents = my_file.readlines()
# print(contents)
for line in contents:
    print(line, end='')

my_file.close()
# print(contents)
# sleep(5)
# will create file for you automatically as shown below:
my_file = open("names.txt", "w")
for i in range(3):
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
my_file.close()

my_file = open("names.txt", "r")
for name in my_file.readlines():
    print(f"hello {name}", end='')


try:
    my_file = open("names.txt", "r")
    for i in range(3):
        current_name = input("enter your name: ")
        my_file.write(current_name + "\n")
    my_file.close()
except io.UnsupportedOperation as e:
    print("Error: " + str(e.args))

try:
    my_file = open("na.txt", "r")
    for i in range(3):
        current_name = input("enter your name: ")
        my_file.write(current_name + "\n")
        my_file.close()
except FileNotFoundError as e:
    print("Error: " + str(e.args[1]))
