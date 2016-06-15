import sys
import os
import csv


in_file = sys.argv[1]

with open(in_file, 'r') as i_f:
	#for line in i_f:
	reader = csv.reader(i_f)

	document_list = []
	sentment_list = []
	for row in reader:
		status = row[1]
		line = row[0]
		sentment_list.append(row[1])

