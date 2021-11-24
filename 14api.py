import requests
def fun():
    response = requests.post("http://127.0.0.1:5001/whatismyname")
    text = response.text
    print(text)

fun()