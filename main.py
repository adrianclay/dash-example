import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)

df = px.data.iris()
fig = px.line(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)