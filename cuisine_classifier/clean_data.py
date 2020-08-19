import json

with open("./data/unprocessed/train.json") as f:
    data = json.load(f)

# There are 12 features
max_val = 0
features = []
for x in data:
    if len(x["ingredients"]) > max_val:
        features = sorted(x["ingredients"])
        max_val = len(features)
#print(features, len(features))

def getList(ingredients, features):
    tmp = sorted(ingredients)
    result = [0] * len(features)
    for x in features:
        try:
            index = tmp.index(x)
            result[index] = 1
        except ValueError:
            continue
    return result

# Create a new clean train.json
with open("./data/train_clean.json", "w") as out_f:
    for x in data:
        tmp_list = getList(x["ingredients"], features)
        tmp_dict = {"id": x["id"], "cuisine": x["cuisine"], "ingredients": tmp_list}
        json.dump(tmp_dict, out_f)
