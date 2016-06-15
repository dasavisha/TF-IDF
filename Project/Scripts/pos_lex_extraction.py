import os
import sys


#this is a python script to extract features from the dataset.
#this creates a frequency based extraction from the dataset.
# python pos_lex_extraction.py <name_of_lexicon> <text_file> <out_file>

def read_lexicon(document):
	#reads the words from the lexicon into a list
	list_of_words = []
	with open(document, 'rb') as in_file:
		for line in in_file:
			line = line.strip('\r\n')
			list_of_words.append(line)
		#print list_of_words
		return list_of_words

def calculate_word_frequency(text_file, word_list):
	#calculate the frequency of a word from the lexicon in the document

	list_of_lines = []
	with open(text_file, 'rb') as t_file:
		line_word_list = []
		for line in t_file:
			line = line.replace("\r\n","")
			line_word_list = line.split(' ')
			
			list_of_lines.append(line_word_list)	

	#print list_of_lines

	list_dictionary = {}

	for word in word_list:
		list_dictionary[word] = 0

	list_lines = []
	with open(text_file, 'rb') as in_file:
		for line in in_file:
			line = line.replace("\r\n","")
			list_lines.append(line)

		#print list_lines

	for key in list_dictionary:
		for line in list_lines:
			if key in line:
				list_dictionary[key] += 1

	return list_dictionary


def write_output(out_file, list_dictionary):

	with open(out_file, 'wb') as o_file:
		o_file.write('Frequency Calculator based on Lexicon: \n')

		for k in list_dictionary:
			o_file.write(str(k)+ ':' + str(list_dictionary[k]))
			o_file.write('\n')

if __name__ == '__main__':

	lexicon = sys.argv[1]
	text_file = sys.argv[2]
	out_file = sys.argv[3]

	list_of_words = read_lexicon(lexicon)
	#print list_of_words

	list_dictionary = calculate_word_frequency(text_file, list_of_words)

	write_output(out_file, list_dictionary)

	print "Done..."
