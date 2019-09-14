import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data/mocksurvey.csv',index_col=0)

data = [go.Bar(x=df.index,y=df[question],name=question) for question in df.columns]

layout = go.Layout(title="Survey",barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
