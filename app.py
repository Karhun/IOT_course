#Serverin flask koodi, demo 3.7
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Serveri'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
