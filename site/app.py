from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__, url_base_pathname='/app/')
data = requests.get("http://localhost:5000/get_player/Yoane-Wissa").json()
jso_result = pd.DataFrame(data)
print(jso_result)
print([jso_result['Tete'][0], jso_result['Tir'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]])
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

def create_polar_chart(jso_result):
    df = pd.DataFrame(dict(
        r=[jso_result['Tete'][0], jso_result['Tir'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]],
        theta=['Tête', 'Tir', 'Dribbles', 'Passe']))

    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    return dcc.Graph(figure=fig)

app.layout = html.Div([
    create_polar_chart(jso_result)
])

if __name__ == '__main__':
    app.run_server(debug=True)
