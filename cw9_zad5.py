import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("zamowienia.csv",header=0,delimiter=";")

p=df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
#print(p)
wykres = p.plot.bar()
wykres.legend()
plt.title('Ilość zamówień złożonych przez Sprzedawców')
plt.show()
