from flask import Flask, render_template, request
from dash import dcc, html, Input, Output, callback


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def form():
    Employee_Name = request.form.get("Employee-Name")
    return render_template("form.html", name=Employee_Name)
