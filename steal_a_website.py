from requests import get

website = "http://example.com" # the target website
r = get(website)
html = r.text # the html document

if r.status_code < 400: # if there is not an error with the GET request
    print(f"succesful: {r.status_code}")
    print(html)
else:
    print(f"error: {r.status_code}")
