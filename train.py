import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

# loading the dataset
df = pd.read_csv('diabetes.csv')


# separating target data from features
df_y = df.Outcome
df_x = df.drop(columns=['Outcome'], axis=1)

# Checking our data
# print(df_y.head(), '\n\n', df_x.head())

# Make the data standard (uniting the means and ranges for all cols)
scaler = StandardScaler().fit(df_x)
df_x_scaled = scaler.transform(df_x)

# Spliting the data into train and test

'''
I used stratify to split the data evenly based on the type of patients.
That is, i want each test and train set to half equal proportions of 
diabetics and non-diabetics
'''
X_train, X_test, y_train, y_test = train_test_split(
    df_x_scaled, df_y, test_size=0.2, random_state=0, shuffle=True, stratify=df_y)

print(X_train.shape)
print(X_test.shape)

# Initializing and training our model
classifier = SVC(kernel='linear',)
classifier.fit(X_train, y_train)

# Evaluating the model using accuracy scores
print(f'Train accuracy: {classifier.score(X_train, y_train):.3f}')
print(f'Test accuracy: {classifier.score(X_test, y_test):.3f}')

'''
It is obvious that the model's both train and test accuracies 
scores are close, which indicates that the model has not overfit the data
'''

print(classifier.predict(X_train[0].reshape(1, -1)))

# Saving the model for later use
'''
I'm using pickle to serialize the model
'''
pickle.dump(classifier, open('svm_model.sav', 'wb'))

# Saving the scaler model
pickle.dump(scaler, open('scaler.sav', 'wb'))
