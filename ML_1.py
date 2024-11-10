#EXP1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Step 1: Load and Pre-process the Dataset
data = pd.read_csv('uber_data.csv')  # Replace with actual file path
data = data.dropna()  # Drop missing values

# Step 2: Detect and Handle Outliers
sns.boxplot(data['price'])  # Visualize outliers
Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3 - Q1
data = data[(data['price'] >= Q1 - 1.5 * IQR) & (data['price'] <= Q3 + 1.5 * IQR)]  # Remove outliers

# Step 3: Check Correlation
sns.heatmap(data.corr(), annot=True)  # Correlation matrix

# Step 4: Feature Selection and Data Splitting
X = data.drop(columns=['price'])
y = data['price']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

# Step 6: Random Forest Regression Model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Step 7: Evaluate the Models
# Linear Regression Evaluation
lr_r2 = r2_score(y_test, y_pred_lr)
lr_rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr))

# Random Forest Evaluation
rf_r2 = r2_score(y_test, y_pred_rf)
rf_rmse = np.sqrt(mean_squared_error(y_test, y_pred_rf))

# Output the results
print(f"Linear Regression R2: {lr_r2:.3f}, RMSE: {lr_rmse:.3f}")
print(f"Random Forest R2: {rf_r2:.3f}, RMSE: {rf_rmse:.3f}")

# Step 8: Compare Models
if rf_r2 > lr_r2:
    print("Random Forest Regression performs better.")
else:
    print("Linear Regression performs better.")
