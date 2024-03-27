from markupsafe import escape

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "curr_bal": 10000,
        "transactions": [
            {
                "date":"202040301",
                "amount":500,
                "description":"Oder",
                "category":"Pet Expense"
            },
            {
                "date":"202040301",
                "amount":9.50,
                "description":"Foodlion",
                "category":"Groceries"
            },
        ]
    }
    return render_template('home.html', data=data)
    # return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"<p>Hello, {escape(name)}"