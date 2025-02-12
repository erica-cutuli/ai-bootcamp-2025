import requests
import pandas as pd
from bs4 import BeautifulSoup

'''
url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data['records'])
soup = BeautifulSoup(response, "html.parser")
'''

base_url = "https://books.toscrape.com/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, features="html.parser")
links = soup.find_all("a")
print([repr(obj) for obj in links])

link = links[0]