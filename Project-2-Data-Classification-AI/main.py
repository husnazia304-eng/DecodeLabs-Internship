# ==========================================
# DATA CLASSIFICATION USING AI
# Iris Dataset + KNN Algorithm
# ==========================================

# Import libraries
import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATASET
# ==========================================

print("\nLoading Iris Dataset...\n")

iris = load_iris()

X = iris.data
y = iris.target

print("Features:")
print(iris.feature_names)

print("\nTarget Classes:")
print(iris.target_names)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nDataset Split Complete.")
print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))

# ==========================================
# FEATURE SCALING
# ==========================================

print("\nApplying Feature Scaling...\n")

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==========================================
# KNN MODEL
# ==========================================

print("Training KNN Model...\n")

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

# ==========================================
# PREDICTION
# ==========================================

y_pred = model.predict(X_test)

# ==========================================
# EVALUATION
# ==========================================

print("Predictions:\n")
print(y_pred)

print("\nActual Values:\n")
print(y_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score:")
print(accuracy)

# F1 Score
f1 = f1_score(y_test, y_pred, average='weighted')

print("\nF1 Score:")
print(f1)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n")
print(cm)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ==========================================
# VISUALIZATION
# ==========================================

plt.figure(figsize=(8,6))

sns.heatmap(
    cm,
    annot=True,
    cmap="Blues",
    fmt='d',
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()

print("\nProject Completed Successfully!")
