from bs4 import BeautifulSoup
import requests
import re

def check_response(r):
    if r.status_code == 200:
        print("\nWeb request success !\n")
        return 0
    else:
        print("Web request failed !")
        return 1
    
def get_all_href_on_page(soup):
    links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
    for i in range(len(links)):
        print(links[i])

def get_top100_filenumbers_on_page(href_lists):
    ebook_links = [href for href in href_lists if href.startswith('/ebooks/')]
    ebook_ids = []
    for link in ebook_links:
        match = re.findall(r'/ebooks/(\d+)', link)
        if match:
            ebook_ids.append(match[0])
    return ebook_ids[:100]

def get_top100_ebooks_Yesterday(soup):
    line = soup.text.splitlines()
    start_index = -1
    for i, current_line in enumerate(line):
        if "Top 100 EBooks yesterday —" in current_line:
            continue
        if "Top 100 EBooks yesterday" in current_line:
            start_index = i
            break

    if start_index == -1:
        print("Error: 'Top 100 EBooks yesterday' not found in the page.")
        exit()

    top_100_ebooks = line[start_index+1:start_index+102]

    ebook_titles = []
    pattern = r'^(.*?)\s+\(\d+\)$'
    for line in top_100_ebooks:
        match = re.match(pattern, line)
        if match:
            book_info = match.group(1).strip()
            ebook_titles.append(book_info)

    for name in ebook_titles:
        print(name)

url = "https://www.gutenberg.org/browse/scores/top"
r = requests.get(url)
check_response(r)
print("-" * 50 )
html = r.content.decode(r.encoding)
soup = BeautifulSoup(html, 'html.parser')
href_lists = [a.get('href') for a in soup.find_all('a') if a.get('href')]
ebook_ids = get_top100_filenumbers_on_page(href_lists)

# แสดงจำนวน hrefs ทั้งหมดในหน้าเว็บ หากไม่ถต้องการแสดงให้คอมเมนต์บรรทัดด้านล่างนี้ออก
print("\nTotal number of hrefs on the page: ", len(href_lists))
print("\nAll hrefs on the page:")
get_all_href_on_page(soup)
print("\n" + "-"*50 + "\n")

# แสดงจำนวน filenumbers 100 อันดับแรกในหน้าเว็บ หากไม่ต้องการแสดงให้คอมเมนต์บรรทัดด้านล่างนี้ออก
print("Top 100 filenumbers on the page:")
for i in range(len(ebook_ids)):
    print(ebook_ids[i])
print("\n" + "-"*50 + "\n")

# แสดงชื่อหนังสือ 100 อันดับแรกในหมวดหมู่ "Top 100 EBooks yesterday" หากไม่ต้องการแสดงให้คอมเมนต์บรรทัดด้านล่างนี้ออก
print("Top 100 EBooks yesterday:")
get_top100_ebooks_Yesterday(soup)
print("\n" + "-"*50 + "\n")

