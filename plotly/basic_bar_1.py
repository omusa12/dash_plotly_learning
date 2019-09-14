import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data/2018WinterOlympics.csv')

data = [go.Bar(x=df['NOC'],
                y=df[medal],
                name=medal,
                marker={'color':color}) for medal,color in zip(['Gold','Silver','Bronze'],
                                                    ['#FFD700','#9EA0A1','#CD7F32'])]

layout = go.Layout(title="Medals")
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)