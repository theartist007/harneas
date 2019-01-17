import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from numpy import genfromtxt

my_data = genfromtxt('data1.csv', delimiter = ',');
time=[]
press=[]
rpm=[]
temp=[]

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

deg = 2;

x = np.ones(len(temp));
i, p, a = 0, "", x;
while i <= deg : 
	j, q, b = 0, "", x;
	while j <= deg :
		k, s, c = 0, "", x;
		while k <= deg :
			if(i != 0 or j != 0 or k != 0) : 
				x_axis = p + q + s;
				x_axis = x_axis[:-1];
				#plot and save graph
				plt.plot(a*b*c, temp);
				plt.xlabel(x_axis);
				plt.ylabel('TEMP');
				plt.savefig(x_axis + '.jpg')
				plt.gcf().clear();
			s += "TIMEx"
			c = c * time;
			k += 1;
		q += "RPMx"
		b = b * rpm;
		j += 1;
	p += "PRESSx";
	a = a * press;
	i += 1;
