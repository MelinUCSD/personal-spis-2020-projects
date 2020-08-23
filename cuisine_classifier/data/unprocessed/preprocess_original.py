import json
import frequencies

from prettyprinter import pprint

def getYumYum(ingredient, result, secondary_result, class_weight):
    ''' Returns the yumyum value of each ingredient '''
    yumyum = [0, 0, 0]
    # Characteristic of a certain cuisine
    for c in result:
        for i in result[c]:
            if (ingredient == i):
                yumyum[0] = class_weight[c][0]
                return yumyum
    
    cuisines = []
    for c in secondary_result:
        for i in secondary_result[c]:
            if (len(cuisines) == 2):
                # Second index
                yumyum[1] = class_weight[cuisines[0]][1]
                tmp = 0.
                for x in cuisines:
                    tmp += class_weight[x][0]
                # Third index
                yumyum[2] = tmp / float(len(cuisines))
                return yumyum
            elif (ingredient == i):
                cuisines.append(c)
    return yumyum

# Opening source files
data = json.load(open("./train.json"))

# Getting top 10 and lower 3 ingredients
result, secondary_result = frequencies.main()
#pprint(secondary_result)

# Completed data: (yumyum intensity, yumyum origin)
# Shape: (n_samples, 3)
# Getting the weight for 20 classes
classes = ["korean","chinese","japanese","thai","vietnamese","filipino",
            "indian","moroccan","russian","french","british","irish","spanish",
            "italian","greek","jamaican","cajun_creole","brazilian","mexican",
            "southern_us"]
class_weight = {}
region = 1
for x in range(20):
    if (x > 7):
        region = 0
    class_weight[classes[x]] = [(x + 1), region]
#pprint(class_weight)

# Testing getIntensity
processed = []
counting = 0
for menu in data:
    dictionary = {}
    recipe = []
    # Calculating the yumyum value for each ingredient
    for ingredient in menu["ingredients"]:
        yumyum = getYumYum(ingredient,result,secondary_result,class_weight)
        #print(ingredient, menu["cuisine"], yumyum)
        recipe.append(yumyum)
    # Selecting only 5 ingredients
    index = 0
    count = []
    for x in recipe: 
        count.append(recipe.count(x))

    while len(recipe) > 5:
        if [0,0,0] in recipe:
            i = recipe.index([0,0,0])
            count.remove(count[i])
            recipe.remove(recipe[i])
        else:
            for x in recipe:
                if (x[0] == 0):
                    i = recipe.index(x)
                    count.remove(count[i])
                    recipe.remove(recipe[i])
                else:
                    i = count.index(min(count))
                    count.remove(count[i])
                    recipe.remove(recipe[i])
                break
    while len(recipe) < 5:
        recipe.append([0,0,0])

    # Adding processed recipe to main list
    dictionary["id"] = menu["id"]
    #dictionary["cuisine"] = menu["cuisine"] # Comment this line for test
    dictionary["ingredients"] = recipe
    processed.append(dictionary)

#pprint(processed)
#with open("../train.json", "w") as out_f:
with open("../test.json", "w") as out_f:
    json.dump(processed, out_f)
