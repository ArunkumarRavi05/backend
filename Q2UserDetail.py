import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://ful.io')
data = r.text
soup = BeautifulSoup(data, "html.parser")
print("Mail Id:")
for i in soup.find_all(href=re.compile("mailto")):
    print(i.string)
print("Social Links")
for i in soup.find_all(href=re.compile("linkedin.com")):
    print(i.string)
for i in soup.find_all(href=re.compile("\\facebook.com")):
    print(i.string)
print("Contact")
for i in soup.find_all(href=re.compile("^\\+?[1-9][0-9]{7,14}$")):
    print(i.string)
