# favicon-hash-generator
To use this tool first make a list of favicon urls then save it in a txt file and then enter that txt file in the python code in place of [ "filename.txt" ]
and then run it it will give you list of favicon hashes which can be used in shodan

# TO use this tool Follow the steps
-->just copy the code and run through python editor(like pycharm or sublime ) directly

                            OR
                            
 1. git clone https://github.com/felicanx/favicon-hash-generator.git
 2. chmod +x fav.py 
 3. pip install " the libraies "
 4. entern the favicon urls txt file name in the positon of " filename.txt "

you can change the code to just add list of domains from a file in that way you don't need to enter domains everytime you need

## WHAT TO DO AFTER GETTING HASH 
you can search that hash like this  [http.favicon.hash:"hash-value"] in shodan to get IP addresses



# INCASE OF ANY ERROR TRY UPDATING PYTHON AND PIP TO LATEST VERSION
