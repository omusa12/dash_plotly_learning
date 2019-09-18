import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../full_course_code/Plotly-Dashboards-with-Dash/Data/OldFaithful.csv')

x = df['X']
y = df['Y']

app.layout = html.Div([dcc.Graph(id='scatterplot',
                    figure = {'data':[
                            go.Scatter(
                                x=x,
                                y=y,
                                mode='markers'
                            )],
                    'layout':go.Layout(title='My scatter plot',
                                        xaxis={'title':'Duration of eruptions(Minutes)'},
                                        yaxis={'title':'Interval until next eruption(Minutes)'})}
                    )])

if __name__=='__main__':
    app.run_server()
