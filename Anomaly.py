import random
from math import exp, pi, log
import csv
import numpy as np 
import pandas as pd 

import matplotlib
import matplotlib.pyplot as plt

TOL_PER=0

def getMyu(vector):
	return sum(vector)/len(vector)

def getSigmaSq(vector, myu):
	s=0
	for i in vector:
		s=s+(i-myu)*(i-myu)
	return s/len(vector)

def getProb(x, myu, sigma_sq):
	denom=((2*pi*sigma_sq)**0.5)
	num=exp(   ( (x-myu)**2    )/(-2*sigma_sq)     )
	return num/denom

def addTolerance(a, tol_per):
	small, big=a
	return (small - 0.01*tol_per*small, big + 0.01*tol_per *big)

def getValue(prob, myu, sigma_sq):
	just_another_temp_var=(-2*sigma_sq*log(prob*((2*pi*sigma_sq)**0.5)))**0.5
	return (-just_another_temp_var + myu, + just_another_temp_var +myu)

def calc_Fscore(Y_predicted, Y_actual):

	true_pos=[1  for i in range(len(Y_actual)) if Y_predicted[i]==1 and Y_actual[i]==1]
	false_pos=[1 for i in range(len(Y_actual)) if Y_predicted[i]==1 and Y_actual[i]==0]
	false_neg=[1 for i in range(len(Y_actual)) if Y_predicted[i]==0 and Y_actual[i]==1]

	true_pos=sum(true_pos)
	false_neg=sum(false_neg)
	false_pos=sum(false_pos)

	try:
		precision=(true_pos)/(true_pos + false_pos)
	except:
		precision=0

	try:
		recall = (true_pos)/(true_pos + false_neg)
	except:
		recall=0

	try:
		return (2*precision*recall)/(precision + recall)
	except:
		return 0


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


X_train_press=data_train[0]
X_train_rpm=data_train[1]
Y_train=data_train[-1]
Y_train=list(map( lambda x: 1 if x>=55 else 0 , Y_train))

#print(Y_train)

X_cv_press=data_cv[0]
X_cv_rpm=data_cv[1]
Y_cv=data_cv[-1]
Y_cv=list(map( lambda x: 1 if x>=55 else 0 , Y_cv))

X_test_press=data_test[0]
X_test_rpm=data_test[1]
Y_test=data_test[-1]
Y_test=list(map( lambda x: 1 if x>=55 else 0, Y_test))




#PRESSURE
probabilities_pressure=[0]*len(Y_train)
myu_p=getMyu(X_train_press)
sigma_sq_p=getSigmaSq(X_train_press, myu_p)
for i in range(len(Y_train)):
	probabilities_pressure[i]=getProb(X_train_press[i], myu_p, sigma_sq_p)

opt_epsilon=0
max_Fscore=0
for epsilon in [0.0000001*x for x in range(100)]:
	temp_pred=list(map(lambda y: 1 if y<epsilon else 0, probabilities_pressure ))
	this_Fscore=calc_Fscore(temp_pred, Y_train)
	if(this_Fscore>max_Fscore):
		max_Fscore=this_Fscore
		opt_epsilon=epsilon

for epsilon in [0.00001*x for x in range(100)]:
	temp_pred=list(map(lambda y: 1 if y<epsilon else 0, probabilities_pressure ))
	this_Fscore=calc_Fscore(temp_pred, Y_train)
	if(this_Fscore>max_Fscore):
		max_Fscore=this_Fscore
		opt_epsilon=epsilon

for epsilon in [0.001*x for x in range(1000)]:
	temp_pred=list(map(lambda y: 1 if y<epsilon else 0, probabilities_pressure ))
	this_Fscore=calc_Fscore(temp_pred, Y_train)
	if(this_Fscore>max_Fscore):
		max_Fscore=this_Fscore
		opt_epsilon=epsilon


#print(opt_epsilon)
print("The non-anomalous values of pressure are: ")
print(addTolerance(getValue(opt_epsilon, myu_p, sigma_sq_p ), TOL_PER))


#RPM

probabilities_rpm=[0]*len(Y_train)
myu_rpm=getMyu(X_train_rpm)
sigma_sq_rpm=getSigmaSq(X_train_rpm, myu_rpm)
for i in range(len(Y_train)):
	probabilities_rpm[i]=getProb(X_train_rpm[i], myu_rpm, sigma_sq_rpm)

opt_epsilon=0
max_Fscore=0
for epsilon in [0.0000001*x for x in range(100)]:
	temp_pred=list(map(lambda y: 1 if y<epsilon else 0, probabilities_rpm ))
	this_Fscore=calc_Fscore(temp_pred, Y_train)
	if(this_Fscore>max_Fscore):
		max_Fscore=this_Fscore
		opt_epsilon=epsilon

for epsilon in [0.00001*x for x in range(100)]:
	temp_pred=list(map(lambda y: 1 if y<epsilon else 0, probabilities_rpm ))
	this_Fscore=calc_Fscore(temp_pred, Y_train)
	if(this_Fscore>max_Fscore):
		max_Fscore=this_Fscore
		opt_epsilon=epsilon

for epsilon in [0.001*x for x in range(100)]:
	temp_pred=list(map(lambda y: 1 if y<epsilon else 0, probabilities_rpm ))
	this_Fscore=calc_Fscore(temp_pred, Y_train)
	if(this_Fscore>max_Fscore):
		max_Fscore=this_Fscore
		opt_epsilon=epsilon

print(opt_epsilon)
print("The non-anomalous values of rpm are: ")
print(addTolerance(getValue(opt_epsilon, myu_rpm, sigma_sq_rpm ), TOL_PER))
#X_train=[list(i) for i in zip(*X_train)]
#X_cv=[list(i) for i in zip(*X_cv)]
#X_test=[list(i) for i in zip(*X_test)