import nltk
import string
import os
import sys
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
import operator
from collections import OrderedDict
import json
from ast import literal_eval
#the python script to create the feature-extractor ~ the frequency of the words with the tf-idf values from the trin and test document.

# python feature_extractor_2.py Fake_train.csv Fake_train.csv Fake_train.svm
# python feature_extractor_2.py Fake_train.csv Fake_test.csv Fake_test.svm
# python feature_extractor_2.py Real_train.csv Real_train.csv Real_train.svm
# python feature_extractor_2.py Real_train.csv Real_test.csv Real_test.svm
# python feature_extractor_2.py train.csv train.csv train.svm

token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def item_counter(word_list, line_list):
 	dict_counter = {}
	itemcounter = {item:count for item, count in [(item, line_list.count(item)) for item in word_list]}
	for item, count in itemcounter.iteritems():
		dict_counter[item] = count
	return dict_counter

def mapper(item_dict, value_dict):
	dictionary_value_count = {}
	for key, value in value_dict.iteritems():
		#print key
		#print 'Avisha'
		for key1, value1 in item_dict.iteritems():
			#print key1
			#print 'Das'
			if key == key1:
				#print value, ' - ', value1
				dictionary_value_count[value] = value1

	return dictionary_value_count
if __name__ == '__main__':

	model_file = sys.argv[1]
	tt_file = sys.argv[2]

	out_file = sys.argv[3]


	#Step -1: read the entire train document for the tf-idf vector list. 
	#Step -2: then take each document/review line by line from the train document and convert it into a word:frequency model
	#Step -3: Repeat Step-2 for test file.


	#Step -1: read the entire train document for the tf-idf vector list.

	with open(model_file, 'r') as mod_file: #reading the input training file in csv format and creating the TFIDF vector
		reader = csv.reader(mod_file)
		for row in reader:
			line = row[0]
			lowers = line.lower()
			no_punctuation = lowers.translate(None, string.punctuation)
			token_dict[line] = no_punctuation
        	

	#this can take some time
	tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
	tfs = tfidf.fit_transform(token_dict.values())

	#print tfs 

	#Step -2a: then take each document/review line by line from the train document and convert it into a word:frequency model


	with open(tt_file, 'r') as in_file:
	
		with open(out_file, 'wb') as o_file:
			reader_in = csv.reader(in_file)

			for row in reader_in:
				line = row[0]
				status = row[1]

				if status == 'pos':
					o_file.write('+1 ')
				elif status == 'neg':
					o_file.write('-1 ')


				additional_dict = {}
				dictionary = {}
				values_dict = {}
				list_of_words = []
				list_of_values = []

				lower_case = line.lower()
				string_line = lower_case.translate(None, string.punctuation)
				line_list = tokenize(str(string_line))
    		

			#print line
				response_tr = tfidf.transform([line]) #response on each line of the training vector
				feature_names = tfidf.get_feature_names()
				for col in response_tr.nonzero()[1]:
				#print col, '-', feature_names[col]
					additional_dict[str(feature_names[col])] = col+1 #mapping of column values+1
				#print additional_dict
					dictionary[str(feature_names[col])] = response_tr[0, col]
					values_dict[str(col)] = response_tr[0, col]
           			sorted_value = sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True)
           			sorted_value_value = sorted(values_dict.items(), key = operator.itemgetter(1), reverse = True)
           		#print additional_dict
           		#print dictionary
           		#print values_dict
           		#print sorted_value
           		#print sorted_value_value
           			for tuple_val in sorted_value_value:
           				list_of_values.append(tuple_val[0])
           		#master_list_of_values.append(list_of_values)	
          	 		for tuple_ in sorted_value:
         	  			list_of_words.append(tuple_[0])
        		#master_list_of_words.append(list_of_words)
        		#print list_of_words
        		#print line_list

        			item_dict = item_counter(list_of_words,line_list)
        			#print item_dict || cross checking data
        			#print additional_dict || Cross checking data

        			dictionary_map_count = mapper(item_dict,additional_dict)
        			#print OrderedDict(sorted(dictionary_map_count.items(), key=lambda t: t[0]))

        			d = OrderedDict(sorted(dictionary_map_count.items(), key=lambda t: t[0]))
        			#dstring = json.dumps(d)
        			#print '-----------------------------'
        			# output_dict = json.loads(json.dumps(d))
        			#print dstring
        			#print dictionary_map_count
        			for key, value in d.iteritems():
        				o_file.write(str(key) + ':' + str(value) + ' ')
        			o_file.write('\n')

        			# for key, value in dictionary_map_count.iteritems():
        			# 	o_file.write(str(key) + ':' + str(value) + ' ')
        			# o_file.write('\n')
        			#dic = literal_eval(dstring)
        			#print dic
        			#print '-----------------------------'
        			
        			

				#print dictionary_map_count
    #     		dict_counter = {}
    #     		itemcounter = {item:count for item, count in [(item, line_list.count(item)) for item in list_of_words]}
    #     		for item, count in itemcounter.iteritems():
				# 	dict_counter[item] = count
				# print dict_counter
				
	

    	
    		
    		
