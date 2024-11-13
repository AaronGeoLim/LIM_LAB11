passing_grade = 75
min_grade = 40
max_grade = 100
total_students = 5

grades = []
passing_count = 0

for i in range(total_students): 
    grade = float(input(f"Enter a grade for student {i+1} (between {min_grade} and {max_grade}):"))
    while grade < min_grade or grade > max_grade:
        print(f"Grade must be between {min_grade} and {max_grade}. ")
        grade = float(input(f"Enter the grade for student {i+1} (between {min_grade} and {max_grade}): "))
        
    grades.append(grade)
    if grade >= passing_grade:
        passing_count += 1
        
average_grade = sum(grades) / total_students
passing_percentage = (passing_count / total_students) * 100

print("\nGrades entered:", grades)
print("Average grade:", average_grade)
print("Number of students with passing grade:, passing_count")
print("Passing percentage:", passing_percentage, "%")

