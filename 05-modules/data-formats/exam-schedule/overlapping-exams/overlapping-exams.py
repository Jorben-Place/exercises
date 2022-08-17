import csv


table = {}
students_with_overlaps = set()
with open('../exam-schedule.csv', 'r') as csvFile:
    data = csv.DictReader(csvFile)
    for row in data:
        student=row['Student ID']
        date = row['Datum']
        partOfDay = row['Dagdeel']

        d = table.setdefault(student, {})

        key = (date, partOfDay)
        oldCount = d.get(key, 0)
        newCount = oldCount + 1
        d[key] = newCount

        if newCount == 2:
            students_with_overlaps.add(student)

for student in sorted(list(students_with_overlaps)):
    overlap_moments = sorted(when for when, count in table[student].items() if count > 1)

    for when in overlap_moments:
        date, partOfDay = when
        count = table[student][when]
        print(f"{student} has {count} exams on {date} ({partOfDay})")