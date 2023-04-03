from flask import Flask, render_template
import os

os.system("clear")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host = "0.0.0.0" , debug=True)