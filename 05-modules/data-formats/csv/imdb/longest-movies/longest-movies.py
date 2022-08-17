
import csv


def second(xs):
    return xs[1]

def runtime(row):
    result = row['runtimeMinutes']
    if result == r"\N":
        return 0
    else:
        try:
            return int(result)
        except:
            print(row)
            raise

csvFilePath = '../title-basics.tsv'


with open(csvFilePath, encoding='utf_8') as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter='\t', quoting=csv.QUOTE_NONE)
    results = [ (row['originalTitle'], row['runtimeMinutes']) for row in csvReader if row['runtimeMinutes'] != r'\N' ]

results.sort (key=second, reverse=True)
top_100 = results[:100]

for title, runtime in top_100:
    print(f"{str(runtime).rjust(5)} {title}")