# Iris Classification Model: three classes, four features each.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Getting the dataset
iris = load_iris()

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
plt.scatter(sep_len, sep_wid, c=iris.target)
plt.title("Sepal Length vs Sepal Width")
plt.xlabel(sep_len_label)
plt.ylabel(sep_wid_label)
#plt.show()

# Splitting dataset: training (75%) and testing (25%)
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)
# Nearest K-Neighbor
knn = KNeighborsClassifier(n_neighbors=1)

# Training
knn.fit(x_train, y_train)

# Predict
spln = float(input("sep_length: "))
spwd = float(input("sep_width: "))
ptln = float(input("pet_length: "))
ptwd = float(input("pet_width: "))
x_new = np.array([[spln, spwd, ptln, ptwd]])
prediction = knn.predict(x_new)
if (prediction == 0):
    print(iris.target_names[0])
elif (prediction == 1):
    print(iris.target_names[1])
else:
    print(iris.target_names[2])

# Testing (0 - 1)
score = knn.score(x_test, y_test)
print("Accuracy score:", score)
