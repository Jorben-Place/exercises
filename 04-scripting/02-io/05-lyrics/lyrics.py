import sys
import urllib.request		

my_request = urllib.request.urlopen("https://api.lyrics.ovh/v1/"sys.argv[1]"/"sys.argv[2])

my_HTML = my_request.read().decode("utf8")

print(my_HTML)