import urllib
import re
import requests
urls = ["http://google.com", "http://gmail.com", "http://iitb.ac.in", "http://twitter.com"]
i=0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i < len(urls):
    htmlfile = requests.get(urls[i])
    htmltext = htmlfile.text
    title = re.findall(pattern, htmltext)
    print(title)
    i+=1
