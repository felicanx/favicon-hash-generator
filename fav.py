#install thse libraries using pip command to successfully run this tool and have fun
##felican AKA Rajnish kumar

import mmh3
import requests
import codecs

file0=open('filename.txt','r')
data=file0.read()
urls=data.splitlines()
file1=open('favicon_hash.txt','a')

for url in urls:
    response=requests.get(url)
    favicon=codecs.encode(response.content,"base64")
    hash=mmh3.hash(favicon)
    hash=str(hash)
    file1.writelines(hash+"\n")

file0.close()
file1.close()
