students= {"A":[85,90,78], "B": [60,72,68], "C": [35,42,38],"D": [95,91,94] }

for student, marks in students.items():
    average= sum(marks)/len(marks)
    if average >= 90:
        grade="A"
    elif average >=75:
        grade="B"
    elif average >= 50:
        grade="C"
    else: 
        grade="Fail"

    print(f"Student: {student}, Average Marks:{average}, Grade: {grade}")