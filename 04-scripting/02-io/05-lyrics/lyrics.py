import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
import sys
import re
import json

def to_url(string):
    '''
    URLs cannot contain spaces. Replaces each space by %20.
    '''
    return re.sub(' ', '%20', string)

artist, title = sys.argv[1:]
title = to_url(title)
artist = to_url(artist)

url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['lyrics'])
