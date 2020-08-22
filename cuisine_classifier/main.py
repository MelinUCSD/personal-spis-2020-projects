# Cuisine Classification Model: 20 classes
import json
import matplotlib.pyplot as plt
import numpy as np

import preprocess

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def getClasses(data):
    ''' Returns a list of the 20 classes '''
    # Number of classses
    classes = [] 
    for x in data:
        if x["cuisine"] not in classes:
            classes.append(x["cuisine"])
    return classes

def getData(data):
    ''' Getting x_train and y_train '''
    x_train = []
    y_train = []
    for x in data:
        x_train.append(np.array(x["ingredients"]))
        y_train.append(np.array(x["cuisine"]))
    return np.array(x_train), np.array(y_train)

def train(x_train, y_train, n):
    ''' Training the model '''
    # Getting the model
    knn = KNeighborsClassifier(n_neighbors=n)
    # Training
    knn.fit(x_train, y_train)
    return knn

def predict(model, input_values):
    ''' Given a custom list of ingredients, predict
        the cuisine '''
    return model.predict(input_values)

def score(model, x_test, y_test):
    ''' Returns the accuracy of the model '''
    return model.score(x_test, y_test)


# Main

# Opening files - Training data
with open("./data/train.json") as f:
    data = json.load(f)
# Opening files - Testing data
#with open("./data/test.json") as f_test:
#    test_data = json.load(f_test)
# Opening files - Predicting data
#with open("./data/unprocessed/test.json") as f_test_id:
#    test_data_id = json.load(f_test_id)
#pprint(test_data_id)

# Getting data
x, y = getData(data)

# Splitting into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

# Reshaping the data to 2D
n_samples, n_x, n_y = x_train.shape
d2_x_train = x_train.reshape((n_samples, n_x * n_y))
n_samples, n_x, n_y = x_test.shape
d2_x_test = x_test.reshape((n_samples, n_x * n_y))

# Training the model
knn = train(d2_x_train, y_train, 10)

## Getting the score
result = score(knn, d2_x_test, y_test)

#=======================================
# Uncommen this section to test main.py
#=======================================

#list_testing = []
#testing = {}
#testing["ingredients"] = ["onion", "extra virgin olive oil",
#                          "tomatoes", "white wine", "greek oregano",
#                          "white pepper", "praws", "feta cheese", "parsley",
#                          "bread", "lemon wedges"]
#testing_2 = {}
#testing_2["ingredients"] = ["extra virgin olive oil",
#                           "garlic", "onion", "oregano",
#                           "kosher salt", "tomatoes", "basil", "spaghetti",
#                           "unsalted butter"]
#list_testing.append(testing)
#list_testing.append(testing_2)
#what = preprocess.main(list_testing)
#for x in what:
#    tmp = np.array(x["ingredients"])
#    n_x, n_y = tmp.shape
#    d1_x_prediction = tmp.reshape(1, n_x * n_y)
#    print(predict(knn, d1_x_prediction))

#count = 0
#for x in range(10):
#    tmp = np.array(test_data[x]["ingredients"])
#    n_x, n_y = tmp.shape
#    d1_x_prediction = tmp.reshape(1, n_x * n_y)
#
#    prediction = predict(knn, d1_x_prediction)
#    print(prediction, test_data[x]["id"])
    #if (prediction[0] == "italian"):
    #    count += 1
    #print(prediction[0], "real:", test_data_id[x]["id"])
#print(count, "out of 10")

#n = 100
#max_accuracy = 0
#best = 0
#for x in range(50):
#    # Training the data
#    knn = train(x_train, y_train, n)
#
#    # Getting the score
#    result = score(knn, x_test, y_test)
#    print(result, n)
#    if (result> max_accuracy):
#        max_accuracy = result 
#        best = n
#    n += 1
#print("Best:", best, "accuracy:", max_accuracy)
