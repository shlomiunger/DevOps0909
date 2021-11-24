import requests
# from os import getenv
# response = requests.post("http://localhost:5001/whatismyname")
# print(response.text)


def test_get(url_to_test):
    response = requests.post(f"http://{url_to_test}/whatismyname")
    print(response.text)
    # print(actual)g
    # expected = "mazda, citroen, chevrolet"
    # # if expected == actual:
    # #     print("all good")
    # assert expected == actual


test_get("localhost:5001")


# def test_post(url_to_test):
#     response = requests.post(f"http://{url_to_test}/whatismyname")
#     actual = response.text
#     expected = "saved new car"
#     # if expected == actual:
#     #     print("all good")
#     assert expected == actual
#
#
# test_post("localhost:5001")
#
#
# def get_cars(url_to_test):
#     response = requests.get(f"http://{url_to_test}/cars")
#     my_file = open("cars.txt", "r")
#     expected = str(my_file.readlines())
#     actual = response.text
#     # if expected == actual:
#     #     print("all good")
#     assert expected == actual
#
#
# get_cars("localhost:5001")
