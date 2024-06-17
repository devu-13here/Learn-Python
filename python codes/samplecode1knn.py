import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

# Creating the dataset
data = {
    'Experience': [2, 3, 5, 7, 10, 12, 15, 6, 8, 13],
    'Written_Test_Score': [5, 7, 8, 7, 8, 9, 9, 6, 7, 8],
    'Interview_Score': [7, 8, 10, 9, 8, 9, 9, 7, 6, 8],
    'Salary': [50000, 60000, 75000, 80000, 110000, 120000, 140000, 72000, 95000, 130000]
}

df = pd.DataFrame(data)

# Save the dataset to a .csv file
df.to_csv('candidate_salary_dataset.csv', index=False)

# Reading the dataset
df = pd.read_csv('candidate_salary_dataset.csv')

# Splitting the dataset into features and target variable
X = df[['Experience', 'Written_Test_Score', 'Interview_Score']]
y = df['Salary']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Building the KNN model
k_values = [3, 5, 7]  # Try different values of k
for k in k_values:
    knn_model = KNeighborsRegressor(n_neighbors=k)
    knn_model.fit(X_train, y_train)

    # Predicting salaries for the given candidates
    candidate_data = np.array([[5, 8, 10], [8, 7, 6]])  # Candidate data for prediction
    candidate_data_scaled = scaler.transform(candidate_data)  # Scale the input data
    predicted_salaries = knn_model.predict(candidate_data_scaled)  # Predict salaries
    print(f"Predicted salaries using KNN with k={k}: {predicted_salaries}")
