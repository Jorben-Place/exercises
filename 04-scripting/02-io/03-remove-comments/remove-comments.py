import sys
import fileinput
 
x = input("***")
y = input("")
 
for l in fileinput.input(files = sys.argv[1]):
    l = l.replace(x, y)
    sys.stdout.write(l)
