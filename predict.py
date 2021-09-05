import pickle
import numpy as np

'''
This function expects a list of all the values of a patient
and returns whether if he has diabetes
'''


def get_patient_status(model, X, scaler_path='scaler.sav'):
    scaler = pickle.load(open(scaler_path, 'rb'))

    # Reshaping the list to a 2-d array
    X = np.array(X).reshape(1, -1)
    X = scaler.transform(X)

    result = model.predict(X)[0]
    return ('Srry, you have Diabetes', 1) if result == 1 else ("Congrats, you don't have diabetes!", 0)
