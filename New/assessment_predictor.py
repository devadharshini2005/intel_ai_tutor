import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Generate synthetic student data
np.random.seed(42)
num_samples = 1000

data = {
    "Age": np.random.randint(10, 18, num_samples),
    "Student_Level": np.random.choice([0, 1, 2], num_samples),
    "Course_Level": np.random.choice([0, 1, 2], num_samples),
    "Study_Hours": np.random.uniform(0.5, 6, num_samples),
    "IQ_Score": np.random.randint(80, 140, num_samples),
    "Assessment_Score": np.random.randint(40, 100, num_samples)
}

df = pd.DataFrame(data)

# Features & target variable
X = df.drop(columns=["Assessment_Score"])
y = df["Assessment_Score"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a new model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

def predict_assessment(student_data):
    """
    Predicts the assessment score given student data.

    :param student_data: dict with keys ["Age", "Student_Level", "Course_Level", "Study_Hours", "IQ_Score"]
    :return: Predicted assessment score
    """
    df = pd.DataFrame([student_data])  # Convert dictionary to DataFrame
    prediction = model.predict(df)
    return prediction[0]


# Save the model
joblib.dump(model, "pretrained_assessment_model.pkl")
print("✅ Model trained & saved successfully!")

