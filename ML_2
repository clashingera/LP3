#EXP2
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Step 1: Load and Preprocess the Dataset
# Example dataset with 'text' (email content) and 'label' (spam or not spam)
# Replace with your actual dataset
data = pd.read_csv('spam_email_data.csv')  # Your dataset
data['label'] = LabelEncoder().fit_transform(data['label'])  # Encoding 'spam' as 1 and 'not spam' as 0

# Step 2: Convert Text Data into Numerical Features
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(data['text']).toarray()  # Convert email text to numerical features
y = data['label']  # Labels for classification (0 = Not Spam, 1 = Spam)

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train K-Nearest Neighbors Classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Step 5: Train Support Vector Machine Classifier
svm = SVC(kernel='linear')  # You can try 'rbf' kernel as well
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

# Step 6: Evaluate the Models
# KNN Evaluation
knn_accuracy = accuracy_score(y_test, y_pred_knn)
knn_report = classification_report(y_test, y_pred_knn)

# SVM Evaluation
svm_accuracy = accuracy_score(y_test, y_pred_svm)
svm_report = classification_report(y_test, y_pred_svm)

# Output the results
print(f"KNN Accuracy: {knn_accuracy:.3f}")
print(f"KNN Classification Report:\n{knn_report}")

print(f"SVM Accuracy: {svm_accuracy:.3f}")
print(f"SVM Classification Report:\n{svm_report}")

# Step 7: Compare the Performance
if knn_accuracy > svm_accuracy:
    print("K-Nearest Neighbors performs better.")
else:
    print("Support Vector Machine performs better.")
