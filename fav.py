import mmh3
import requests
import codecs
import argparse

parser = argparse.ArgumentParser(description="favicon-hash-generator is a automation tool for hash generation of favicons you can use this as TYPE as  [ python3 fav.py filename.txt ]")
parser.add_argument('filename', type=argparse.FileType('r'))
args = parser.parse_args()


data=args.filename.read()
urls=data.splitlines()
file1=open('favicon_hash.txt','a')

for url in urls:
    response=requests.get(url)
    favicon=codecs.encode(response.content,"base64")
    hash=mmh3.hash(favicon)
    hash=str(hash)
    file1.writelines(hash+"\n")




