import pandas as pd

STUDENT_FILE = "students.csv"

def assign_material():
    df = pd.read_csv(STUDENT_FILE)

    for index, row in df.iterrows():
        level = row["Student_Level"]
        if level == "Beginner":
            df.at[index, "Material_Name"] = "Basic Video Lessons"
        elif level == "Intermediate":
            df.at[index, "Material_Name"] = "Advanced Books & Quizzes"
        else:
            df.at[index, "Material_Name"] = "Research Papers & Case Studies"

    df.to_csv(STUDENT_FILE, index=False)
    print("\n✅ Learning materials assigned!")

assign_material()
