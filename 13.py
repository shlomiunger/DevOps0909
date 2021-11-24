import requests

# def write_names():
#     my_file = open("names.txt", "w")
#     for name in range(3):
#         current_name = input("Name: ")
#         my_file.write(current_name + "\n")
#     my_file.close()
#
#
# def greet_names():
#     my_file = open("names.txt", "r")
#     names = my_file.readlines()
#     for name in names:
#         print(f"Hello {name}")
#     my_file.close()
#


def read_url_file_to_json_file():
    my_file = open("urls.txt", "r")
    urls = my_file.readlines()
    urls = [line[:-1] for line in urls]
    my_json_file = open("json-urls.txt", "w")
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            # print(f"{url}:, status: {response.status_code}")

            my_json_file.write('{\n    "url": "' + url + '", \n    ' +
                               '"status_code": ' + '"' + str(response.status_code) + '"\n}\n')
    my_json_file.close()
    my_file.close()


read_url_file_to_json_file()