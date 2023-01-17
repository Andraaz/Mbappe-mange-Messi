from app import app

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

@app.server.route('/app/page2')
def serve_layout():
    return html.Div([
        html.H1('This is page 2'),
        html.Div([
            "Input: ",
            dcc.Input(id='my-input', value='initial value', type='text')
        ]),
        html.Br(),
        html.Div(id='my-output'),
    ])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'
