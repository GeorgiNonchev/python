import requests
res = requests.get('https://en.wikipedia.org/wiki/XPath')
res.raise_for_status()
playFile = open('Xpath.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
