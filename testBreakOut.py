import csv
import numpy as np
list_1439 = []
with open("/Users/alexguitar/finance_mal/csv/testBreakOut.csv", newline='') as csvfile:
    for row in csv.reader(csvfile):
        list_1439.append(row[0])


float_list_1439 = [float(x) for x in list_1439]
print(list_1439)

highest = max(float_list_1439)
lowest = min(float_list_1439)
MID = (highest + lowest) / 2

print('highest = ', highest)
print('lowest ＝', lowest)
print('MID = ', MID)

j = 0
for i in range(19):
    # print(list_1439[i])

    if (float_list_1439[i] > MID and float_list_1439[i+1] < MID) or (float_list_1439[i] < MID and float_list_1439[i+1] > MID):
        j+=1
        print(i)
# print(j)
condition1 = highest > lowest*1.14 and j > 2
print (condition1)
print(lowest * 1.14)


# print(MID)