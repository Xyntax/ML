# coding: utf-8
import matplotlib.pyplot as plt
plt.figure()
plt.title('single variable')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([30,400,100,400])
plt.grid()
xx = [[50],[100],[150],[200],[250],[300]]
yy = [[150],[200],[250],[280],[310],[330]]
plt.plot(xx,yy,'k.')
plt.show()
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xx,yy)
x2 = [[30],[40]]
y2 = model.predict(x2)
plt.plot(x2,y2,'g-')
plt.show()
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
xx  = np.linspace(30,400,100)
quadratic_featurizer = PolynomialFeatures(degree=2)
X_train_quadratic = quadratic_featurizer.fit_transform(X)
X_train_quadratic = quadratic_featurizer.fit_transform(x)
X = [[50],[100],[150],[200],[250],[300]]
y = [[150],[200],[250],[280],[310],[330]]
X_test = [[250],[300]]
y_test = [[310],[330]]
plt.plot(X,y,'k.')
plt.show()
X_train_quadratic = quadratic_featurizer.fit_transform(X)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0],1))
regresson_quadratic = LinearRegression()
regresson_quadratic.fit(X_train_quadratic,y)
plt.plot(xx,regresson_quadratic.predict(xx_quadratic),'r-')
print '一元线性回归 rsquared',model.score(X_test,y_test)
X_test_quadratic = quadratic_featurizer.transform(X_test)
print '二次回归 rsquared',regresson_quadratic.score(X_test_quadratic,y_test)
plt.show()
cubic_featurizer = PolynomialFeatures(degree=3)
X_train_cubic = cubic_featurizer.fit_transform(X)
regressor_cubic = LinearRegression()
regresson_quadratic.fit(X_train_cubic,y)
xx_cubic = cubic_featurizer.transform(xx.reshape(xx.shape[0],1))
plt.plot(xx, regressor_cubic.predict(xx_cubic))
regresson_cubic.fit(X_train_cubic,y)
regressor_cubic.fit(X_train_cubic,y)
plt.plot(xx, regressor_cubic.predict(xx_cubic))
X_test_cubc = cubic_featurizer.transform(X_test)
print '三次回归 r-squared', regressor_cubic.score(X_test_cubc,y_test)
plot.show()
plt.show()
