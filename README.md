# Diabetes_Classification_SVM
* Built a SVM to predict a diabetes patient status with ```train_accuracy``` ~ 0.780 and ```test_accuracy ~ 0.779```
* EDA for the dataset in jupyter notebook with some notes about the data (uploaded above)
* Pre_prosseced (Standarization, splitting) the dataset 
* Built SVM and uploaded it on a web server using Flask API

## Resources
**Data Retrieved from:** https://www.kaggle.com/uciml/pima-indians-diabetes-database
**Model Build Info:** https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html?highlight=svc#sklearn.svm.SVC
**What is BMI:** https://en.wikipedia.org/wiki/Body_mass_index

## Dataset
The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

* The dataset has 768 samples, each with 8 features ```Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age```
* The dataset has more negative (*non-diabetic*) than positive samples (*diabetic*)

*Note: THE DATA ONLY HAVE ```FEMALE SAMPLES```*

## EDA 
###**You can find a full explaination of the data in the notebook above (*data_eda.ipynb*)**
Here are some of the highlights about the data:

![Alt text](https://github.com/ahmedheakl/Diabetes_Classification_SVM/blob/main/BMI_boxplot.png "BoxPlot for BMI Values")
![Alt text](https://github.com/ahmedheakl/Diabetes_Classification_SVM/blob/main/data_means_groupedby_target_vals.PNG "Mean of the dataset")

