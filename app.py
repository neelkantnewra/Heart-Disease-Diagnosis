from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/heart-disease-predictor")
def heartDiseasePredictor():
    return render_template("heart_disease.html")

if __name__ == "__main__":
    app.run()

    