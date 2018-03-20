import csv


readings_x=[]
readings_y=[]

with open('data.csv', 'r') as g:
	reader = csv.reader(g)
	my_list = list(reader)
# print (my_list)
for column in my_list:
	readings_x.append(float(column[0]))
	readings_y.append(float(column[1]))

# print (readings_x)
# print (readings_y)
