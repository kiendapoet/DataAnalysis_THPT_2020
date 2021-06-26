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
average = [0,0,0,0,0,0,0,0,0,0,0,0]


for s in students:
	count = 0
	total = 0
	for i in range(11):
		if s[i+5] != "-1":
			total += float(s[i+5])
			count += 1

	num_of_exam_taken[count] += 1
	average[count] += total/count

for i in range(12):
	if num_of_exam_taken[i] != 0:
		average[i] = round(average[i]/num_of_exam_taken[i],2)

print(num_of_exam_taken)
print(average)

import matplotlib.pyplot as plt
import numpy 

# list from 0-11
y_pos = numpy.arange(12)
x_pos = numpy.arange(12)

figure, axis = plt.subplots()

# plot the bar chart using 2 list
plt.bar(y_pos, average)

# change horizontal category name
plt.xticks(x_pos, x_pos)

# set limit to vertical axis
axis.set_ylim(0,10)

#label and title
plt.ylabel('Điểm trung bình')
plt.title('Điểm trung bình của các học sinh với số lượng môn thi khác nhau')


# Draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, average):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

# show the plot
plt.show()