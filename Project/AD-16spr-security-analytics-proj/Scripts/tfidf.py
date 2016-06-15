import nltk
import string
import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import operator

# python tfidf.py test_tr.txt test_tt.txt abc.txt 

infile = sys.argv[1]
test_file = sys.argv[2]
out_file = sys.argv[3]


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

# for subdir, dirs, files in os.walk(path):
#     for file in files:
#         file_path = subdir + os.path.sep + file
#         shakes = open(file_path, 'r')
#         text = shakes.read()
#         lowers = text.lower()
#         no_punctuation = lowers.translate(None, string.punctuation)
#         token_dict[file] = no_punctuation
  
with open(infile, 'r') as in_file: #reading the input file and creating the TFIDF vector

    for line in in_file:
        lowers = line.lower()
        no_punctuation = lowers.translate(None, string.punctuation)        
        token_dict[line] = no_punctuation

#print token_dict

#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

#print tfs
feature_names_ = tfidf.get_feature_names()
# for col in tfs.nonzero()[1]:
#             print feature_names_[col], ' - ', tfs[0, col]

#str = "During my stay at the Hilton Chicago it has been quite unpleasant. How so you might ask? Well ill tell you, the towels where scratchy and the service was terrible and by terrible I mean they werent even at the desk when I checked in. Also, When I ordered my breakfast, lunch, and dinner from room service I received the wrong order for all meals and felt a little sick after lunch. Finally, The bill was charging me for stuff I didnt want or ask for. But overall the hotel was very bad and unpleasant for me and others. I give it a half a star."


# index = 0
# with open(test_file, 'r') as tt_file:
#     index = 0
#     for line in tt_file:
#        # line = line.split(' ')
#         print line
#         response = tfidf.transform([line])
#         # print response[]
#         feature_names = tfidf.get_feature_names()
#         for col in response.nonzero()[1]:
#             print feature_names[col], '-', response[0, col]

#             index +=1
#         print "The total # of words: ", index

#printing the tf-idf vector as a dictionary
#dictionary = {}
master_list_of_words = [] # a list of list of words from each document
list_of_words = [] # list of words from each document
with open(test_file, 'r') as tt_file:
    #index = 0

    for line in tt_file:
        dictionary = {} # initializing it here gives the tf-idf value for each line/reviews from a list of reviews 
        list_of_words = [] # list of words from each document
       # line = line.split(' ')
        print line
        response = tfidf.transform([line])
        # print response[]
        feature_names = tfidf.get_feature_names()
        for col in response.nonzero()[1]:
           dictionary[str(feature_names[col])] = response[0, col]
           sorted_value = sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True)
        print dictionary
        #sorted_value = sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True) #sorting the dictionary by the tf-idf values
        print sorted_value
        #print sorted_value[1][0]
        for tuple_ in sorted_value:
            list_of_words.append(tuple_[0])
        print list_of_words    # adding the extracted most frequent words to the list.
        master_list_of_words.append(list_of_words)

    print master_list_of_words
        #print sorted_value[1][1] # accessing the elements by the tuple

#extract the top words' frequencies with the maximum tf-idf values.

print '-----------------------'  
with open(test_file, 'r') as tt_file:
    for line in tt_file:
        line = line.lower()
        no_punctuation = line.translate(None, string.punctuation)
        tokens = nltk.word_tokenize(no_punctuation)
        print tokens



#calculates the number of words in each review of the test file.
with open(test_file, 'r') as tt_file:
    for line in tt_file.readlines():
        words = len(line.split(' '))
        print words