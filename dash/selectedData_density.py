import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = dash.Dash()

# CTREATE DATA
np.random.seed(10)
x1 = np.linspace(0.1,5,50)
x2 = np.linspace(5.1,10,50)
y = np.random.randint(0,50,50)

# DATAFRAME
df1 = pd.DataFrame({'x':x1,'y':y})
df2 = pd.DataFrame({'x':x1,'y':y})
df3 = pd.DataFrame({'x':x2,'y':y})

df = pd.concat([df1,df2,df3])

app.layout = html.Div([
    html.Div([
        dcc.Graph(
        id='plot',
        figure={
            'data': [go.Scatter(
                x=df['x'],
                y=df['y'],
                mode='markers'
            )],
            'layout':go.Layout(
                title='Scatterplot',
                hovermode='closest'
            )
        }
    )
    ],style={
        'width':'30%',
        'display':'inline-block'
    }),
    html.Div([
        html.H1(
            id='density',
            style={
                'padding':25
            }
        )
    ],style={
        'width':'30%',
        'display':'inline-block',
        'verticalAlign':'top'
    })
])

@app.callback(Output('density','children'),
              [Input('plot','selectedData')])
def find_density(selectedData):
    # Calculate the density
    pts = len(selectedData['points'])
    rng_or_lp = list(selectedData.keys())
    rng_or_lp.remove('points')
    max_x = max(selectedData[rng_or_lp[0]]['x'])
    min_x = min(selectedData[rng_or_lp[0]]['x'])
    max_y = max(selectedData[rng_or_lp[0]]['y'])
    min_y = min(selectedData[rng_or_lp[0]]['y'])
    area = (max_x-min_x)*(max_y-min_y)
    d = pts/area
    return 'Density = {:.2f}'.format(d)

if __name__ == "__main__":
    app.run_server()
