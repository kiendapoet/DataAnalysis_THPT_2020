# I/O file
file = open("data.txt","w")
#write
for i in range(10):
	file.write(str(i) + "\n")
#read
file = open("data.txt","r")

line = file.read().split("\n")
print(len(line))

for i in range(len(line)):
	print(line[i])