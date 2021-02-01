import json, os, subprocess, sys
import urllib3
import re

# pip install custom package to /tmp/ and add to path
subprocess.call('pip install bs4 -t /tmp/ --no-cache-dir'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.path.insert(1, '/tmp/')

from bs4 import BeautifulSoup

def get_data():

    """
        Refactored code for extracting the data from ncdc website in a dictionary format (key-value pair)
    """
    PAGE_URL = "https://covid19.ncdc.gov.ng/"
    
    http = urllib3.PoolManager()
    r = http.request('GET', PAGE_URL)
    # Response Data
    response_data = r.data
    # Initializing the BeautifulSoup package and the specifying the parser
    soup = BeautifulSoup(response_data, 'lxml')
    content_table = soup.find("table", id="custom1")

    # Extracting the Table header names 
    table_headers = content_table.thead.findAll("tr")
    for k in range(len(table_headers)):
        data = table_headers[k].find_all("th")
        column_names = [j.string.strip() for j in data]

    # Extracting the data in the Table's body (values)
    table_data = content_table.tbody.findAll('tr')
    values = []
    keys = []
    data_dict = {}
    for k in range(len(table_data)):
        key = table_data[k].find_all("td")[0].string.strip()
        value = [j.string.strip() for j in table_data[k].find_all("td")]
        keys.append(key)
        values.append(value)
        data_dict[key] = value
    
    data_dict["Column_names"] = column_names
    return data_dict

print(get_data())