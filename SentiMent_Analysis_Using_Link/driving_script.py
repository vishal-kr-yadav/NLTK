import json
import data_extraction

with open("data.json") as f:
    dataset = json.load(f)

# print((dataset))

for each in dataset:

    keySourceName = each['sourceName']
    valueLink = each['sourceLink']

    #
    # print("key==",keySourceName)
    # print("value=",valueLink)
    # break

    data_extraction.extract_aff_content(keySourceName, valueLink)