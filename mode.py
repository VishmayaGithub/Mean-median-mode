import csv
from typing import Counter
#mean = addition of all data/number of data

with open('Socr-HeightWeight.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    new_num = file_data[i][1]
    new_data.append(float(new_num))

data = Counter(new_data)

mode_data_blah = {
                   '50 - 60':0,
                   '60 - 70':0,
                   '70 - 80':0
                }

for height,occurence in data.items():
    if 50< float(height) < 60:
        mode_data_blah['50 - 60'] += occurence

    
    elif 60< float(height) < 70:
        mode_data_blah['60 - 70'] += occurence 

    elif 70< float(height) < 80:
        mode_data_blah['70 - 80'] += occurence 

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_blah.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")        
