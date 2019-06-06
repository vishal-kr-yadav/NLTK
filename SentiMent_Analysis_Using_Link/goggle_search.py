# pip3 install google
# pip3 install google-searchtry:

from googlesearch import search
import re
import json

list_of_google_link = []

def googleSearch(query_keywords):

    for eachLink in search(query_keywords, tld="co.in", num=5, stop=1, pause=2):

        list_of_google_link.append(eachLink)
    return list_of_google_link




def prepare_dataset():
    result = googleSearch("ind vs aus")
    final_list_of_dataset = []
    for each_link in result:
        dict={}
        sourceName = re.search("^https:.*.com",each_link).group(0)
        dict["sourceName"] = sourceName.split('.')[-2]
        dict["sourceLink"] = each_link
        final_list_of_dataset.append(dict)

    with open('data.json', 'w') as outfile:
        json.dump(final_list_of_dataset, outfile)


prepare_dataset()
