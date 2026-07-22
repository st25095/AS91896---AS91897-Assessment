import datetime
import json
import sqlite3

from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_data():
    try:
        with open('data/pizzas.json') as file:
            pizzas = json.load(file)
        return pizzas
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return {}

@app.route('/')
def home():
    pizzas = load_data()
    return render_template("home.html", pizzas = pizzas)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)