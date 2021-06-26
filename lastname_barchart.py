# read file
with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# turn each student to a list
for i in range(len(students)):
	students[i] = students[i].split(",")

# remove empty list (end of file)
students.pop()

name = [] # Danh sách các họ
name_count = [] # số lần lăp lại của họ

for s in students:
	s_name = s[1].split(" ") 
	lastname = s_name[0] 
	if lastname not in name:
		name.append(lastname)
		name_count.append(0)
		name_count[name.index(lastname)] += 1
	else:
		name_count[name.index(lastname)] += 1

counted_max_num = [] # số lần lặp lại các họ từ lớn đến bé

for i in range(len(name)):
	max_number = 0
	for j in range(len(name)):
		if name_count[j] > max_number and name_count[j] not in counted_max_num:
			max_number = name_count[j]

	counted_max_num.append(max_number)

sort_index = []

for max_num in counted_max_num:
	for i in range(len(name)):
		if name_count[i] == max_num and i not in sort_index:
			sort_index.append(i)

name_sorted = [] # Danh sách họ đã sắp xếp
name_count_sorted = [] 

# Dùng sort_index để sắp sếp lại họ và số lần lặp
for index in sort_index:
	name_sorted.append(name[index])
	name_count_sorted.append(name_count[index])

# https://matplotlib.org/3.1.0/gallery/ticks_and_spines/custom_ticker1.html#sphx-glr-gallery-ticks-and-spines-custom-ticker1-py
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20)
y = np.arange(20)

fig, axis = plt.subplots()
plt.bar(x, name_count_sorted[0:20])

# set limit 
axis.set_ylim(0,30000)

# label for column x
plt.xticks(x, name_sorted[0:20])

axis.set_ylabel('Số học sinh')
axis.set_xlabel('Họ')

rects = axis.patches

# Make some labels.
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
labels = name_count_sorted[0:20]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height, label,ha='center', va='bottom')

plt.title('20 họ phổ biến nhất trong kì thi')
	
plt.show()