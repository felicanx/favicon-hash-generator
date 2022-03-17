#install thse libraries using pip command to successfully run this tool and have fun
##felican AKA Rajnish kumar

import mmh3
import requests
import codecs

response = requests.get('enter-domain-here')
favicon = codecs.encode(response.content, "base64")
hash = mmh3.hash(favicon)
print(hash)
