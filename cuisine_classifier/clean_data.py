import json
import sys

def getList(ingredients, features):
    ''' Binarizing the ingredients '''
    tmp = sorted(ingredients)
    result = [0] * len(features)
    for x in features:
        try:
            index = tmp.index(x)
            result[index] = 1
        except ValueError:
            continue
    return result

def saveFeatures(features):
    ''' Saving features to a file '''
    with open("./data/features.json", "w") as f:
        json.dump(features, f)

# Opening source files
with open("./data/unprocessed/train.json") as f:
    data = json.load(f)

# Getting total number of features
max_val = 0
features = []
for x in data:
    if len(x["ingredients"]) > max_val:
        features = sorted(x["ingredients"])
        max_val = len(features)
#saveFeatures(features) # Uncomment if you want to save features
#print(features, len(features))

# Writing to output
with open("./data/train.json", "w") as out_f:
    output = []
    for x in data:
        tmp_list = getList(x["ingredients"], features)
        tmp_dict = {"id": x["id"], "cuisine": x["cuisine"], "ingredients": tmp_list}
        output.append(tmp_dict)
    json.dump(output, out_f)
