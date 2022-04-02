'''

MIT License

Copyright (c) 2022 Neelkant Newra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''



from flask import Flask
from flask import Flask, render_template, request
import sklearn
import pickle
from assembleModel.modelcombine import combineModel

model1 = pickle.load(open("static/model/model.sav", 'rb'))
sc = pickle.load(open('static/model/scaler.pkl', 'rb'))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/heart-disease-predictor", methods=['POST', 'GET'])
def heartDiseasePredictor():
    if request.method == 'POST':
        result = request.form.to_dict()
        age = int(result['age'])
        gender = int(result['gender'])
        chest_pain_type = int(result['chest-pain-type'])
        fasting_blood_sugar = int(result['fasting-blood-sugar'])
        induced_agina = int(result['induced-agina'])
        resting_blood_pressure = int(result['resting-blood-pressure'])
        peak_exercise_st = int(result['peak-exercise-st'])
        st_depression_value = float(result['st-depressed-value'])
        heart_rate_value = int(result['heart-rate-value']) 
        serum_cholestrol_value = int(result['serum-cholestrol-value'])
        resting_ecg = int(result['resting-ecg'])
        element = sc.transform([[age, gender, chest_pain_type, resting_blood_pressure, serum_cholestrol_value,
                               fasting_blood_sugar, resting_ecg, heart_rate_value, induced_agina, st_depression_value, peak_exercise_st]])
        prediction,prediction_prob = combineModel(models=[model1],element=element)
        k = 0
        if prediction>=0.5:
            k=1
        result['prediction'] = k 
        result['prediction-prob']=prediction_prob
        
        return render_template("result.html", results=result)
    return render_template("heart_disease.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
if __name__ == "__main__":
    app.run()
