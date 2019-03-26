import csv
import time
import os

import sys
from bs4 import BeautifulSoup

try:
    import urllib2
except:
    import urllib.request as urllib2


field_order = ['date', 'last_trade','change','ah_price', 'ah_change']
fields = {'date': 'Date', 'last_trade': 'Last_Trade','change':'Change', 
          'ah_change': 'After hours Price',
          'ah_change': 'After Hours Change'}

def get_stock_html(URL):
        opener = urllib2.build_opener(
                urllib2.HTTPRedirectHandler(),
                urllib2.HTTPHandler(debuglevel=0),
                )
        opener.addheaders = [
                ('User-agent',
                 'Mozilla/4.0 (compatible;MSIE 7.0;'
                 'Windows NT 5.1; .NET CLR 2.0.50727;'
                 '.NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
                 ]
        url = "http://proxy.com.ru/%s" % URL
        response = opener.open(url)
        return str(b''.join(response.readlines()))
def parse_stock_html(html, ticker_name):
    quote = find_quote_section(html)
    result = {}
    tick = ticker_name.lower()
    result['stock_name'] = quote.find('h2').contents[0]
    return result

def find_quote_section(html):
    soup = BeautifulSoup(html)        
    quote = soup.find('div', attrs={'class': 'yfi_rt_quote_summary'})
    return quote


def write_raw(ticker_name, stock_values):
   file_name = "Stocktracker-" + ticker_name + ".csv"
   if os.access(file_name, os.F_OK):
      file_mode = 'ab'
   else:
      file_mode = 'wb'
   
   csv_writer = csv.DictWriter(open(file_name, file_mode),fieldnames = field_order, extrasaction='ignore')

   if file_mode  == 'wb':
      csv_writer.writerow(fields)
   csv_writer.writerow(stok_values)

if __name__ == '__main__':
   html = get_stock_html('GOOG')
   stock = parse_stock_html(html, 'GOOG')
   stock['date'] = time.strftime("%Y-%m-%d %H:%M")
   write_row('GOOG',stock)
   print ('Stock')


