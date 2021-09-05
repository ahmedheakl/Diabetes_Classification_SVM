# Diabetes_Classification_SVM
* Built a SVM to predict a diabetes patient status with ```train_accuracy``` ~ 0.780 and ```test_accuracy ~ 0.779```
* EDA for the dataset in jupyter notebook with some notes about the data (uploaded above)
* Pre_prosseced (Standarization, splitting) the dataset 
* Built SVM and uploaded it on a web server using Flask API

## Resources
**Data Retrieved from:** https://www.kaggle.com/uciml/pima-indians-diabetes-database

**Model Build Info:** https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html?highlight=svc#sklearn.svm.SVC

**What is BMI:** https://en.wikipedia.org/wiki/Body_mass_index

# Code and Packages
**Python Version:** 3.9.6

**Packages:** Python, Flask, Scikit-learn, Numpy, Pandas, Matplotlib, HTML, CSS 

**To run the server:** Write ```python app.py``` in your terminal in the same directory as the files and open the server url on your browser.


## Dataset
The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

* The dataset has 768 samples, each with 8 features ```Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age```
* The dataset has more negative (*non-diabetic*) than positive samples (*diabetic*)

*Note: THE DATA ONLY HAVE ```FEMALE SAMPLES```*

## EDA 
### You can find a full explaination of the data in the notebook above (*data_eda.ipynb*)

Here are some of the highlights about the data:

![alt text](https://github.com/ahmedheakl/Diabetes_Classification_SVM/blob/main/BMI_boxplot.png "BoxPlot for BMI Values")
![alt text](https://github.com/ahmedheakl/Diabetes_Classification_SVM/blob/main/data_means_groupedby_target_vals.PNG "Mean of the dataset")

## Data Preprossing and Model Build
* Applied a ```StandardScaler``` model to normalize the data, and unit its range for better performance
* Split the data into train and test with ```test_size=0.2```
* Fit the data to sklearn *Support Vector Machine Classifier* model. 
* Tested the train and test accuracies to be 0.780 and 0.779
* Saved the model to be used later by the web server

## Flask Web Server
* Built an ```index``` route with multiple text input to enter the data
* Built a ```predict``` route. You can only access this route with a ```POST``` method

Here is how the page looks:

<p>
<img width="250" height="400" src="https://github.com/ahmedheakl/Diabetes_Classification_SVM/blob/main/website_data.PNG">
<img width="250" height="400" src="https://github.com/ahmedheakl/Diabetes_Classification_SVM/blob/main/yes_diabetes.PNG">
</p>


