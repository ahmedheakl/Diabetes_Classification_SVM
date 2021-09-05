import pickle
import numpy as np

'''
This function expects a list of all the values of a patient
and returns whether if he has diabetes
'''


def get_patient_status(model, X, scaler_path='scaler.sav'):
    scaler = pickle.load(open(scaler_path, 'rb'))
    X = scaler.transform(X)
    X = np.array(X)
    # Reshaping the list to a 2-d array
    X = X.reshape(1, -1)
    result = model.predict(X)[0]
    return 'Diabetic' if result == 1 else 'Non-Diabetic'
