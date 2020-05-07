import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")
#print(df)
p=df.groupby(['Plec']).agg({'Liczba':['sum']})
print(p)
wykres=p.plot.bar()
wykres.set_ylabel('Mln')
wykres.legend()
plt.title('Liczba urodzonych dzieci względem płci na przesterzeni lat 2000-2017')
plt.show()