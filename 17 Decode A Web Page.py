"""
Use the BeautifulSoup and requests Python packages to print out 
a list of all the article titles on the New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
 

soup = BeautifulSoup(r_html)

for story_heading in soup.find_all(class_="meta content"): 
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())