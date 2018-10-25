# -*- coding: utf-8 -*-

import json
import ssl
import urllib
if __name__ == "__main__":
    context = ssl._create_unverified_context()
    url = "https://raw.githubusercontent.com/AstinChoi/introducing-python/master/intro/top_rated.json"
    response = urllib.urlopen(url, context=context)
    contents = response.read()
    text = contents.decode('utf-8')
    data = json.load(text)
    for video in data['feed']['entry'][0:6]:
        print(video['title']['\t'])
