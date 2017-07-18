# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_table('../dataset/wine_data', delimiter=',')

# split
X = data.iloc[:, 1:]
y = data.iloc[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)

# scale
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# train
clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(26, 13, 6), max_iter=500)
clf.fit(X_train_scaled, y_train)

# predict and validate
y_pred = clf.predict(X_test_scaled)
print confusion_matrix(y_test, y_pred)
print accuracy_score(y_test, y_pred)

"""
[[42  1  0]
 [ 0 48  1]
 [ 0  0 32]]
0.983870967742
"""
