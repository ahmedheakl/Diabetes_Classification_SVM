from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from predict import get_patient_status


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        keys = ['preg', 'glucose', 'bloodpressure',
                'skin', 'insulin', 'bmi', 'pedifunc', 'Age']
        X = []
        for key in keys:
            X.append(float(request.form[key]))
        model = pickle.load(open('svm_model.sav', 'rb'))
        result = get_patient_status(model, X)
        return render_template('index.html', message=result[0], color=result[1])
    else:
        return 'You need to access the predict with GET method'


if __name__ == '__main__':
    app.run(debug=True)
