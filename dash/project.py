import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from datetime import datetime as dt
from datetime import date
import pandas as pd

df = pd.read_csv('../full_course_code/Plotly-Dashboards-with-Dash/Data/NASDAQcompanylist.csv')

app = dash.Dash()


app.layout = html.Div([
    html.Div(
       'Stock Ticker Dashboard', style={'fontSize':35}
    ),
    html.Div([
        html.H1('Select Stock symbols',style={'paddingBotttom':10}),
        dcc.Dropdown(
            id='stock-name',
            options=[{'label':i,'value':j} for i, j in zip(df['Symbol'],df['Name'])],
            multi=True,
            value='ABMD'
        )
    ],style={
        'width':'30%',
        'display':'inline-block'
    }),
    html.Div([
        html.H1('Select start and end dates:',style={'paddingTop':50}),
        dcc.DatePickerRange(
            id='stock-date-picker-range',
            min_date_allowed=dt(1990,1,1),
            max_date_allowed=date.today(),
            initial_visible_month=dt(2019,7,7)
        )
    ],style={
        'width':'30%',
        'display':'inline-block'
    }),
    html.Button(id='submit-button',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24,'paddingLeft':10})
])


if __name__ == "__main__":
    app.run_server()