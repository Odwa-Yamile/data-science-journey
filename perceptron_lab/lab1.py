import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Load the dataset from the CSV file
# The separator is ";" because the dataset values are separated by semicolons
data = pd.read_csv("Percept1.csv", sep=";")

# Separate the input features and target labels
# X contains the feature columns
# y contains the output/class column
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# ---------------------------------------------------
# STEP 1: Split the dataset into training and temp data
# 50% training
# 50% temporary data (will later become validation + testing)
# ---------------------------------------------------
X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.5,
    random_state=42
)

# ---------------------------------------------------
# STEP 2: Split the temporary data into:
# 25% validation
# 25% testing
# Since X_temp already contains 50% of the data,
# splitting it equally gives 25% validation and 25% testing
# ---------------------------------------------------
X_validation, X_test, y_validation, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.5,
    random_state=42
)

# Create the Perceptron model
model = Perceptron()

# Train the model using the training dataset
model.fit(X_train, y_train)

# --------------------------------------------
# VALIDATION PHASE
# Use validation data to evaluate the model
# during development before final testing
# --------------------------------------------
validation_predictions = model.predict(X_validation)

validation_accuracy = accuracy_score(
    y_validation,
    validation_predictions
)

print("Validation Accuracy:", validation_accuracy)

# --------------------------------------------
# TESTING PHASE
# Use the final test dataset to measure the model's final performance
# --------------------------------------------
test_predictions = model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, test_predictions)

# Precision measures how many predicted positives were correct
precision = precision_score(y_test, test_predictions)

# Recall measures how many actual positives were correctly identified
recall = recall_score(y_test, test_predictions)

# F1 Score balances precision and recall
f1 = f1_score(y_test, test_predictions)

# Display evaluation results
 
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Generate a confusion matrix to see
# how many predictions were correct or incorrect
cm = confusion_matrix(y_test, test_predictions)

# Display the confusion matrix

print(cm)



