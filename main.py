"""
visualise road casualty data
"""

import dash
from dash import dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server


def extract_road_casualty_statistics(csv_filepath):
    """Take in a CSV filepath and return a dataframe"""
    converted_df = pd.read_csv(csv_filepath, low_memory=False)
    converted_df['date'] = pd.to_datetime(converted_df['date'], format="%d/%m/%Y")
    return converted_df


df = extract_road_casualty_statistics(
    'data/dft-road-casualty-statistics-accident-2020.csv')


# https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas-series-to-frame
number_of_accidents_per_day = df.groupby(
    ['date']).size().to_frame('number_of_accidents')


fig = px.line(
    number_of_accidents_per_day,
    x=number_of_accidents_per_day.index,
    y="number_of_accidents",
    title="No. of road accidents per day in 2020",
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
