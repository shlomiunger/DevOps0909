import requests
# my_variable = int(input("Enter first number: "))
# my_other_variable = int(input("Enter second number: "))
# # result = my_variable / my_other_variable
# # print(result)
# try:
#     requests.get("htpp://github.com")
# except ValueError as e:
#     print("enter a normal number")
# except ValueError as e:
#     print("enter a normal number")
# except BaseException as e:
#     print("something went wrong, check this: " + str(e.args))
# print("hello again")


def get_user_age():
    input_from_user = int(input("enter your positive age: "))
    if input_from_user < 0:
        raise ValueError("Age can not be negative")

try:
    get_user_age()
except ValueError as e:
    print(e.args[0])

