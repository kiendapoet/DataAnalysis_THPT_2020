# read file 
with open("clean_data.csv", encoding ='utf8') as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

# remove last student (empty student)
students.pop()

total_student = len(students)

# split header
header = header.split(",")
subject = header[5:]

# split each student in list
for i in range(len(students)):
	students[i] = students[i].split(",")

# num of students who took 0,1,2,.... subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	for i in range(11):
		if s[i+5] != "-1":
			count += 1

	num_of_exam_taken[count] += 1

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = "0","1","2","3","4","5","6","7","8","9","10","11"
sizes = num_of_exam_taken
# explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
