import json
import numpy as np
import pandas as pd
import pickle as pk

from prettyprinter import pprint
from sklearn.metrics.pairwise import cosine_similarity

def predict(df, classes, recipe):
    ''' Predicts the cuisine of the recipe '''
    cos_sim = cosine_similarity(df, recipe)
    count = 0
    #print(cos_sim)
    for x in cos_sim:
        count = max(count, x)
    return classes[np.where(cos_sim==count)[0][0]]
    
def preprocess(recipe, all_ingredients):
    dataframe = [[0 for _ in range(len(all_ingredients))]]
    for ingredient in recipe:
        try:
            dataframe[0][all_ingredients.index(ingredient)] += 1
        except ValueError:
            continue
    return dataframe

# Getting some test cases
with open("./data/unprocessed/test.json") as f:
    test_data = json.load(f)

# Getting the model
df = pd.read_pickle("./data/preprocess/cosine_similarity/dataframe.pickle")
#print(df)

# Getting the classes
with open("./data/preprocess/cosine_similarity/classes.txt", "rb") as fp:
    classes = pk.load(fp)
# Getting all the ingredients
all_ingredients = list(df.columns.values)

# Testing predict
#for recipe in test_data:
#    preprocessed_recipe = preprocess(recipe["ingredients"], all_ingredients)
#    prediction = predict(df, classes, preprocessed_recipe)
#    print(prediction)
#    #exit()

# Personalized menu
menu = ["spaguetti", "tomatoes", "extra virgin olive oil", "fresh oregano",
        "garlic", "salt", "ground black pepper"] # Incorrect
menu2 = ["taramara", "stale bread", "lemons", "red onion"] # Correct
menu3 = ["chicken", "onion", "diced green chiles", "beans", "tortillas",
          "cheese", "cilantro", "avocado", "red onion", "sour cream", "cotija"]
menu4 = ["eggplant", "tomatoes", "yellow squashes", "zucchini", "olive oil",
         "onion", "garlic cloves", "red bell pepper", "salt", "pepper",
          "crushed tomatoes", "fresh basil", "parsley"]
preprocessed_recipe = preprocess(menu4, all_ingredients)
print(predict(df, classes, preprocessed_recipe))
