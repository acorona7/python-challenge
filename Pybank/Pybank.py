import os
import csv

csvpath = 'Pybank_Resources.csv'

PLTotal = []
Differences = []
Dates = [] 

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	header = next(csvreader)

	counter = 0
	total = 0
	for lines in csvreader:
		PLTotal.append(int(lines[1]))
		Dates.append(lines[0])
		counter = counter + 1 
		total = total + int(lines[1])
	for i in range(len(PLTotal)-1):
		#print(PLTotal[i])  # 0 => 867884 , 1 => 984655
		#print(PLTotal[i+1]) # 1 =>984655 , 2 => 322013
		Differences.append(PLTotal[i+1]-PLTotal[i])
	print(Differences)
	print(counter)
	print(total)
	print(sum(Differences) / (counter - 1))
	#print(counter, total)
	print(max(Differences))
	print(min(Differences))
	print(Dates)
	maximum_index = (Differences.index(max(Differences)))
	maximum_index += 1
	print(Dates[maximum_index])
	minimum_index = (Differences.index(min(Differences)))
	minimum_index += 1
	print(Dates[minimum_index])
