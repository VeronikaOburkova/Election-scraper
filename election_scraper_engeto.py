"""
election_scraper_engeto.py
author: Veronika Obůrková
email: oburkova.veronika@gmail.com
discord: veronika007
"""
import csv
from requests import get
from bs4 import BeautifulSoup 
import sys

def get_page(url):
    response = get(url)
    return BeautifulSoup(response.text, features="html.parser") 


"""
    FUNCTION scrape_web_page SCRAPES INFORMATION ABOUT ELETCTION RESULTS FROM GIVEN WEB PAGE AND STORES IT IN A DICTIONARY.
"""
def scrape_web_page(url):
    soup = get_page(url)
    extracted_data = {}
    all_tr = soup.find_all("tr")   
    for tr in all_tr:
        try:
            td = tr.find('td', class_='cislo')
            code = td.find('a').string
            url = td.find('a', href= True)
            data_url_location = "https://volby.cz/pls/ps2017nss/"+url['href']
            location = tr.find('td', class_="overflow_name").string
            soup2 = get_page(data_url_location)
            table_data2 = soup2.find_all("td", class_ ='cislo')
            registred = table_data2[3].string
            envelopes = table_data2[4].string
            valid = table_data2[7].string
            extracted_data[code] = {
                'Kód obce' : code,
                'Název obce': location,
                'URL obce' : data_url_location,
                'Voliči v seznamu' : registred,
                'Vydané obálky' : envelopes,
                'Platné hlasy' : valid,
            }

            table2 = soup2.find_all('table', class_='table')
            trs_2 = table2[1].find_all('tr') 
            trs_3 = table2[2].find_all('tr')
            
            for tr in trs_2:
                try:       
                    political_party = tr.find('td',class_ = "overflow_name").text
                    votes = tr.find('td', {"class" : "cislo", "headers" : "t1sa2 t1sb3"}).text
                    extracted_data[code][political_party] = votes
                except AttributeError:
                   continue

            for tr in trs_3:
                try:       
                    political_party = tr.find('td',class_ = "overflow_name").text
                    votes = tr.find('td', {"class" : "cislo", "headers" : "t2sa2 t2sb3"}).text
                    extracted_data[code][political_party] = votes
                except AttributeError:
                    continue
    
        except AttributeError:
            continue
        
    return extracted_data


"""
    IT RETRIEVES THE HEADER FOR OUR CSV FILE FROM A GIVEN WEB PAGE WITH ELECTION RESULTS.
"""
def get_header(url):
    soup = get_page(url)
    try:
        location = soup.find('td', attrs= {'class': 'cislo', 'headers': 't1sa1 t1sb1'}).a
        url_location = "https://volby.cz/pls/ps2017nss/"+location['href']
        soup_2 = get_page(url_location)
        political_parties = soup_2.find_all('tr')
        header = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]
    except AttributeError:
        print("ERROR IN DOWNLOADING OR PROCESSING DATA, CHECK THE DATA, PLEASE. ENDING THE PROGRAM.")
        quit()
            
    for i in political_parties:
        try:
            party = i.find('td', class_='overflow_name').string
            header.append(party)
        except AttributeError:
            continue
    return list(header)


"""
    IT EXTRACTS DATA TO CSV FILE.
"""
def write_to_csv(extracted_data,output_file,url):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = get_header(url)
        writer.writerow(header)
        for location_data in extracted_data.values():
            obec_data_filtered = {key: location_data[key] for key in header}
            writer.writerow(obec_data_filtered.values())


"""
    IT CHECKS NUMBER OF GIVEN ARGUMENTS, VALID URL AND IF FILE NAME CONTAINS .csv EXTENSION.
"""
def check_arguments(argv):
    if len(argv) != 3:
        print("WRONG NUMBER OF ARGUMENTS! YOU MUST ENTER EXACTLY 2 ARGUMENTS!")
        quit()
    elif "https://volby.cz/pls/ps2017nss/" not in argv[1]:
        print("INVALID URL")
        quit()
    elif not argv[2].endswith(".csv"):
        print(" NAME OF FILE MUST HAVE A .csv EXTENSION")
        quit()


"""
    FUNCTION main SCRAPES RESULTS AND SAVES THEM TO OUR CSV FILE.
"""
def main(url,output_file):
    try:
        print(f"DOWNLOADING DATA FROM GIVEN URL: {sys.argv[1]}'\n")
    except AttributeError:
        print("UNEXPECTED ERROR, CLOSING THE PROGRAM.")
        quit()
    
    extracted_data = scrape_web_page(url)
    print(f"FILE SAVED AS: '{output_file}'")
    write_to_csv(extracted_data,output_file,url)
    print("CLOSING THE ELECTION SCRAPER")


if __name__ == '__main__':
    check_arguments(sys.argv)
    main(sys.argv[1], sys.argv[2])
