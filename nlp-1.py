import urllib.request

response = urllib.request.urlopen('http://somiljain.me/')

html = response.read()

print (html)
