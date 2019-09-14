import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

df = pd.read_csv('data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

data = [go.Scatter(x=df['LST_TIME'],
                    y=df[df['DAY']==day]['T_HR_AVG'],
                    mode='lines',
                    name=day) for day in df['DAY'].unique()]

layout = go.Layout(title='Daily tem avgs')
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig)