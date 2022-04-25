import time
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS
import sms

# set URL to monitor
url = Request('https://www.whitneybethesda.com/availableunits.aspx',
            headers={'User-Agent': 'Mozilla/5.0'})

# set data to monitor 
element = 'td'
attribute = 'data-label'
tag_name = 'Apartment'

# set monitoring frequency (seconds)
frequency = 3600

# set phone numbers to send updates - choose carriers from options in sms.py
phone1 = '1234567890'
phone1_carrier = sms.carriers['verizon']

phone2 = '1234567890'
phone2_carrier = sms.carriers['att']

# method to scrape page data
def get_list_of_specified_tag(element, attribute, tag_name, html):
    soup = BS(html, 'html.parser')
    return soup.find_all(element, attrs={attribute: tag_name})

# begin monitoring the specified url and data
print("Starting Page Monitoring...")
while True:
    try:
        # get intitial scrape
        response = urlopen(url).read()
        tag_list = get_list_of_specified_tag(element, attribute, tag_name, response)

        time.sleep(frequency)

        # get new scrape
        response = urlopen(url).read()
        tag_list_new = get_list_of_specified_tag(element, attribute, tag_name, response)
        
        # compare and notify
        if tag_list_new == tag_list:
            print('Nothing Changed')
            continue
        else:
            print('Something Changed ')
            sms.send('Something Changed', phone1, phone1_carrier)
            sms.send('Something Changed', phone2, phone2_carrier)
            continue
            
    # handle exceptions
    except Exception as e:
        print("Error Processing Page Status")

