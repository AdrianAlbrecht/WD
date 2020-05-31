from lxml import html
import requests
import pandas as pd
from matplotlib import pyplot as plt

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
table_div = page.get_element_by_id('collection')
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]
labels = [label.strip() for label in table.xpath('.//th/text()')]
headers = [label for label in table.xpath('.//th')]
labels = []
for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        labels.append(anchor[0].strip())
    else:
        labels.append(header.text.strip())

#2
gry={}
for g in labels:
    if (g !='')&(g!='Shop'):
        gry[g]=[]

for a in table.xpath('.//*[@id="row_"]'):
    for b in range(len(labels)):
        if labels[b] in gry.keys():
            if labels[b] == 'Board Game Rank':
                gry[labels[b]].append(a.xpath('./td['+str(b+1)+']/a/@name')[0].strip())
            elif labels[b] == 'Title':
                gry[labels[b]].append(a.xpath('./td['+str(b+1)+']/div[2]/a/text()')[0].strip())
            else:
                gry[labels[b]].append(float(a.xpath('./td['+str(b+1)+']/text()')[0].strip()))

df=pd.DataFrame(gry)
print(df)

#3

p=df.sort_values('Num Voters',ascending=False)
print(p[:10])
wykres= p[:10].plot.bar()
plt.show()