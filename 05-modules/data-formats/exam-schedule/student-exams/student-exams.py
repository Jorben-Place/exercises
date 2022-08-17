import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='.csv file to consult')
parser.add_argument('id', help='student id')
parser.add_argument('--format', help='format string', default='%d %c')
args = parser.parse_args()

with open(args.filename) as file:
    data = csv.DictReader(file)

    for row in data:
        studentID = row['Student ID']

        if studentID == args.id:
            date = row['Datum']
            partOfDay = row['Dagdeel']
            course = row['OLA Naam']
            location = row['Lokaal']
            hour = row['Startuur']

            output = args.format
            output = output.replace('%d', date)
            output = output.replace('%p', partOfDay)
            output = output.replace('%c', course)
            output = output.replace('%l', location)
            output = output.replace('%t', hour)

            print(output)
