# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:26:15 2019

@author: STEM
"""

import pandas as pd

import plotly
from plotly.offline import plot
import plotly.graph_objs as go

#pd replaces the word 'pandas'

wodf = pd.read_excel("GISdata.xlsx", sheet_name ="womenOccupation")
wodf

wodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
plot([womenoccupation])
#start bar graph
womenoccupation = go.Bar(x= wodf["occupation"], y=wodf["women"], 
                       marker ={"color": wodf["women"], "colorscale" : "Jet"})

plot([womenoccupation])

#how to title, and label axis titles
titles = go.Layout(title = "Women in Occupations", 
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",)),
                   yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",)))


fig = go.Figure(data=[womenoccupation], layout=titles)
plot(fig) 

#star

wodf = pd.read_excel("GISdata.xlsx", sheet_name ="cancercases")
wodf

wodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
plot([womenoccupation])





