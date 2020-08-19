# Cuisine Classification Model: 20 classes

import json
import matplotlib.pyplot as plt
import numpy as np

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
        x_train.append(x["ingredients"])
        y_train.append(x["cuisine"])
    return x_train, y_train

def train(x_train, y_train):
    ''' Training the model '''
    # Getting the model
    knn = KNeighborsClassifier(n_neighbors=1)
    # Training
    knn.fit(x_train, y_train)
    return knn

with open("./data/train.json") as f:
    data = json.load(f)

# Getting data
x_train, y_train = getData(data)
print(len(x_train[0]), len(x_train[1]))

# Training the data
#knn = train([x_train], y_train)
