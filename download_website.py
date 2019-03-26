from urllib.request import urlopen

def get_stock_html(ticker_name):
   opener =urlopen(urllib.HTTPRedirectHandler(),urllib.HHTPHandler(debuglevel=0),)
   opener =urllib.build_opener(urllib.HTTPRedirectHandler(),urllib.HHTPHandler(debuglevel=0),)
   opener.addheader = [
('User-agent',)]
   url = "https://finance.yahoo.com/q?s=" +ticker_name
   response = opener.open(url)
   return ''.join(response.readlines())

if __name__ == '__main__':
   print (get_stock_html('GOOG'))
