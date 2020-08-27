from urllib.request import urlopen        #library to work with url
from bs4 import BeautifulSoup as soup     #library for web scraping
import pandas as pd


URL = "https://en.wikipedia.org/wiki/Call_of_Duty"        #website to scrape
CLASS = "wikitable sortable"        #class attribute of the table
CSV = "Call of Duty.csv"        #csv file to store data


def tableFromWikipedia(url, cl):
    
    url_req = urlopen(url)
    url_html_raw = url_req.read()

    url_html = soup(url_html_raw, parser="html")        #parsing html elements

    tables = url_html.findAll('table', {"class":cl})    #find table elements with that class

    headers = tables[0].findAll('th',{})
    headers = [h.text[:-1] for h in headers]        #adding headers


    #maintaining row content
    all_rows = tables[0].findAll('tr',{})[1:]
    rows = []
    for r in all_rows:
        content = []
        for i in r.findAll('td', {}):
            word = i.text[:-1]
            word = word.replace("," , "/")
            content.append(word)
        
        rows.append(content)
        
    return headers,rows


#write into a csv file
def writeCSV(headers, rows, file):
    
    with open(file,"w") as f:
        S = ','.join(headers)
        f.write(S+'\n')
        for r in rows:
            S = ','.join(r)
            f.write(S+'\n')


#print the dataframe(csv)
def printCSV(file):
    df = pd.read_csv(file)
    display(df.head(n=20))
    
    
if __name__=='__main__':
    headers,rows = tableFromWikipedia(URL, CLASS)
    writeCSV(headers, rows, CSV)
    printCSV(CSV)
    

