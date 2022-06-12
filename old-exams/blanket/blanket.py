import datetime
import json
with open('output.txt', 'w') as out:
    with open('input.txt') as inp:
        datums = json.loads(inp.read()).items()
        for key, value in sorted(datums, key=lambda x: datetime.datetime.strptime(x[0], '%d/%m/%Y')):
            out.write(str(round(sum(value)/len(value)))+'\n')