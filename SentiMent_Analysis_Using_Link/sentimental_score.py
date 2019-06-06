# https://github.com/anelachan/sentimentanalysis
from sentiment import *
import os
import json
# 'geometric', 'harmonic', 'average'
data_dir='/home/vishal/MEGA/NLTK/SentiMent_Analysis_Using_Link/data/'
list_of_text_files= [path for path in os.listdir(data_dir) if os.path.isdir(data_dir)]
# file_list=['1.txt','2.txt','3.txt','4.txt','5.txt']
result=[]
for each in list_of_text_files:
    d = {}

    f = open(data_dir+each, "r")
    content = (f.read())
    f.close()
    main_content = os.linesep.join([s for s in content.splitlines() if s])
    main_content_after_removing_new_line=main_content.replace('\n', '')

    s = SentimentAnalysis(filename='SentiWordNet.txt',weighting='geometric')

    a=s.score(main_content_after_removing_new_line.strip())
    d['score']=a
    fileName=each.split('.')[0]
    d['fileName']=fileName
    result.append(d)

with open('output.json', 'w') as outfile:
    json.dump(result, outfile)

