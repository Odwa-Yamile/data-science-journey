# Income Classification using Spark MLlib

## Overview

This project uses **Apache Spark (PySpark) and MLlib** to build machine learning models that predict whether an individual earns **more than $50,000 per year** based on demographic and census information from the **US Census Income dataset**.

The dataset contains approximately **32,000 records** and includes both numerical and categorical features. Since Spark MLlib requires numerical input, categorical variables are converted into indexed numerical representations before training the models.

## Objectives

- Load and explore the Income dataset using PySpark.
- Preprocess and transform categorical variables into numerical indexes.
- Assemble features into a single feature vector.
- Train and evaluate:
  - Decision Tree Classifier
  - Random Forest Classifier
- Achieve a classification accuracy greater than **75%**.

---

## Technologies Used

- Python 3
- Apache Spark (PySpark)
- Spark MLlib
- Jupyter Notebook

---

## Dataset

**File:** `income.csv`

The dataset contains census attributes such as:

- Age
- Work Class
- Education
- Marital Status
- Occupation
- Relationship
- Race
- Sex
- Citizenship
- Hours Worked per Week
- Capital Gain
- Capital Loss
- Income Category (Target Variable)

The target variable indicates whether an individual's annual income is:

- `<=50K`
- `>50K`

---

## Project Workflow

### 1. Create Spark Session

A Spark session is initialized and log messages are reduced for cleaner output.

### 2. Load the Dataset

The CSV file is loaded into a Spark DataFrame using:

- Header detection
- Automatic schema inference

The schema and sample records are displayed to understand the structure of the data.

### 3. Data Preprocessing

Categorical features are converted into numerical indexes using `StringIndexer`.

Indexed columns include:

- `workclass`
- `education`
- `marital_status`
- `occupation`
- `relationship`
- `race`
- `sex`
- `citizenship`

The income target variable is also indexed to create the `label` column.

### 4. Feature Engineering

All predictor variables are combined into a single `features` vector using `VectorAssembler`.

Features used:

- age
- weight
- education_years
- capital_gain
- capital_loss
- hours_per_week
- Indexed categorical variables

### 5. Train-Test Split

The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

A fixed random seed (`42`) is used to ensure reproducibility.

---

## Machine Learning Models

### Decision Tree Classifier

A Decision Tree model is trained using:

- `featuresCol = "features"`
- `labelCol = "label"`
- `maxBins = 64`

The model learns decision rules that classify individuals into income categories.

### Random Forest Classifier

A Random Forest model is trained using:

- `featuresCol = "features"`
- `labelCol = "label"`
- `numTrees = 100`
- `maxBins = 64`

Random Forest combines multiple decision trees to improve prediction performance and reduce overfitting.

---

## Evaluation Metrics

Both models are evaluated using:

- Accuracy
- Precision
- Recall
- Area Under the ROC Curve (AUC)

These metrics are calculated using Spark MLlib evaluators:

- `MulticlassClassificationEvaluator`
- `BinaryClassificationEvaluator`

---

## Expected Results

The models are designed to achieve:

- Classification accuracy greater than **75%**
- Good precision and recall
- Strong AUC performance

Typically, the **Random Forest classifier** performs better than the Decision Tree classifier due to its ensemble learning approach.

---

## Project Structure

```text
├── income.csv
├── Income_Classification.ipynb
└── README.md
```

---

## How to Run

### Start Spark

```bash
pip install pyspark
```

### Run the Notebook

```bash
jupyter notebook
```

Open:

```text
Income_Classification.ipynb
```

Ensure that `income.csv` is in the same directory as the notebook before running all cells.

---

## Conclusion

This project demonstrates how Apache Spark MLlib can be used to perform large-scale machine learning tasks. By preprocessing categorical census data and applying Decision Tree and Random Forest classifiers, the system can effectively predict whether an individual's annual income exceeds **$50,000** with high accuracy.
