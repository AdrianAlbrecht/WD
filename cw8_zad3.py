import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime

def a(df):
    print(df.Sprzedawca.unique())

def b(df):
    p=df.sort_values('Utarg',ascending=False)
    print(p.iloc[:5])

def c(df):
    p=df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
    print(p)

def d(df):
    p=df.groupby(['Kraj']).agg({"idZamowienia":['count']})
    print(p)

def e(df):
    p=df.copy()
    p['year']=pd.DatetimeIndex(p['Data zamowienia']).year
    p=p.groupby(["year",'Kraj']).agg({"idZamowienia":['count']})
    print(p.index.values[5],p.values[5])

def f(df):
    p=df.copy()
    p['year']=pd.DatetimeIndex(p['Data zamowienia']).year
    p=p.groupby(["year"]).agg({"Utarg":['mean']})
    print(p.index.values[1],p.values[1][0])

def g(df):
    p=df.copy()
    p['Rok']=pd.DatetimeIndex(p['Data zamowienia']).year
    cztery=p[p["Rok"]==2004].copy()
    cztery=cztery.drop(['Rok'],axis=1)
    cztery.to_csv('zamowienia_2004.csv',header=True, index=False)
    pic=p[p["Rok"]==2005].copy()
    pic=pic.drop(['Rok'],axis=1)
    pic.to_csv('zamowienia_2005.csv',header=True, index=False)

df= pd.read_csv("zamowienia.csv",header=0,delimiter=";")
#print(df)
#a(df)
#b(df)
#c(df)
#d(df)
#e(df)
#f(df)
g(df)