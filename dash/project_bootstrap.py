import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from datetime import datetime as dt
import pandas_datareader.data as web
from datetime import date
import pandas as pd
import os

df = pd.read_csv('../full_course_code/Plotly-Dashboards-with-Dash/Data/NASDAQcompanylist.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = html.Div([dbc.NavbarSimple(
    brand="Stock Ticker Dashboard",
    sticky="top",
    style={'fontSize':45}
)],style={'marginBottom': 50})

body = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H5("Select Stock symbols"),
            dcc.Dropdown(
            id='stock-name',
            options=[{'label':i,'value':i} for i in df['Symbol']],
            multi=True,
            value="TSLA"
        )
        ]),
        dbc.Col([
            html.H5("Select start and end dates:"),
            dcc.DatePickerRange(
            id='stock-date-picker-range',
            min_date_allowed=dt(2015,1,1),
            max_date_allowed=date.today(),
            start_date=dt(2018,1,1),
            end_date=dt.today()
        )
        ]),
        dbc.Col([
            dbc.Button(
                id='submit-button',
                n_clicks=0,
                children='Submit',
            )
        ])
    ]),
    dbc.Row([
        html.Div([
            dcc.Graph(
                id='stock-price-main',
                figure={
                    'data':[go.Scatter(
                        x=[1,2,3],
                        y=[1,4,9]
                    )],                    
                    'layout': go.Layout(
                        title='Stock Price time series',
                        xaxis={'title':'Date'},
                        yaxis={'title':'Price $'},
                        hovermode='closest'
                    )
                }
            )
        ],style={'width':'100%','paddingTop':150})
    ])
])

app.layout = html.Div([navbar, body])

@app.callback(Output('stock-price-main','figure'),
              [Input('submit-button','n_clicks')],
              [State('stock-name','value'),
              State('stock-date-picker-range','start_date'),
              State('stock-date-picker-range','end_date')])
def update_graph(n_clicks,stock_ticker,start_date,end_date):
    data = []
    for stok in stock_ticker:
        start = dt.strptime(start_date[:10],'%Y-%m-%d')
        end = dt.strptime(end_date[:10],'%Y-%m-%d')        
        df = web.DataReader(stok,"yahoo",start,end)
        data.append({'x':df.index,'y':df['Close']})
    fig = {
       'data':data,
       'layout':{'title':stock_ticker[0]}
    }
        
    return fig

if __name__ == "__main__":
    app.run_server()