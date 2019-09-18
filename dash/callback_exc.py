import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
    html.Div(dcc.RangeSlider(
        id='slider',
        min=-5,
        max=6,
        step=1,
        value=[-1, 2],
        marks={i: str(i) for i in range(-5,7)}        
    ),style={'fontSize':14,'width':'48%'}),
    html.Br(),
    html.Br(),
    html.Div(id='slider-output')
],style={'fontFamily':'helvetica','fontSize':25})

@app.callback(Output('slider-output','children'),
              [Input('slider','value')])
def multiply_slider_values(slider_value):
    return slider_value[0]*slider_value[1]


if __name__ == "__main__":
    app.run_server()
