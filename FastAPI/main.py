from fastapi import FastAPI  # all lowercase for 'fastapi'
import uvicorn
from BankNotes import BankNote # Importing the BankNote model
import numpy as np
import pandas as pd
import pickle


# Create FastAPI instance
app = FastAPI()
pickle_in = open("model.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post('/predict')
def predict_bank_note(data: BankNote):
    variance = data.variance
    skewness = data.skewness
    curtosis = data.curtosis
    entropy = data.entropy
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if prediction[0] == 0:
        return {'prediction': 'The note is authentic'}
    else:
        return {'prediction': 'The note is not authentic'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
# BankNotes.py