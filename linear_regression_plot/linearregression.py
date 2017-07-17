# coding: utf-8
import numpy as np
from sklearn.linear_model import LinearRegression
x = [[1],[2],[3],[4],[5],[6]]
y = [[1],[2.1],[2.9],[4.2],[5.1],[5.8]]
model = LinearRegression()
model.fit(x,y)
predicted = model.predict([[13]])[0]
print predicted
