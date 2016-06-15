import os
import sys

path = 'C:\Users\Avisha\Desktop\SPRING 2016\Security Analytics\Project\op_spam_v1.4\\negative_polarity\deceptive_from_MTurk\\fold1'

print os.listdir(path)

print os.getcwd()

with open("NP_MTurk_dec_f1.txt", "wb") as out_file:
	for file in os.listdir(path):
		if file.endswith(".txt"):
			with open(file, "rb") as in_file:
				out_file.write(in_file.read())