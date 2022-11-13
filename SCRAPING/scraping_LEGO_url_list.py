from requests_html import HTMLSession
import csv

session = HTMLSession()
url = 'https://www.brickeconomy.com/sets'
url_constant = 'https://www.brickeconomy.com'

page = session.get(url)

list_of_urls = []

for theme_container in page.html.find(".theme"):
    link_to_set_page = theme_container.find("a")[0].attrs["href"]
    full_url = url_constant + link_to_set_page
    list_of_urls.append(full_url)

list_of_urls_to_scrape = [url + '\n' for url in list_of_urls]
    
with open('urls_for_scraping.txt', 'w', encoding='utf-8') as text_object:
    text_object.writelines(list_of_urls_to_scrape)