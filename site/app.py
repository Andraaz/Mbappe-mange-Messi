from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

from flask import Flask

server = Flask(__name__)

app = Dash(__name__, server=server, url_base_pathname='/app/')
jso_result = requests.get("http://localhost:5000/get_player/messi")
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

def generate_table(jso_result):
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

app.layout = html.Div(children=[
    ##html.H1(children=jso_result.text),
    html.Div(generate_table(jso_result), children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
])

#todo faire fonctionner la second epage (l'URL ne fonctionne pas)


if __name__ == '__main__':
    app.run_server(debug=True)


import calltest.py
