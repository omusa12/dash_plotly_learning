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
            options=[{'label':i,'value':j} for i, j in zip(df['Symbol'],df['Name'])],
            multi=True,
            value='ABMD'
        )
        ]),
        dbc.Col([
            html.H5("Select start and end dates:"),
            dcc.DatePickerRange(
            id='stock-date-picker-range',
            min_date_allowed=dt(1990,1,1),
            max_date_allowed=date.today(),
            initial_visible_month=dt(2019,7,7)
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
             [Input('stock-name','value'),
             Input('stock-date-picker-range','start_date'),
             Input('stock-date-picker-range','start_date')])
def update_graph(stock_ticker,start_date,end_date):
    df = web.DataReader(stock_ticker,"av-daily",start_date,end_date,access_key=os.getenv('ALPHAVANTAGE_API_KEY'))
    fig = {
        'data':[{'x':df.index,'y':df['close']}],
        'layout':{'title':stock_ticker}
    }
    return fig


if __name__ == "__main__":
    app.run_server()