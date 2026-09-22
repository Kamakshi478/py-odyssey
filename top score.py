students = [{"name": "Jacob", "score": 85}, {"name": "Mia", "score": 58}, {"name": "Sophia", "score": 92}, {"name": "Liam", "score": 70}]
top_students = [student for student in students if student["score"] > 70]
print(top_students)