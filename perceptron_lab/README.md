# Perceptron Classification using Scikit-Learn

## Overview

This project applies the **Perceptron Learning Algorithm** using **scikit-learn** to classify data from the **Percept1 dataset**. The objective is to demonstrate the implementation of a basic linear classifier and evaluate its performance on a given dataset.

The project follows the requirements of the first lab assignment for **COMS5026A – Applied Machine Learning**, focusing on using Python and the scikit-learn library to train and test a perceptron model.

---

## Objectives

* Load and explore the Percept1 dataset.
* Prepare the dataset for machine learning.
* Implement the Perceptron Learning Algorithm using scikit-learn.
* Train the perceptron model on the dataset.
* Evaluate the model's performance using classification metrics.
* Demonstrate the successful use of scikit-learn for machine learning classification.

---

## Technologies Used

* Python 3
* scikit-learn
* NumPy
* Pandas
* Matplotlib
* Jupyter Notebook

---

## Dataset

**File:** `Percept1.csv`

The Percept1 dataset is provided in both spreadsheet and CSV formats and contains features and corresponding target labels used for binary classification.

---

## Project Workflow

### 1. Load the Dataset

The dataset is loaded into a Pandas DataFrame and explored to understand its structure and contents.

### 2. Data Preparation

The dataset is prepared by:

* Separating input features and target labels
* Handling any missing or inconsistent values if necessary
* Converting the data into a format suitable for training the model

### 3. Train-Test Split

The dataset is divided into:

* Training Set
* Test Set

This allows the perceptron model to learn from one portion of the data and be evaluated on unseen data.

### 4. Model Training

A Perceptron classifier is implemented using scikit-learn:

```python
from sklearn.linear_model import Perceptron
```

The model is trained on the training data and learns a linear decision boundary that separates the classes.

### 5. Model Evaluation

The trained model is evaluated on the test set using classification metrics such as:

* Accuracy
* Predictions on unseen samples

The evaluation measures how well the perceptron generalises to new data.

---

## Machine Learning Model

### Perceptron Classifier

The Perceptron is a supervised learning algorithm that performs binary classification by learning a set of weights and a bias term. During training, these parameters are iteratively adjusted to minimise classification errors.

---

## Project Structure

```text
├── Percept1.csv
├── Perceptron_Classification.ipynb
└── README.md
```

---

## Installation

Install the required libraries:

```bash
pip install scikit-learn numpy pandas matplotlib jupyter
```

---

## Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Perceptron_Classification.ipynb
```

Run all notebook cells to:

1. Load the dataset
2. Prepare the data
3. Train the perceptron classifier
4. Evaluate the model's performance

---

## Conclusion

This project demonstrates the application of the Perceptron Learning Algorithm using scikit-learn for binary classification. By training and evaluating a perceptron model on the Percept1 dataset, the assignment provides practical experience in implementing a fundamental machine learning algorithm and using the scikit-learn library for supervised learning tasks.

