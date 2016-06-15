import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
#this is a code which prints the frequency of words in a document.

w_list = ['mary', 'little', 'lamb', 'school', 'doe']
string_text = "Mary had a little lamb. Mary goes to school. Lamb does not go to school."


lower_case = string_text.lower()
string_line = lower_case.translate(None, string.punctuation)
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


new_list = tokenize(str(string_line))
print new_list

# cv = CountVectorizer(vocabulary = w_list)
# #print cv
# array_list = cv.fit_transform(new_list).toarray()
# print array_list
# for list_ in array_list:
# 	print list_
# 	#for value in list_:
# 	mydict = {key:value for key, value in zip(w_list,list_)}
# print mydict

itemcounter = {item:count for item, count in [(item, new_list.count(item)) for item in w_list]}
final_counts = [(item, count) for item, count in itemcounter.iteritems()]
print final_counts

sentences = nltk.sent_tokenize(string_text)
print sentences
sentences = [nltk.word_tokenize(sent) for sent in sentences]

sentences = [nltk.pos_tag(sent) for sent in sentences]

print sentences
#output:

