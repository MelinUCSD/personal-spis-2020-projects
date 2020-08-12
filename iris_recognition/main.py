# Iris Classification Model: three classes, four features each.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def train(x_train, y_train):
    ''' Training a model given a np array of data points'''
    # Nearest K-Neighbor
    knn = KNeighborsClassifier(n_neighbors=1)
    # Training
    knn.fit(x_train, y_train)
    return knn

def predict(knn, spln, spwd, ptln, ptwd):
    ''' Given a custom value it will predict the Iris flower '''
    x_new = np.array([[spln, spwd, ptln, ptwd]])
    prediction = knn.predict(x_new)
    if (prediction == 0):
        return iris.target_names[0]
    elif (prediction == 1):
        return iris.target_names[1]
    else:
        return iris.target_names[2]

def score(model, x_test, y_test):
    ''' Returns the accuracy of the model '''
    # Testing range: 0 to 1
    return model.score(x_test, y_test)

def plot(x_value, y_value, target, title, x_label, y_label):
    ''' Produces a scatter plot of the given values '''
    plt.scatter(x_value, y_value, c=target)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    

# Getting the dataset
iris = load_iris()

# Splitting dataset: training (75%) and testing (25%)
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)
# Extracting features
features = iris.data.T
sep_len = features[0]
sep_wid = features[1]
pet_len = features[2]
pet_wid = features[3]

# Getting the labels
sep_len_label = iris.feature_names[0]
sep_wid_label = iris.feature_names[1]
pet_len_label = iris.feature_names[2]
pet_wid_label = iris.feature_names[3]

# Visualazing the data
plot(sep_len, sep_wid, iris.target, "Sepal Length vs Sepal Width", sep_len_label, sep_wid_label)

# Training the model
knn = train(x_train, y_train)

# Predict
spln = float(input("Sepal Length (cm): "))
spwd = float(input("Sepal Width (cm): "))
ptln = float(input("Petal Length (cm): "))
ptwd = float(input("Petal Width (cm): "))
print("Prediction:", predict(knn, spln, spwd, ptln, ptwd))

# Getting the accuracy of the model
print("Accuracy score:", score(knn, x_test, y_test))