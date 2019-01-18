import csv
from sklearn import linear_model

data = list(csv.reader(open("data1.csv")))
header=data[0]
core_data=data[1:]
core_data=[list(i) for i in zip(*core_data)]

X=core_data[:-1]
X=[list(i) for i in zip(*X)]

Y=core_data[-1]

reg = linear_model.Ridge(alpha=.5, fit_intercept=True, normalize=True, copy_X=True)
reg.fit(X, Y)
print(reg.coef_)
print(reg.predict([[16, 1603, 60]]))
