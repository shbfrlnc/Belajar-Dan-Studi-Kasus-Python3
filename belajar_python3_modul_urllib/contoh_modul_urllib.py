import urllib.request

print("mulai contoh 1")
html = urllib.request.urlopen('https://quotes.toscrape.com').read()
print(html)

print("mulai contoh 2")
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
req = urllib.request.Request('https://quotes.toscrape.com', headers = headers)
html = urllib.request.urlopen(req).read()
print(html)