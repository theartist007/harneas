
def calculate_cost(Y_predicted, Y_actual):

	cost=0
	number_of_terms=len(Y_predicted)
	for i in range(number_of_terms):
		cost=cost+(Y_predicted[i]-Y_actual[i])**2

	return (cost/(number_of_terms))


import csv
import random
from sklearn import linear_model

data_1 = list(csv.reader(open("data1.csv")))
data_2 = list(csv.reader(open("data2.csv")))

header=data_1[0]

core_data_1=data_1[1:]
core_data_2=data_2[1:]

core_data=core_data_1+core_data_2

#random.shuffle(core_data)

dimension_1=len(core_data)
dimension_2=len(core_data[0])

for i in range(dimension_1):
	for j in range(dimension_2):
		core_data[i][j]=int(core_data[i][j])

core_data=[list(i) for i in zip(*core_data)]

Y_full=core_data[-1]
X_full=core_data[:-1]

X_full=[list(i) for i in zip(*X_full)]

size_full=len(Y_full)

X_training=X_full[:int(0.7*size_full)]
X_cv=X_full[int(0.7*size_full):int(0.9*size_full)]
X_test=X_full[int(0.9*size_full):]

Y_training=Y_full[:int(0.7*size_full)]
Y_cv=Y_full[int(0.7*size_full):int(0.9*size_full)]
Y_test=Y_full[int(0.9*size_full):]

alphas=[x*0.1 for x in range(10, 31)]
opt_cost=-1

for alpha in alphas:
	print(alpha)
	reg = linear_model.Ridge(alpha=alpha, fit_intercept=True, normalize=True, copy_X=True)
	reg.fit(X_training, Y_training)

	Y_cv_predicted=reg.predict(X_cv)

	this_alpha_cost=calculate_cost(Y_cv_predicted, Y_cv)
	print(this_alpha_cost, end="\n\n")
	if(this_alpha_cost<opt_cost or opt_cost==-1):
		opt_alpha=alpha
		opt_cost=this_alpha_cost
		opt_theta=reg.coef_

print(opt_theta)

Y_test_predicted=reg.predict(X_test)
print(calculate_cost(Y_test_predicted, Y_test))

for i in range(len(Y_test)):
	print(f'{Y_test_predicted[i]} {Y_test[i]}')

'''
print(X_training)
print("---------------------")
print(Y_training)


print(len(X_training))
print(len(Y_training))
print(len(X_cv))
print(len(Y_cv))
print(len(X_test))
print(len(Y_test))
'''



'''
X=core_data[:-1]
X=[list(i) for i in zip(*X)]

Y=core_data[-1]

reg = linear_model.Ridge(alpha=0, fit_intercept=True, normalize=True, copy_X=True)
reg.fit(X, Y)
print(reg.coef_)
print(reg.predict([[23, 1922, 200]]))
'''
