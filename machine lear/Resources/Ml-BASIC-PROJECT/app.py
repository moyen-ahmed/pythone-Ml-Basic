import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle   
from pathlib import Path

app = Flask(__name__)
MODEL_PATH = Path(__file__).with_name("model.pkl")
with MODEL_PATH.open("rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    # output = prediction[0]
    return render_template('index.html', prediction_text='Predicted Iris Species is: {}'.format(prediction))
if __name__ == "__main__":
    app.run(debug=True)
    