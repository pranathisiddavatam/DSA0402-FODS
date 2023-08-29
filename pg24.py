import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
data = np.genfromtxt('C:/Users/DELL/OneDrive/Documents/medical.csv', delimiter=',', skip_header=True)
features = data[:, :-1] 
labels = data[:, -1]    
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
k = int(input("Enter the number of neighbors (k): "))
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train, y_train)
new_patient_features = []
for i in range(features.shape[1]):
    feature_value = float(input(f"Enter the value for symptom {i + 1}: "))
    new_patient_features.append(feature_value)
prediction = knn_classifier.predict([new_patient_features])
if prediction[0] == 0:
    print("The new patient is predicted to NOT have the medical condition.")
else:
    print("The new patient is predicted to have the medical condition.")
