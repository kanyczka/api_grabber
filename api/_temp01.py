import requests
import webbrowser
from bs4 import BeautifulSoup

def clean_soup(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
    for s in soup(['script', 'style']):
        s.decompose()
    return ' '.join(soup.stripped_strings)

        # ' '.join(soup.stripped_strings)


link = "https://www.crummy.com"

# webbrowser.open_new(link)
response = requests.get(link)
if response:
    data = response.text
    print(clean_soup(data))
else:
    print(response.status_code)
# headers = response.headers