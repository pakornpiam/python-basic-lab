from bs4 import BeautifulSoup
from urllib.request import urlopen


url = 'https://www.pttor.com/th/oil_price'
webopen = urlopen(url) # open web with out web browzer
html_page = webopen.read()
#print(html_page)
#webopen.close()
#print(html_page)

data = BeautifulSoup(html_page,'html.parser')# bs4 help to decode  to thai 
print(data)
temp = data.find('td',{'data-v-223e48cc'})
#print (temp.text)

####


