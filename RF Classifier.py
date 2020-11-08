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
import sys

data_path = r"E:\Mohammad\Microbiome\CRC_Data\otu.csv"
y_pred = None
X_train, X_test, y_train, y_test = None, None, None, None

label_path = r"E:\Mohammad\Microbiome\CRC_Data\crc1+2_label_vector.tab"
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

# otu_nolabel = otu_table.drop(columns=['label'])
# otu_labels = otu_table['label']

X_train, X_test, y_train, y_test = train_test_split(otu_table, binary_labels, test_size=0.3) # 70% training and 30% test
# y_train = y_train.astype('int')

print(X_test)

sys.exit()

# model = RandomForestClassifier(n_estimators=31)
# model = LinearSVC()
# model = KNeighborsClassifier(n_neighbors=5)
# model = ElasticNet(random_state=0)
# model = linear_model.Lasso(alpha=0.1)
model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(91, 100 ,2), random_state=1, max_iter=750)
model.fit(X_train,y_train)


y_pred = model.predict(X_test)

# y_test = y_test.astype('int')
print("Accuracy:", metrics.accuracy_score(y_test, y_pred)*100)