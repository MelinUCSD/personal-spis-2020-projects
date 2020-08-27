import json
import pandas as pd
import pickle as pk

from prettyprinter import pprint
from sklearn.metrics.pairwise import cosine_similarity

with open("../../unprocessed/train.json") as f:
    data = json.load(f)

# This is going to be the rows of my data frame
classes = []
#classes.append([x["cuisine"] for x in data if x["cuisine"] not in classes])
for x in data:
    if x["cuisine"] not in classes:
        classes.append(x["cuisine"])
with open("./classes.txt", "wb") as fp:
    pk.dump(classes,fp)
# Getting all ingredients
all_ingredients = []
for x in data:
    for ingredient in x["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
#print(all_ingredients)

# Getting a count vector of all the ingredients in all the cuisines 
dataframe = [[0 for __ in range(len(all_ingredients))] for _ in range(len(classes))]
for recipe in data:
    #print("Cuisine:", recipe["cuisine"])
    for ingredient in recipe["ingredients"]:
        #print(ingredient)
        dataframe[classes.index(recipe["cuisine"])][all_ingredients.index(ingredient)] += 1
#print("Finished")
#pprint(dataframe)

# Convert sparse matrix to Pandas dataframe
df = pd.DataFrame(dataframe, columns=all_ingredients, index=classes)
df.to_pickle("dataframe.pickle")
#print(df)

# Compute cosine similarity
#cos_sim = cosine_similarity(df, df)
#print(cos_sim)
