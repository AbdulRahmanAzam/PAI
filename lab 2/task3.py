def convert(url):
    return url[11:]

url = (input("enter URL that should starts with http://www.") + ".com")

print(convert(url))
