import sys
import urllib.request		

my_request = urllib.request.urlopen(sys.argv[1])

my_HTML = my_request.read().decode("utf8")

print(my_HTML)