from collections import namedtuple

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/main')
def hello():
    return render_template('main.html', messages=messages)

@app.route('/add_message')
def add_message():
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)