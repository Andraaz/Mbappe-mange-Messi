from flask import Flask
from dash import Dash
import pandas as pd
app = Flask(__name__)

data_players = pd.read_csv("NotesAtq.csv")
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/get_player/<name>')
def get_info_player(name):
    #{name:{"tirs":10}}
    #data_players
    return data_players.iloc[:10].to_dict()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)