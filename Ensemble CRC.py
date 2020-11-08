from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
from random import randint
import pandas as pd 
import numpy as np 
import statistics
import sys

Accuracy_scores = []
class_acc = []
for i in range(14):
    class_acc.append([])

for i in range(20):
    print(f"********************Round {i}********************")

    data_path = r"E:\Mohammad\Microbiome\CRC_Data\OTU_Cluster_216.xlsx"
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

    percent_train = 0.70
    num_subjects = round(216*percent_train)

    train_index_list = []
    s = 0
    while s < num_subjects:
        index = randint(0,215)
        if index in train_index_list:
            pass
        else:
            train_index_list.append(index)
            s += 1

    test_index_list = []
    for i in range(216):
        if i in train_index_list:
            pass
        else:
            test_index_list.append(i)

    for k in range(14):
        otu_table = pd.read_excel(data_path, sheet_name=k, index_col=0)
        input_layer = len(otu_table)
        
        otu_table = otu_table.transpose()
        # otu_nolabel = otu_table.drop(columns=['label'])
        # otu_labels = otu_table['label']

        # if k == 0:
        #     X_train, X_test, y_train, y_test = train_test_split(otu_table, binary_labels, test_size=0.3) # 70% training and 30% test
        # y_train = y_train.astype('int')

        X_train = otu_table.iloc[train_index_list, :]
        y_train = []
        for index in train_index_list:
            y_train.append(binary_labels[index])

        X_test = otu_table.iloc[test_index_list, :]
        y_test = []
        for index in test_index_list:
            y_test.append(binary_labels[index])
        

        if input_layer == 2:
            nestimator = 1
        else:
            nestimator = round(input_layer/2.5)

        model = RandomForestClassifier(n_estimators=100)
        # model = LinearSVC(max_iter=5000)
        # model = KNeighborsClassifier(n_neighbors=5)
        # model = MLPClassifier(solver='lbfgs', alpha=0.00005, hidden_layer_sizes=(round(input_layer*2),3), random_state=1, max_iter=800)
        model.fit(X_train,y_train)
        classifier_pred = model.predict(X_test)

        classifier_accuracy = metrics.accuracy_score(y_test, classifier_pred)*100

        class_acc[k].append(classifier_accuracy)

        # print(f"Classifier {k}\tAccuracy: {classifier_accuracy}")

        if k == 0:
            y_pred = np.array(model.predict(X_test))

        else:
            y_pred += np.array(model.predict(X_test))
        
    y_final_pred = []
    for m in y_pred:

        if m >= 7:
            y_final_pred.append(1)
        
        else:
            y_final_pred.append(0)

    # y_test = y_test.astype('int')
    # print("Accuracy:", metrics.accuracy_score(y_test, y_final_pred)*100)
    Accuracy_scores.append(metrics.accuracy_score(y_test, y_final_pred)*100)

print(statistics.mean(Accuracy_scores))

for i in range(len(class_acc)):
    print(f"Classifier {i}\tAvg_Accuracy: {statistics.mean(class_acc[i])}")