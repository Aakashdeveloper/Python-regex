import urllib.request
from re import findall
url="https://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)
html = response.read()
htmlstr = html.decode()

pdata = findall("\(\d{3}\) \d{3}-\d{4}",htmlstr)

for item in pdata:
    print(item)