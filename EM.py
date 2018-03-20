import csv
import numpy as np

readings_x=[]
readings_y=[]

with open('sample EM data (1).csv', 'r') as g:
	reader = csv.reader(g)
	my_list = list(reader)
# print (my_list)
for column in my_list:
	readings_x.append(float(column[0]))
	readings_y.append(float(column[1]))

# print (readings_x)
# print (readings_y)


def step_1(readings):
	cluster_1_ =np.mean(readings)
	cluster_2 = (cluster_1/2)
	cluster_3 = (2*cluster_1)
	a = []
	b= []
	c =[]
	for x in readings:
		s = x -cluster_1
		a.append(s)
	# print (a)
	a_length = len(a)
	# print (a_length)
	for x in readings:
		s = x -cluster_2
		b.append(s)
	# print (a)
	b_length = len(b)
	# print (a_length)
	for x in readings:
		s = x -cluster_3
		c.append(s)
	# print (a)
	c_length = len(c)
	return a
	return b
	return c
