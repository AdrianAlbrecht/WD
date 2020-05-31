from bs4 import BeautifulSoup
import urllib3
import pandas as pd

url='https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page='
http=urllib3.PoolManager()
li={'Tytul':[], 'Platforma':[], 'Data_wydania':[], 'Ocena':[]}
zupka=BeautifulSoup(http.request('GET',url+'0').data,'lxml')
for elem in zupka.find_all('table'):
    for strink in elem.find_all('td',{'class':'clamp-summary-wrap'}):
        li['Tytul'].append(strink.find('h3').string.strip())
        for trybik in strink.find_all('div'):
            if trybik['class'] == ['clamp-score-wrap']:
                li['Ocena'].append(float(trybik.find('div').string.strip()))
            elif trybik['class'] == ['clamp-details']:
                 li['Platforma'].append(trybik.find('span',{'class':'data'}).string.strip())
                 li['Data_wydania'].append(trybik.find('span',{'class':None}).string)
df=pd.DataFrame(li)
print(df)