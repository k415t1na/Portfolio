from flask import Flask, render_template, request
import os



app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caricatures")
def caricatures():
    return render_template("caricature.html")

@app.route("/portraits")
def portraits():
    return render_template("portrait.html")

@app.route("/logos")
def logos():
    return render_template("logos.html")

@app.route("/posters")
def posters():
    return render_template("poster.html")

@app.route("/tshirt")
def tshirt():
    return render_template("tshirt.html")


if __name__ == "__main__":
    #app.debug=True
    app.run()