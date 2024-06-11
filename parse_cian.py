import urllib.request
from bs4 import BeautifulSoup as bs

BASE_URL = "https://habarovsk.cian.ru/cat.php?deal_type=sale&engine_version=2&location%5B0%5D=4811&offer_type=flat&p=1"

# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}

req = urllib.request.Request(BASE_URL)

r = urllib.request.urlopen(req).read().decode('utf-8')

# with open("PARSED_DATA.txt", 'w', encoding="utf-8") as file:
#     file.write(r)

soup = bs(r, 'html.parser')
elements = soup.find_all(attrs={"data-testid":"offer-card"})
with open("PARSED_DATA.txt", 'w', encoding="utf-8") as file:
    for elem in elements:
        print(elem, file=file)
    
# print(elements)