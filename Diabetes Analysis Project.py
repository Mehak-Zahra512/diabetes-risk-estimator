import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -------------------------
# Sample Dataset (simplified version)
# -------------------------

data = {
    "glucose": [80, 120, 90, 150, 85, 160, 95, 130, 100, 170, 88, 140],
    "bmi": [22, 30, 25, 35, 24, 38, 26, 32, 27, 40, 23, 34],
    "age": [22, 45, 30, 50, 28, 55, 33, 48, 29, 60, 26, 52],
    "diabetes": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print(df.head())


# Visualization


df["diabetes"].value_counts().plot(kind="bar")
plt.title("Diabetes Cases Distribution")
plt.xlabel("0 = No Diabetes, 1 = Diabetes")
plt.ylabel("Count")
plt.savefig("diabetes_distribution.png")
plt.show()


# Model
X = df.drop("diabetes", axis=1)
y = df["diabetes"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# Evaluation


print("\nAccuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Prediction Example


new_patient = [[110, 28, 40]]
prediction = model.predict(new_patient)

if prediction[0] == 1:
    print("Patient is at risk of diabetes")
else:
    print("Patient is not at risk")