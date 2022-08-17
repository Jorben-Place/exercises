import csv


table = {}
with open('../exam-schedule.csv', 'r') as csvFile:
    data = csv.DictReader(csvFile)
    for row in data:
        student=row['Student ID']
        table[student] = table.get(student, 0) + 1

max_exam_count = max(table.values())

for student in ( student for student, exam_count in table.items() if exam_count == max_exam_count ):
    print(f"{student} has {max_exam_count} exams")