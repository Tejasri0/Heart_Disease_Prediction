# ❤️ Heart Disease Prediction using Machine Learning

## Overview

Heart Disease Prediction is a Machine Learning web application that predicts whether a patient is likely to have heart disease based on clinical parameters. The project uses multiple classification algorithms, compares their performance, applies hyperparameter tuning using GridSearchCV, and deploys the best-performing model using Flask.

---

## Features

* Data preprocessing and feature engineering
* Training multiple Machine Learning models
* Model comparison using accuracy, confusion matrix, and classification report
* Hyperparameter tuning using GridSearchCV
* ROC Curve visualization
* Best model selection
* Model serialization using Pickle
* Flask-based web application for real-time prediction
* User-friendly HTML interface

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib
* Flask
* HTML
* CSS
* Pickle

---

## Machine Learning Algorithms

The following classification algorithms were trained and evaluated:

* K-Nearest Neighbors (KNN)
* Naive Bayes
* Logistic Regression
* Decision Tree
* Random Forest
* AdaBoost
* Gradient Boosting
* XGBoost
* Support Vector Machine (SVM)

---

## Hyperparameter Tuning

GridSearchCV was used to optimize the Logistic Regression model.

### Best Parameters

* C = 1
* penalty = l1
* solver = liblinear
* max_iter = 100
* fit_intercept = True
* class_weight = None
* tol = 0.0001

---

## Dataset

The project uses the Heart Disease Prediction dataset containing patient medical information such as:

* Age
* Sex
* Chest Pain Type
* Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* ECG Results
* Maximum Heart Rate
* Exercise-Induced Angina
* ST Depression
* Slope of ST Segment
* Number of Major Vessels
* Thallium Scan Result

Target:

* Presence
* Absence

---

## Project Structure

```
HeartDiseasePrediction/
│
├── app.py
├── main.py
├── Heart_Disease_Best_Model.pkl
├── Heart_Disease_Prediction.csv
├── templates/
│   └── index.html
├── static/
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd HeartDiseasePrediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Train the Model

Run:

```bash
python main.py
```

This will:

* Load the dataset
* Train multiple models
* Compare their performance
* Perform GridSearchCV
* Select the best model
* Generate `Heart_Disease_Best_Model.pkl`

---

## Run the Flask Application

Start the Flask server:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

Enter the patient's medical information and click **Predict**.

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report
* ROC Curve

---

## Sample Prediction

Input:

* Age: 70
* Sex: 1
* Chest Pain Type: 4
* Blood Pressure: 130
* Cholesterol: 322
* Fasting Blood Sugar: 0
* ECG Results: 2
* Maximum Heart Rate: 109
* Exercise Angina: 0
* ST Depression: 2.4
* Slope: 2
* Number of Vessels: 3
* Thallium: 3

Output:

```
Heart Disease: Presence
```

---

## Future Improvements

* Improve model accuracy using advanced ensemble methods
* Deploy the application on Render or Railway
* Add probability scores
* Improve UI with Bootstrap
* Add patient history management
* Integrate a database for storing predictions
