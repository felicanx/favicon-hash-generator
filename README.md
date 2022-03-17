# favicon-hash-generator
This tools takes favicon url as input and convert its hash value which can be further used in shodan to find IP addresses

# TO use this tool Follow the steps
-->just copy the code and run through python editor(like pycharm or sublime ) directly

                            OR
                            
{ step 1. git clone https://github.com/felicanx/favicon-hash-generator.git } 
{ step 2. chmod +x fav.py }
{ step 3. pip install " the libraies " }
{ step 4. change the domain whenever you need in the code } 

you can change the code to just add list of domains from a file in that way you don't need to enter domains everytime you need

## WHAT TO DO AFTER GETTING HASH 
you can search that hash like this  [http.favicon.hash:"hash-value"] in shodan to get IP addresses
