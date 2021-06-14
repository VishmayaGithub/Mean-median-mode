import csv
#mean = addition of all data/number of data

with open('Socr-HeightWeight.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    new_num = file_data[i][1]
    new_data.append(float(new_num))

n = len(new_data)
total = 0

for x in new_data:
    total+=x

mean = total/n
print(n)
print(total)
print('Mean =',str(mean))