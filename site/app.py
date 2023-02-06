from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

app = Dash(__name__, url_base_pathname='/app/')
data = requests.get("http://localhost:5000/get_player/messi").json()
jso_result = pd.DataFrame(data)
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

def generate_table(jso_result, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in jso_result.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(jso_result.iloc[i][col]) for col in jso_result.columns
            ]) for i in range(min(len(jso_result), max_rows))
        ])
    ])

app.layout = html.Div([
    generate_table(jso_result)
])

if __name__ == '__main__':
    app.run_server(debug=True)

