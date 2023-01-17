from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

from flask import Flask

server = Flask(__name__)

app = Dash(__name__, server=server, url_base_pathname='/app/')
#jso_result = requests.get("http://localhost:5000/ge_player/yytyt")
jso_result = requests.get("http://localhost:5000/")
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children=jso_result.text),
    html.Div(children='''
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

# Include page2.py
import calltest.py
