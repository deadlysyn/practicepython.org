#!/usr/bin/env python
#
# practicepython.org exercise 17:
# print story list from nytimes.com


import urllib.request
from bs4 import BeautifulSoup


request = urllib.request.Request('http://nytimes.com')
response = urllib.request.urlopen(request)
html = response.read().decode()
soup = BeautifulSoup(html, 'html.parser')

for story in soup.find_all(class_="story-heading"):
    if story.a:
        print(story.a.text.replace("\n", " ").strip())
    else:
        print(story.contents[0].strip())
