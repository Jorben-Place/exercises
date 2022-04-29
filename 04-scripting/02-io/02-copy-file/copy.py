import sys
with open(sys.argv[1],'r') as firstfile, open(sys.argv[2],'a') as secondfile:
    for line in firstfile:
             secondfile.write(line)