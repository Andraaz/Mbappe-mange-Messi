from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route("/search_player/:name")
def hello_world():
    return json

@app.route('/test')
def hello():
    return redirect("http://www.example.com", code=302)

app.run(host='localhost', port=5000)