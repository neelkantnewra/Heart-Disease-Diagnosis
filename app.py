from flask import Flask
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/heart-disease-predictor",methods=['POST','GET'])
def heartDiseasePredictor():
    if request.method == 'POST':
        result = request.form.to_dict()
        age = result['age']
        print(result)
        print(age)
        return render_template("result.html",results=result)
    return render_template("heart_disease.html")

if __name__ == "__main__":
    app.run()

    