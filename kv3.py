# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:23:44 2019

@author: STEM
"""

import math

def box(cd,cm,cw):
    
    print("There are", cd, "dark chocolates,", cm, "milk chocolates and", cw, "white chocolates.")
box(5,6,8)

cadbury1="milk chocolate"
cadbury2="dark chocolate"
cadbury3="white chocolate"

print(cadbury1, cadbury2, cadbury3)

cadburymilk=6
cadburydark=5
cadburywhite=8

print(cadburymilk, cadburydark, cadburywhite)

choco1={cadbury1:5}
choco2= {cadbury2:8}
choco3= {cadbury3:3}

print(choco1,choco2,choco3)

s1= "steve"
s2= "lia"
s3="vin"
s4="katie"

print(s1, "is", sas, s2, "is", sal, s3, "is",sav, s4, 'is' ,sak)

sas=32
sal=28
sav=45
sak=38

print(sas, sal, sav, sak)

sg = {"steve": "m", "lia" : "f", "vin" : "m", "katie" : "f"} 

sa = {"steve" : 35, "lia" : 28, "vin" :45, "katie" : 38}

studentlist = [["steve", 32, "m"], ["lia", 28, "f"], ["vin", 45, "m"], ["katie", 38, "f"]]





import pandas
dir(pandas)
studentdf = pandas.DataFrame(sl, columns=("name","age","gender"))
print(studentdf)

#reference specific columns in list
studentdf["name"]
studentdf["age"]

#chocolate bar graph
import plotly
from plotly.offline import plot
import plotly.graph_objs as go


cb = [["milk", 5],["dark",8],["white",3]]


chocodf = pandas.DataFrame(cb, columns=("type", "quantity"))
print(chocodf)

chocobar = go.Bar(x=chocodf["type"],y=chocodf["quantity"])
plot([chocobar])

#title graphs
titles = go.Layout(title = "number of chocolates by type")

chocobar=go.Bar(x=chocodf["type"],y=chocodf["quantity"])

fig = go.Figure(data=[chocobar], layout=titles)
plot(fig)


#student list graph

studentlist = [["steve", 32, "m"],["lia", 28, "f"],["vin", 45, "m"],["katie", 38, "f"]]
#studentlist

#import pandas

studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"),index=["1","2","3","4"])
studentdf

#plottting with bar graphs
import plotly
from plotly.offline import plot
import plotly.graph_objs as go


studentbar = go.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])











