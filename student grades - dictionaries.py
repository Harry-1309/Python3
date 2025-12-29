
# Scores 91 - 100: Grade = "Outstanding" 

# Scores 81 - 90: Grade = "Exceeds Expectations" 

# Scores 71 - 80: Grade = "Acceptable" 

# Scores 70 or lower: Grade = "Fail" 

def grades(score):
    grade = ""
    if 91<=score<=100:
        grade = "Outstanding"
    elif 81<=score<=90:
        grade = "Exceeds Expectations" 
    elif 71<=score<=80:
        grade = "Acceptable"
    elif score<=70:
        grade = "Fail" 
    return grade

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
  
student_grades = {}
for key in student_scores:
    student_grades[key]  = grades(student_scores[key])
    
print(student_grades)