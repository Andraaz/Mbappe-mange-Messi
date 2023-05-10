from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

app = Dash(__name__, url_base_pathname='/app/', external_stylesheets=[dbc.themes.BOOTSTRAP])
data = requests.get("http://localhost:5000/get_player/Ola-Aina").json()
jso_result = pd.DataFrame(data)
print(app)
data_players = pd.read_csv("notesGlobales.csv")
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div([
    html.H1(children='En sah, les meilleurs joueurs de foot', style={'textAlign':'center'}),
    dcc.Dropdown(data_players['Player'], data_players['Player'].iloc[0], id='dropdown-selection'),
    dbc.Row([
        #TODO CHATGPT OU SYNTHAXE (UNE COL POUR LE GRAPH ET UNE POUR LE GRAPHIQUE)
        dbc.Col([
            dcc.Graph(id='graph-content')
        ]),
        dbc.Col([
    dbc.Card([
            dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/static/images/portrait-placeholder.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4(id="namePlayer"),
                            html.P(
                                id="ligue"),
                            html.P(
                                id="nation"
                            ),
                            html.P(
                                id="equipe"
                            ),
                            html.P(
                                id="puissance"
                            ),
                            html.Small(
                                "Copyright © entrepriseTopBudget",
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
            ],className="g-0 d-flex align-items-center")
    #create_polar_chart(jso_result)
])
@callback(
    [Output('graph-content', 'figure'), Output("namePlayer", "children"),
     Output("ligue", "children"), Output("nation", "children"), Output("equipe", "children"), Output("puissance", "children")],
    Input('dropdown-selection', 'value')
)
def graph_and_cart(value):

    #Graphique
    data = requests.get(f"http://localhost:5000/get_player/{value}").json()
    jso_result = pd.DataFrame(data)
    if str(jso_result['Pos'][0]).startswith('FW'):
        #Attaque
        df = pd.DataFrame(dict(
            r=[jso_result['Tete'][0], jso_result['Tir'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]],
            theta=['Tête', 'Tir', 'Dribbles', 'Passe']))
    elif str(jso_result['Pos'][0]).startswith('DF'):
        #Défenseur
        df = pd.DataFrame(dict(
            r=[jso_result['Tete'][0], jso_result['Tacle'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]],
            theta=['Tête', 'Tacle', 'Dribbles', 'Passe']))
    elif str(jso_result['Pos'][0]).startswith('MF'):
        #Millieu
        df = pd.DataFrame(dict(
            r=[jso_result['Block'][0], jso_result['Tir'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]],
            theta=['Block', 'Tir', 'Dribbles', 'Passe']))
    
    fig = px.line_polar(data_frame=df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')

    #Carte
    try:
        bigName = value.split("-")
        prenom = bigName[0]
        nom = bigName[1]
    except:
        prenom = value
        nom = ""
    ligue = jso_result['Comp'][0]
    nationalite = jso_result['Nation'][0]
    noteFinale = jso_result['Note Finale'][0]
    squad = jso_result['Squad'][0]
    rankEquipe = jso_result['classement_equipe']
    card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/static/images/portrait-placeholder.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4(prenom + " " + nom, className="card-title"),
                            html.P(
                                "🏆 Ligue : " + ligue + ""
                            ),
                            html.P(
                                "🌎 Nation : " + str(nationalite) + ""
                            ),
                            html.P(
                                "🔰 Équipe : " + str(squad) + ""
                            ),
                            html.P(
                                "🧮 Puissance : " + str(noteFinale) + ""
                            ),
                            html.Small(
                                "Copyright © entrepriseTopBudget",
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"width": "100%", "maxWidth": "540px", "margin": "0 auto"},
    )
    
    name = prenom + " " + nom
    ligueName = "🏆 Ligue : " + ligue + ""
    equipe = "🔰 Équipe : " + str(squad) + ""
    puissance = "🧮 Puissance : " + str(noteFinale) + ""
    nation = "🌎 Nation : " + str(nationalite) + ""
    return fig, name, ligueName, equipe, puissance, nation


# def generate_table(jso_result, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in jso_result.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(jso_result.iloc[i][col]) for col in jso_result.columns
#             ]) for i in range(min(len(jso_result), max_rows))
#         ])
#     ])

def create_polar_chart(jso_result):
    if str(jso_result['Pos'][0]).startswith('FW'):
        #Attaque
        df = pd.DataFrame(dict(
            r=[jso_result['Tete'][0], jso_result['Tir'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]],
            theta=['Tête', 'Tir', 'Dribbles', 'Passe']))
    elif str(jso_result['Pos'][0]).startswith('DF'):
        #Défenseur
        df = pd.DataFrame(dict(
            r=[jso_result['Tete'][0], jso_result['Tacle'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]],
            theta=['Tête', 'Tacle', 'Dribbles', 'Passe']))
    elif str(jso_result['Pos'][0]).startswith('MF'):
        #Millieu
        df = pd.DataFrame(dict(
            r=[jso_result['Block'][0], jso_result['Tir'][0], jso_result['Dribbles'][0], jso_result['Passe'][0]],
            theta=['Block', 'Tir', 'Dribbles', 'Passe']))
    
    fig = px.line_polar(data_frame=df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True)
