###Basic ML Script that test accuracies for various classifiers to see which single classifier performs the best

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import ElasticNet
from sklearn import linear_model
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import BernoulliRBM
from sklearn import metrics
import pandas as pd 
import numpy as np 
import statistics

##Data is OTU Table of numerous patients with Colorectal Canncer 
data_path = r"INPUT_PATH_OF_DATA.csv"
y_pred = None
X_train, X_test, y_train, y_test = None, None, None, None

##Label of the patients' diagnosis (Normal or Syndromic)
label_path = r"INPUT_PATH_OF_LABELS.csv"
label_list = pd.read_csv(label_path, sep="\t", header=None).to_numpy()

binary_labels = []

for j in label_list[0]:
    if "Cancer" in j:
        binary_labels.append(1)

    elif "label" in j:
        pass

    else:
        binary_labels.append(0)


otu_table = pd.read_csv(data_path, index_col=0)

otu_table = otu_table.transpose()

X_train, X_test, y_train, y_test = train_test_split(otu_table, binary_labels, test_size=0.3) # 70% training and 30% test
# y_train = y_train.astype('int')

print(X_test)


# model = RandomForestClassifier(n_estimators=31) ## Random Forest CLassifier with 31 Random Trees developed
# model = LinearSVC() ##Support Vector Machine Classifer 
# model = KNeighborsClassifier(n_neighbors=5) ##KNN Classifier with 5 neighbors
model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(91, 100 ,2), random_state=1, max_iter=750) ##Multi-layer Perceptron classifier
model.fit(X_train,y_train)


y_pred = model.predict(X_test)

# y_test = y_test.astype('int')
print("Accuracy:", metrics.accuracy_score(y_test, y_pred)*100)
