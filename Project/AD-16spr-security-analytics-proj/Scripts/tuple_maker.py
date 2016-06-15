import csv
import os
import sys
import time

from textblob.classifiers import NaiveBayesClassifier #using a TextBlob Python library for classification

#the classifier used is Naive Bayes Classifier and the dataset is training dataset of fake reviews. #
#We have 800 fake reiews where 400 are positive and 400 are negative
#this tuple maker has been created to train and test the reviews for the fake dataset.

# python classification_script.py Fake_train.csv Fake_test.csv > Fake_NB_classification.txt
# python classification_script.py Real_train.csv Real_test.csv > Real_NB_classification.txt

with open('Fake_test.csv') as f:
	reader=csv.DictReader(f)
	for line in reader:
		test_data = [tuple(line) for line in csv.reader(f)]

if __name__ == '__main__':

	train_file = sys.argv[1]
	#test_file = sys.argv[2]
	start_time = time.time()

	print "--- "+str(time.time() - start_time)+ " seconds ---"
	print 'Training...'
	with open(train_file, 'rb') as fp:
		cl = NaiveBayesClassifier(fp, format='csv')

	print "--- "+str(time.time() - start_time)+ " seconds ---"
	print 'Testing...'
	
	accuracy_value = cl.accuracy(test_data) 

	print 'Writing to file...'
	print accuracy_value

	cl.show_informative_features(5)

	print "--- "+str(time.time() - start_time)+ " seconds ---"
