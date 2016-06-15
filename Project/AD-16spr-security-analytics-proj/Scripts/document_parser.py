import os
import sys
from os.path import isdir, join
import glob

# a script to parse each folder under op_spam_v1.4

if __name__ == '__main__':

	path = 'C:\Users\Avisha\Desktop\SPRING 2016\Security Analytics\Project\op_spam_v1.4' # path to the dataset

	folder_list_1 = os.listdir(path)

	#check if a directory
	# for f in folder_list_1:
	# 	if isdir(join(path,f)) == True:
	# 		print f

	#folder_list_2 = [f for f in folder_list_1 if isdir(join(path,f))]

	print folder_list_1


	for f_2 in folder_list_1:
		if isdir(join(path,f_2)) == True:
			new_path = path + '\\' + f_2
			print new_path

			folder_list_3 = os.listdir(new_path)
		 	print folder_list_3

			for f_3 in folder_list_3:
				new_new_path = new_path + '\\' + f_3

				print new_new_path

				folder_list_4 = os.listdir(new_new_path)
				print folder_list_4

		 		for f_4 in folder_list_4:
		 			new_new_new_path = new_new_path + '\\' + f_4

			 		print new_new_new_path

		 			folder_list_5 = os.listdir(new_new_new_path)
		 			print folder_list_5

		 			new_new_new_path_rename = new_new_new_path.replace('\\','_')

		 			with open (new_new_new_path_rename, "wb") as write_file:
			 			for file in os.listdir(new_new_new_path):
							print os.getcwd()
							os.chdir(new_new_new_path)
							print os.getcwd()
							with open (file, "rb") as read_file:
		 						write_file.write(read_file.read())




		
