**data** : text data after extraction for each link.  
**data.json** : based on the query keywords in goggle_search it will prepare the sourceName and its link.  
**data_extraction.py**: main script for data extraction, this script called from driving.script  
**goggle_search.py** : using the query ,fetch link from google search and prepared the datasert and write down in a file.  
**output.json**: after running the sentimental analysis .this is the final result. it contains the score and its source name.  
**sentiment.py** : main sentiment class , contain all the function for calculating th score.  
**sentimental_score.py**: it call the main class , from which it call the score method .  
**sentiWordNet.txt**: a model that contain all the rules for sentimental analysis.  
