#EXP3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Read the dataset
# Assuming the dataset is available as 'bank_data.csv'
data = pd.read_csv('bank_data.csv')

# Step 2: Distinguish feature and target sets and divide data into training and test sets
# Drop unnecessary columns like 'CustomerId' and 'Surname'
X = data.drop(columns=['Exited', 'CustomerId', 'Surname'])
y = data['Exited']  # Target column ('Exited' indicates whether the customer left or not)

# One-hot encoding for categorical variables (e.g., 'Geography', 'Gender')
X = pd.get_dummies(X, drop_first=True)

# Split data into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Normalize the train and test data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Initialize and build the model
# Build a neural network model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))  # Input layer + hidden layer
model.add(Dense(units=32, activation='relu'))  # Another hidden layer
model.add(Dense(units=1, activation='sigmoid'))  # Output layer (sigmoid for binary classification)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Step 5: Evaluate the model
# Predict on the test data
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)  # Convert probabilities to binary outcome (0 or 1)

# Calculate the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)
