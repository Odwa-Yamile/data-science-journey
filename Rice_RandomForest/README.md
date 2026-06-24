# Rice Classification using Random Forest

## Overview

This project implements a **Random Forest Classifier** using **scikit-learn** to classify rice grains from the **Rice (Cammeo and Osmancik) dataset**. The objective is to build a machine learning model that can accurately distinguish between the two rice varieties based on their physical measurements.

The project follows the requirements of **COMS5026A – Applied Machine Learning Lab Exercise 3**, focusing on training a Random Forest classifier and evaluating its performance using standard classification metrics.

---

## Objectives

* Load and explore the Rice dataset.
* Prepare the dataset for machine learning.
* Implement a Random Forest classifier using scikit-learn.
* Train and test the classifier on the dataset.
* Evaluate the model by printing:

  * Confusion Matrix
  * Accuracy
  * Precision
  * Sensitivity (Recall)
  * F1 Score
* Demonstrate the implementation to a tutor as required by the assignment.

---

## Technologies Used

* Python 3
* scikit-learn
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Dataset

**Dataset:** Rice (Cammeo and Osmancik)

The dataset contains measurements of rice grains belonging to two varieties:

* Cammeo
* Osmancik

Each sample contains numerical features describing the shape and size of a rice grain, including attributes such as:

* Area
* Perimeter
* Major Axis Length
* Minor Axis Length
* Eccentricity
* Convex Area
* Extent
* And other geometric measurements

The target variable represents the rice variety classification.

---

## Project Workflow

### 1. Load the Dataset

The Rice dataset is loaded into a Pandas DataFrame and explored to understand its structure and features.

### 2. Data Preparation

The dataset is prepared by:

* Separating input features and target labels
* Handling missing values if necessary
* Encoding the target labels
* Preparing the data for machine learning

### 3. Train-Test Split

The dataset is divided into:

* Training Set
* Test Set

This allows the model to learn from one portion of the data and evaluate its performance on unseen samples.

### 4. Model Training

A Random Forest classifier is implemented using scikit-learn:

```python
from sklearn.ensemble import RandomForestClassifier
```

The classifier is trained on the training data using multiple decision trees to improve prediction performance and reduce overfitting.

### 5. Model Evaluation

After training, the model is evaluated on the test set and prints the following metrics:

* Confusion Matrix
* Accuracy
* Precision
* Sensitivity (Recall)
* F1 Score

These metrics provide a comprehensive evaluation of the classifier's performance.

---

## Machine Learning Model

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that constructs multiple decision trees and combines their predictions to produce a more accurate and robust classification model.

Advantages of Random Forest include:

* High classification accuracy
* Reduced overfitting
* Ability to handle large datasets and multiple features
* Robust performance on classification tasks

---

## Evaluation Metrics

### Confusion Matrix

Displays the number of correct and incorrect predictions for each rice variety.

### Accuracy

Measures the percentage of correctly classified samples.

### Precision

Measures the proportion of positive predictions that are correct.

### Sensitivity (Recall)

Measures the ability of the model to correctly identify positive samples.

### F1 Score

Provides a balance between Precision and Recall.

---

## Project Structure

```text
├── Rice_Cammeo_Osmancik.csv
├── Rice_Random_Forest.ipynb
└── README.md
```

---

## Installation

Install the required libraries:

```bash
pip install scikit-learn numpy pandas matplotlib seaborn jupyter
```

---

## Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Rice_Random_Forest.ipynb
```

Run all notebook cells to:

1. Load and explore the dataset
2. Prepare the data
3. Train the Random Forest classifier
4. Generate predictions
5. Print the evaluation metrics

---

## Expected Output

The program should display:

* Confusion Matrix
* Accuracy
* Precision
* Sensitivity (Recall)
* F1 Score

These metrics demonstrate the effectiveness of the Random Forest classifier on the Rice dataset.

---

## Conclusion

This project demonstrates the application of a Random Forest classifier using scikit-learn for binary classification of rice grain varieties. By training and evaluating the model using multiple performance metrics, the assignment provides practical experience in implementing ensemble learning methods and assessing classification performance in machine learning.
