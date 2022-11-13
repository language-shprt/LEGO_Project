from requests_html import HTMLSession
import csv
from datetime import date

session = HTMLSession()
# The website we want data from
web = 'https://www.brickeconomy.com'

today = str(date.today()).replace('-', '_')

# Reads all urls we have prepared for scrraping - LEGO themes (see 'scraping_LEGO_url_list.py')
with open('urls_for_scraping.txt', encoding='utf=8') as text_object:
    urls_in_file = text_object.readlines()

# Removes some symbols from each url
urls_ready_to_scrape = [url.replace('\n', '').replace(' ', '') for url in urls_in_file]

# All the information for each set
all_info_about_sets = []

def copy_theme_for_set(row):
    theme = row.find(".ctlsets-left .mb-2")[0].text
    theme = theme.replace('Theme / Subtheme', '').replace('Theme', '').lstrip()
    return theme

def copy_number_and_name_for_set(row):
    number_and_name = row.find(".mb-5 > h4")[0].text
    return number_and_name

def copy_price_for_set(row):
    price = row.find("td.ctlsets-right.text-right")[0].text
    price = price.split(' ')[1].replace(',', '.')
    return price
    
def copy_rating_for_set(row):
    number_and_name_html = row.find(".mb-5 > h4")[0]
    child_web_link = number_and_name_html.find("a")[0].attrs["href"]
    full_url_leads_to_rating = web + child_web_link
    page_internal = session.get(full_url_leads_to_rating)
    # Some sets do not have data about rating, but we still want to keep them in our dataset (don't skip them!)
    try:
        rating = page_internal.html.find(".col-xs-3.text-center > .mt-0.mb-0")[0].text
        return rating
    except:
        return 'NULL'

def add_record_to_final_table(list_of_all_sets, col_1, col_2, col_3, col_4):
    # Adds inforamtion about the current set to the list        
    list_of_all_sets.append([col_1, col_2, col_3, col_4])

def create_final_report(report_data):
    # Structures and creates a csv file with all the information we wanted
    column_names = ['theme', 'set_number_and_name', 'price', 'rating']
    report_name = 'scraping_data_all_sets_' + today + '.csv'
    _create_csv_file(column_names, report_name, report_data)

def _create_csv_file(column_names, report_name, report_data):
    with open(report_name, 'w', encoding='utf-8', newline='') as file_object:
        writing_data = csv.writer(file_object)
        writing_data.writerow(column_names)
        writing_data.writerows(report_data)

# Starts to loop through the list of urls
for url in urls_ready_to_scrape:
    page = session.get(url)
    print(f'Scraping data from this url now: {url}')
    # Finds and parces table for each theme - each row of this table is a set
    for set_container in page.html.find(".table.table-hover.ctlsets-table"):
        list_of_rows = set_container.find("tr")
        print(f'Found {len(list_of_rows)} rows')
        for index in range(len(list_of_rows)):
        # Taking only odd rows (each second row is empty due to the page design) 
            if index % 2 != 0:
                current_row = list_of_rows[index]        
                add_record_to_final_table(
                    all_info_about_sets, 
                    copy_theme_for_set(current_row), 
                    copy_number_and_name_for_set(current_row), 
                    copy_price_for_set(current_row), 
                    copy_rating_for_set(current_row))

create_final_report(all_info_about_sets)