import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

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
tables = soup.find_all('table')
print(f"The web page contains {len(tables)} tables in total.")
gdp_table = None
for table in tables:
    caption = table.find('caption')
    if caption and 'GDP' in caption.text:
        gdp_table = table
        break
if gdp_table:
    header = gdp_table.find_all('th', {'colspan': '2'})
    if header:
        print(f"We found {len(header)} header rows indicating info sources as follows.")
        header_text = [re.sub(r'\[\d+\]', '', h.text.strip()) for h in header]
        print(header_text)

        df = pd.read_html(str(gdp_table))[0]
    
    # ทำความสะอาด DataFrame
    df.columns = [re.sub(r'\[.*?\]', '', col).strip() for col in df.columns]  # ลบอ้างอิงในชื่อคอลัมน์
    df = df.dropna(how='all')  # ลบแถวที่ไม่มีข้อมูลทั้งหมด
    
    # ตรวจสอบโครงสร้างของ DataFrame
    print("Extracted DataFrame:")
    print(df.head())
    
    # สร้าง DataFrame ใหม่ที่มี 3 คอลัมน์: Rank, Country, GDP (IMF)
    if 'IMF' in df.columns:
        gdp_imf_df = df[['Rank', 'Country', 'IMF']].copy()
        gdp_imf_df.rename(columns={'IMF': 'GDP (million US$)'}, inplace=True)
        
        # ทำความสะอาดข้อมูล GDP (ลบ comma และแปลงเป็นตัวเลข)
        gdp_imf_df['GDP (million US$)'] = gdp_imf_df['GDP (million US$)'].replace(',', '', regex=True).astype(float)
        
        # แสดง DataFrame ที่ได้
        print("Cleaned DataFrame (IMF):")
        print(gdp_imf_df.head())
    else:
        print("The 'IMF' column was not found in the table.")
else:
    print("No GDP table found.")