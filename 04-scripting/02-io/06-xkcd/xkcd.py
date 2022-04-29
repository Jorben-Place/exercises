from urllib.parse import urljoin
import urllib.request
import sys
import json
url = f"https://xkcd.com/{sys.argv[1]}/info.0.json"
# print(url)
with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['comic'])