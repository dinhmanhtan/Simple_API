import requests

# r = requests.get("https://imgs.xkcd.com/comics/python.png")

# print(r.headers)

# with open('comic.png','wb') as f:
#     f.write(r.content)

# payload = {"username":"jwer","password":"123"}
# r = requests.post("http://httpbin.org/post",data=payload)
# print(r.text)

r = requests.get("http://httpbin.org/basic-auth/jwer/123",auth=('jwer','123'))
print(r.text)