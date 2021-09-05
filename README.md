# Diabetes_Classification_SVM
* Built a SVM to predict a diabetes patient status with ```train_accuracy``` ~ 0.780 and ```test_accuracy ~ 0.779```
* EDA for the dataset in jupyter notebook with some notes about the data (uploaded above)
* Pre_prosseced (Standarization, splitting) the dataset 
* Built SVM and uploaded it on a web server using Flask API

## Resources
**Data Retrieved from:** https://www.kaggle.com/uciml/pima-indians-diabetes-database
**Model Build Info:** https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html?highlight=svc#sklearn.svm.SVC

## Dataset
The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

* The dataset has 768 samples, each with 8 features ```Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age```

*Note: THE DATA ONLY HAVE ```FEMALE SAMPLES```*
