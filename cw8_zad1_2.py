import pandas as pd
import numpy as np
import xlrd
import openpyxl

def a(df):
    #p=df.groupby(["Rok"]).agg({"Liczba":['sum']})
    #print(p[(p[('Liczba','sum')] > 1000)])
    #print(p)
    print(df[df['Liczba']>1000])
    #nie wiem o ktore rozwiazanie Panu chodzilo w sumie, wiec zostawiam obydwa :)

def b(df):
    print(df[df['Imie']=="ADRIAN"])

def c(df):
    print(df.agg({"Liczba":["sum"]}))

def d(df):
    p=df[(df['Rok']>=2000)&(df['Rok']<=2005)]
    print(p.agg({"Liczba":['sum']}))

def e(df):
    ch=df[df["Plec"]=='M']
    dz=df[df["Plec"]=='K']
    print(ch.agg({"Liczba":["sum"]}),dz.agg({"Liczba":["sum"]}), sep="\n")

def f(df):
    p=df.sort_values("Liczba", ascending=False).groupby(['Rok',"Plec"]) 
    for i,g in enumerate(p,start=1):
        print(f"{g[0]}")
        print(f"{g[1].iloc[[0],[1]].values[0][0]}", end=" ")
        print(f"{g[1].iloc[[0],[2]].values[0][0]}")

def g(df):
    dz=df[df['Plec']=='K']
    dz_max=df[df['Plec']=='K'].max()
    print(dz[(dz['Liczba']==dz_max['Liczba'])])
    ch=df[df['Plec']=='M']
    ch_max=df[df['Plec']=='M'].max()
    print(ch[(ch['Liczba']==ch_max['Liczba'])])
    


df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")
#print(df)
#a(df)
#b(df)
#c(df)
#d(df)
#e(df)
#f(df)
#g(df)

