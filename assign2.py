import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
count_num = int(input('Enter count: '))
pos = int(input('Enter position: '))


def parseHtml(url, pos):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    i = 0
    for tag in tags:
        i += 1
        if i == pos:
            return tag.get('href', None)

current_num = 0
while current_num < count_num:
     print('Retrieving: ', url)
     url = parseHtml(url, pos)
     current_num += 1

print('The Last URL of this turn:', url)
