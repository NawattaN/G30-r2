import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def print_dataframe(df):
    print("-" * 80)  # Line to split header and value
    print(df[['Index', 'Rank', 'Country', 'GDP (million US$) by IMF']])
    print("-" * 80)
    print(df[['Index', 'Rank', 'Country', 'GDP (million US$) by World Bank']])
    print("-" * 80)
    print(df[['Index', 'Rank', 'Country', 'GDP (million US$) by United Nations']])

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
if response.status_code == 200:
    print("Request to https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal) successful !!")
    print("Status code: " + str(response.status_code) + " -- OK")
else:
    print("Request to https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal) failed !!")
    print("Status code: " + str(response.status_code) + " -- ERROR")
    exit(1)
table = soup.find_all("table")
print(f"The web page contains {len(table)} tables in total.")
tbody = table[2].find_all("tbody")
th = tbody[0].find_all("th", {"colspan": "2"})
header = []
for i in th:
    clean_text = re.sub(r'\[.*?\]', '', i.get_text(strip=True))
    header.append(clean_text)
print(f"We found {len(header)} header rows indicating info sources as follows.")
print(header)

data_table = soup.find("table", {"class": "wikitable"})
data_headers = []


for x in data_table.find_all("tr"):
    for y in x.find_all("th"):
        data_headers.append(y.get_text(strip=True))
        

table_values = []
for x in data_table.find_all("tr")[1:]:
    td_tag = x.find_all("td")
    td_values = [y.text.strip() for y in td_tag]
    table_values.append(td_values)
data_headers.remove(data_headers[1])
data_headers.remove(data_headers[1])
data_headers.remove(data_headers[1])

df = pd.DataFrame(table_values, columns=data_headers)
df = df.drop(index=0).reset_index(drop=True)
df.insert(0, 'Index', range(0, len(df)))
df.insert(1, 'Rank', df['Index'])
df = df.drop(columns=['Year'])
df.columns = ['Index', 'Rank', 'Country', 'GDP (million US$) by IMF', 
              'GDP (million US$) by World Bank', 'GDP (million US$) by United Nations']

print_dataframe(df)