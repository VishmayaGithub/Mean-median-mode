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
new_data.sort()    


if(n%2 == 0 ):
    num1 = float(new_data[n//2])
    num2 = float(new_data[n//2-1])
    median = (num1+num2)/2
    print(median)

else:
    num3 = float(new_data[n//2])
    median = num3
    print(median)