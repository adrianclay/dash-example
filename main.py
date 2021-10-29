import dash
from dash import dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

"""
visualise road casualty data
"""


app = dash.Dash(__name__)
server = app.server

def convert_from_CSV_to_DF(data):
    """convert csv file to dataframe"""
    converted_df = pd.read_csv(r'data', low_memory=False)
    return converted_df




df = pd.read_csv(r'data/dft-road-casualty-statistics-accident-2020.csv', low_memory=False)
df['date']= pd.to_datetime(df['date'], format="%d/%m/%Y")

# https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas-series-to-frame
number_of_accidents_per_day = df.groupby(['date']).size().to_frame('number_of_accidents')


fig = px.line(
    number_of_accidents_per_day,
    x = number_of_accidents_per_day.index,
    y = "number_of_accidents",
    title = "No. of road accidents per day in 2020",
    labels={
        "number_of_accidents": "number of accidents"
    },
    template="plotly_dark"
)


app.layout = html.Div([
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        )
    ]),
    html.Div([
    dcc.Graph(figure=fig)
])
])

if __name__ == '__main__':
    app.run_server(debug=True)
