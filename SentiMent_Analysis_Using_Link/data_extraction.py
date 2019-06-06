import requests,re, os
from bs4 import BeautifulSoup
import re, unicodedata

dir = 'data/'
pattern = ['[^!.",?]+']

def remove_punctuation(pattern, phrase):
    for pat in pattern:
        return (re.findall(pat, phrase))

def extract_aff_content(sourceName,url):

    website = requests.get(url)
    soup = BeautifulSoup(website.content)
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]

    f = open(dir+sourceName+'.txt', "w")

    for item in text:

        aa="".join(remove_punctuation(pattern, re.sub('\s+',' ',item)))

        f.write(aa)


# url ='https://sports.ndtv.com/indian-premier-league-2019/prithvi-shaw-gives-update-on-fitness-expects-to-return-in-ipl-2019-1980864'
# sourceName="timesOfIndia"
# a=extract_aff_content(sourceName,url)
# print(a)