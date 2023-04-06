
import requests
from bs4 import BeautifulSoup

response = requests.get(
        'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup')
url = BeautifulSoup(response.text, 'html.parser')
s = url.img
   
n1 = s.find("s", 0, 80)


print(n1)
n2 = s.find('>')

s1 = s[s[n1] : s[n2]]

print(s)


print(s1)
