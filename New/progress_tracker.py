import joblib
import pandas as pd

# Load the trained model
model = joblib.load("pretrained_assessment_model.pkl")

# Mapping for categorical values
level_mapping = {"Beginner": 0, "Intermediate": 1, "Advanced": 2}

def predict_assessment(student_data):
    """
    Predicts the assessment score given student data.

    :param student_data: dict with keys ["Age", "Student_Level", "Course_Level", "Study_Hours", "IQ_Score"]
    :return: Predicted assessment score
    """
    # Convert categorical values to numerical
    student_data["Student_Level"] = level_mapping.get(student_data["Student_Level"], 0)
    student_data["Course_Level"] = level_mapping.get(student_data["Course_Level"], 0)

    # Convert to DataFrame
    df = pd.DataFrame([student_data])

    # Ensure feature names match model training
    df = df[["Age", "Student_Level", "Course_Level", "Study_Hours", "IQ_Score"]]

    # Predict score
    prediction = model.predict(df)
    return prediction[0]
