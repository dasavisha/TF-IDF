import os
import sys
import time

from textblob.classifiers import NaiveBayesClassifier #using a TextBlob Python library for classification

#the classifier used is Naive Bayes Classifier and the dataset is training dataset of fake reviews. #
#We have 800 fake reiews where 400 are positive and 400 are negative

# python classification_script.py Fake_train.csv Fake_test.csv > Fake_NB_classification.txt
# python classification_script.py Real_train.csv Real_test.csv > Real_NB_classification.txt



if __name__ == '__main__':

	train_file = sys.argv[1]
	test_file = sys.argv[2]
	start_time = time.time()

	print "--- "+str(time.time() - start_time)+ " seconds ---"
	print 'Training...'
	with open(train_file, 'rb') as fp:
		cl = NaiveBayesClassifier(fp, format='csv')

	print "--- "+str(time.time() - start_time)+ " seconds ---"
	print 'Testing...'
	with open(test_file, 'rb') as fp_t:
		accuracy_value = cl.accuracy(fp_t, format='csv') 

	print 'Writing to file...'
	print accuracy_value

	cl.show_informative_features(5)

	print "--- "+str(time.time() - start_time)+ " seconds ---"
