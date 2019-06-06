from main import *
import os
main_content="I love dhoni"

s = SentimentAnalysis(filename='SentiWordNet.txt',weighting='geometric')

a=s.score(main_content.strip())

print(a)
