import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from numpy import genfromtxt

my_data = genfromtxt('data1.csv', delimiter = ',');
time = press = rpm = temp = [];

firstRow = 0;
for l in my_data:
	if(firstRow == 0) : 
		firstRow = 1;
		continue;
	press.append(l[0])
	rpm.append(l[1])
	time.append(l[2])
	temp.append(l[3])

press = np.array(press);
rpm = np.array(rpm);
time = np.array(time);
temp = np.array(temp);

deg = 3;

x = np.ones(len(temp));
i, p, a = 0, "", x;

for i in range(0, deg) :
	q, b = "", x;
	for j in range(0, deg) :
		s, c = "", x;
		for k in range(0, deg) : 
			if(i != 0 or j != 0 or k != 0) : 
				x_axis = p + q + s;
				x_axis = x_axis[:-1];
				print(x_axis);
				#plot and save graph
				plt.plot(a*b*c, temp);
				plt.xlabel(x_axis);
				plt.ylabel('TEMP');
				plt.savefig(x_axis + '.jpg')
				plt.gcf().clear();
			s += "TIMEx";
			c = c * time;
		q += "RPMx";
		b = b * rpm;
	p += "PRESSx";
	a = a * press;
