import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from hw8_4 import *
import sys
from nltk.stem import WordNetLemmatizer

def main(datapath):

	print("*** Testing readAndCleanDoc ***")
	print(readAndCleanDoc('lecs/1_vidText.txt')[0:5])

	doclist = ['lecs/1_vidText.txt', 'lecs/2_vidText.txt']
	print("*** Testing buildDocWordMatrix ***")
	docword, wordlist = buildDocWordMatrix(doclist)
	print(docword.shape)
	print(len(wordlist))
	print(docword[0][0:10])
	print(wordlist[0:10])
	print(docword[1][0:10])

	print("*** Testing buildTFMatrix ***")
	tf = buildTFMatrix(docword)
	print(tf[0][0:10])
	print(tf[1][0:10])
	print(tf.sum(axis=1))

	print("*** Testing buildIDFMatrix ***")
	idf = buildIDFMatrix(docword)
	print(idf[0][0:10])

	print("*** Testing buildTFIDFMatrix ***")
	tfidf = buildTFIDFMatrix(docword)
	print(tfidf.shape)
	print(tfidf[0][0:10])
	print(tfidf[1][0:10])

	print("*** Testing findDistinctiveWords ***")
	print(findDistinctiveWords(docword, wordlist, doclist))

	return 0

if __name__ == '__main__':
	#Must change Configurations
	datapath = []
	datapath = [sys.argv[i] for i in range(1,len(sys.argv))]
	#print(datapath)
	dictNgrams = main(datapath)

