def percentage_accuracy(Y_predicted, Y_actual):
	number_of_terms=len(Y_predicted)
	error_per=0
	for i in range(number_of_terms):
		error_per=error_per+abs(Y_predicted[i]-Y_actual[i])/(Y_actual[i])

	return 100-(error_per*100/(number_of_terms))

def predict(opt_intercept, opt_theta, X_test):
	Y_test_predicted=[]

	no_of_features=len(X_test[0])

	for features in X_test:
		
		ans=opt_intercept
		for i in range(no_of_features):
			ans=ans+(features[i]*opt_theta[i])
		
		Y_test_predicted.append(ans)

	return Y_test_predicted


def calculate_cost(Y_predicted, Y_actual):

	cost=0
	number_of_terms=len(Y_predicted)
	for i in range(number_of_terms):
		cost=cost+(Y_predicted[i]-Y_actual[i])**2

	return (cost/(number_of_terms))





from sklearn.preprocessing import StandardScaler
import csv
import random
from sklearn import linear_model
import matplotlib.pyplot as plt




data_train=list(csv.reader(open("data_train.csv")))
data_cv=list(csv.reader(open("data_cv.csv")))
data_test=list(csv.reader(open("data_test.csv")))


header=data_train[0]

data_train=data_train[1:]
data_cv=data_cv[1:]
data_test=data_test[1:]


dimension_1=len(data_train)
dimension_2=len(data_train[0])

for i in range(dimension_1):
	for j in range(dimension_2):
		data_train[i][j]=int(data_train[i][j])

dimension_1=len(data_cv)
dimension_2=len(data_cv[0])

for i in range(dimension_1):
	for j in range(dimension_2):
		data_cv[i][j]=int(data_cv[i][j])

dimension_1=len(data_test)
dimension_2=len(data_test[0])

for i in range(dimension_1):
	for j in range(dimension_2):
		data_test[i][j]=int(data_test[i][j])



data_train=[list(i) for i in zip(*data_train)]
data_cv=[list(i) for i in zip(*data_cv)]
data_test=[list(i) for i in zip(*data_test)]


X_train=data_train[:-1]
Y_train=data_train[-1]

X_cv=data_cv[:-1]
Y_cv=data_cv[-1]

X_test=data_test[:-1]
Y_test=data_test[-1]

X_train=[list(i) for i in zip(*X_train)]
X_cv=[list(i) for i in zip(*X_cv)]
X_test=[list(i) for i in zip(*X_test)]

#TESTED TILL HERE
'''
scaler = StandardScaler()
scaler.fit(X_training)

X_training=scaler.transform(X_training)
X_cv=scaler.transform(X_cv)
X_test=scaler.transform(X_test)
'''
alphas=[x*0.1 for x in range(0, 50)]
opt_cost=-1

for alpha in alphas:
	print(alpha)
	reg = linear_model.Ridge(alpha=alpha, fit_intercept=True, normalize=True, copy_X=True)
	reg.fit(X_train, Y_train)

	Y_cv_predicted=reg.predict(X_cv)

	this_alpha_cost=calculate_cost(Y_cv_predicted, Y_cv)
	print(this_alpha_cost, end="\n\n")
	if(this_alpha_cost<opt_cost or opt_cost==-1):
		opt_alpha=alpha
		opt_cost=this_alpha_cost
		opt_theta=reg.coef_
		opt_intercept=reg.intercept_

print('Optimum ALPHA= {}'.format(opt_alpha))
print('Optimum INTERCEPT= {}'.format(opt_intercept))
print('Optimum THETA= {}'.format(opt_theta))

#print(list(zip(Y_test, predict(opt_intercept, opt_theta, X_test))))
Y_test_predicted=predict(opt_intercept, opt_theta, X_test)
print('\nThe accuracy of the used test set is: {}'.format(percentage_accuracy(Y_test_predicted, Y_test)))


print('\n\nGenerating DoctorsManual.csv ...')
import numpy as np

#file=open("DoctorsManual.csv", "w")

lines=[["Pressure", "Approximate_Safe_RPM"]]

for P in range(10, 32):
	print(P)
	coeff=[P*P*opt_theta[7] + P*opt_theta[5] + opt_theta[3], opt_theta[6]*P*P + opt_theta[4]*P + opt_theta[1], opt_theta[0]*P + opt_intercept -60 ]
	print(np.roots(coeff))
	print()


print("DoctorsManual.csv written succesfully")

'''
Y_test_predicted=reg.predict(X_test)
'''

'''
print(opt_theta)

print(calculate_cost(Y_test_predicted, Y_test))

for i in range(len(Y_test)):
	print(f'{Y_test_predicted[i]} {Y_test[i]}')
'''

'''
print("The accuracy of prediction is:")
print(percentage_accuracy(Y_test_predicted, Y_test))

print(reg.intercept_)
print(opt_theta)
print(opt_alpha)
print(scaler.scale_)
print(scaler.mean_)

print(scaler.transform([[18,	1665,	430,	2772225,	29970,	49900050,	539460,	898200900]]))
print(reg.predict(scaler.transform([[18,	1665,	430,	2772225,	29970,	49900050,	539460,	898200900]])))
'''

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
