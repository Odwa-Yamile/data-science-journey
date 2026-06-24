# Iris Classification using a Neural Network

## Overview

This project implements a **feedforward neural network** using **scikit-learn** to classify flower species in the **Iris dataset**. The objective is to build, train, and evaluate a neural network that predicts the correct Iris species based on four flower measurements.

The project follows the requirements of the **COMS5026A – Applied Machine Learning Lab Exercise 2** assignment, including data preprocessing, dataset splitting, neural network training, and performance evaluation.

---

## Objectives

* Construct a neural network with:

  * An input layer containing **4 nodes**
  * At least **one hidden layer** containing **20 nodes**
  * An output layer containing **3 nodes**
* Apply **max-min normalisation** to the input features.
* Create a **one-hot encoding** of the target classes.
* Split the dataset into **training**, **validation**, and **test** sets.
* Train the neural network using the **sum-of-squares loss function**.
* Monitor training by printing:

  * Training loss after every epoch
  * Validation loss after every epoch
* Evaluate the model by reporting the **test accuracy**.

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

The project uses the **Iris dataset**, which contains **150 samples** of iris flowers belonging to three species:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

Each sample contains four input features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The target variable consists of three flower species classes.

---

## Project Workflow

### 1. Load the Dataset

The Iris dataset is loaded and explored to understand its structure and class distribution.

### 2. Data Preprocessing

#### Input Normalisation

All input features are normalised using **max-min normalisation**:

```text
x' = (x - min(x)) / (max(x) - min(x))
```

#### One-Hot Encoding

The target labels are converted into one-hot encoded vectors:

```text
Setosa      -> [1, 0, 0]
Versicolor  -> [0, 1, 0]
Virginica   -> [0, 0, 1]
```

### 3. Dataset Splitting

The dataset is divided into:

* Training Set
* Validation Set
* Test Set

This allows the model to learn from the training data, monitor performance during training using validation data, and evaluate final performance on unseen test data.

---

## Neural Network Architecture

The neural network consists of:

| Layer        | Number of Nodes |
| ------------ | --------------- |
| Input Layer  | 4               |
| Hidden Layer | 20              |
| Output Layer | 3               |

Additional hidden layers may be added to improve performance.

---

## Training

The neural network is trained using the **sum-of-squares loss function**.

After every training epoch, the following metrics are displayed:

* Training Loss
* Validation Loss

Monitoring both losses helps determine whether the model is learning effectively and whether overfitting occurs.

---

## Evaluation

After training is complete, the model is evaluated on the test set.

### Evaluation Metric

* Classification Accuracy

The final accuracy indicates how well the neural network generalises to unseen Iris samples.

---

## Project Structure

```text
├── iris.csv
├── Iris_Neural_Network.ipynb
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
Iris_Neural_Network.ipynb
```

Run all notebook cells to:

1. Load and preprocess the data
2. Train the neural network
3. Display training and validation losses
4. Evaluate and print the test accuracy

---

## Conclusion

This project demonstrates the implementation of a feedforward neural network for multiclass classification using the Iris dataset. By applying data normalisation, one-hot encoding, and proper dataset splitting, the neural network is able to learn the underlying patterns in the data and accurately classify Iris flower species.

