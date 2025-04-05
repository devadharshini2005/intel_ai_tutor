import pandas as pd
import os

STUDENT_FILE = "students.csv"

def initialize_student_file():
    if not os.path.exists(STUDENT_FILE):
        columns = ["Name", "Age", "Gender", "Country", "State", "City", "Parent_Occupation",
                   "Earning_Class", "Student_Level", "Course_Level", "Course_Name",
                   "Assessment_Score", "Study_Hours", "Material_Name", "Material_Level", "IQ_Score"]
        df = pd.DataFrame(columns=columns)
        df.to_csv(STUDENT_FILE, index=False)

def add_student():
    print("\n📌 Enter Student Details:")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender (Male/Female/Other): ")
    country = input("Country: ")
    state = input("State: ")
    city = input("City: ")
    parent_occupation = input("Parent Occupation: ")
    earning_class = input("Earning Class (Low/Middle/High): ")
    student_level = input("Student Level (Beginner/Intermediate/Advanced): ")
    course_level = input("Course Level (Beginner/Intermediate/Advanced): ")
    course_name = input("Course Name: ")
    assessment_score = 0  # Initially 0, predicted later
    study_hours = float(input("Study Hours Per Day: "))
    material_name = input("Default Material Name: ")
    material_level = input("Material Level (Beginner/Intermediate/Advanced): ")
    iq_score = int(input("IQ Score: "))

    student_data = {
        "Name": name, "Age": age, "Gender": gender, "Country": country, "State": state, "City": city,
        "Parent_Occupation": parent_occupation, "Earning_Class": earning_class,
        "Student_Level": student_level, "Course_Level": course_level, "Course_Name": course_name,
        "Assessment_Score": assessment_score, "Study_Hours": study_hours, "Material_Name": material_name,
        "Material_Level": material_level, "IQ_Score": iq_score
    }

    df = pd.read_csv(STUDENT_FILE)

    # ✅ Fix: Use `pd.concat()` instead of `.append()`
    df = pd.concat([df, pd.DataFrame([student_data])], ignore_index=True)

    df.to_csv(STUDENT_FILE, index=False)

    print("\n✅ Student data saved successfully!")

initialize_student_file()
add_student()
