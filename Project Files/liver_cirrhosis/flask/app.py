

from flask import Flask, render_template, url_for, flash, redirect
import joblib
import numpy as np
from flask import request

app = Flask(__name__, template_folder = "templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/liver")
def liver():
    return render_template("liver.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 10):
        loaded_model = joblib.load(r"rf_acc_100.pkl")
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/predict", methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        if (len(to_predict_list) == 10):
            result = ValuePredictor(to_predict_list, 10)
            
            if(int(result)==1):
                prediction = "Sorry, you have chances of getting the disease. Please consult the doctor immediately"
            else:
                prediction = "No need to fear! You have no dangerous symptoms of the disease."
            return(render_template("result.html", prediction_text=prediction))       

if __name__ == "__main__":
    app.run(debug=True)