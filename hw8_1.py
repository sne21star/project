from nltk import ngrams
from collections import Counter
import operator
#Arguments:
#  filename: name of file to read in
#Returns: a list of strings, each string is one line in the file
#hints: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#       https://docs.python.org/3/library/stdtypes.html#str.splitlines
def getText(filename) :
	#myFile = open(filename)
	with open(filename) as f:
		data = f.readlines()
	f.close()
	strLine = [x.strip() for x in data]
	return strLine

#Arguments:
#  line: a string of text
#Returns: a list of n-grams
#Notes: make sure to pad the beginning and end of the string with '_'
#       make sure to convert the string to lower-case
#       so "Hello" should be turned into "__hello__" before processing
def getNgrams(line) :
	line = [x.lower() for x in line]
	line = [x.ljust(len(x) + 1,' ') for x in line]
	line = [x.rjust(len(x) + 1,' ') for x in line]
	i = 0
	wordNGrams = []
	listNgrams = []
	while i < len(line):
		word = ngrams(line[i], 3)
		wordNGrams.append(word)
		i = i + 1
	while i > 0:
		i = i - 1
		for grams in wordNGrams[i]:
			#print(grams)
			listNgrams.append(grams)
	return listNgrams
    
#Arguments:
#  filename: the filename to create an n-gram dictionary for
#Returns: a dictionary, with ngrams as keys, and frequency of that ngram as the value.
#Notes: Remember that getText gives you a list of lines, and you want the ngrams from
#       all the lines put together.
#       use 'map', use getText, and use getNgrams
#Hint: dict.fromkeys(l, 0) will initialize a dictionary with the keys in list l and an
#      initial value of 0
def getDict(filename) :
	strLine = getText(filename)
	line = getNgrams(strLine)
	listRange = range(0,len(line))
	K = []
	for i in line:
		 K.append(str(i[0]) + str(i[1]) + str(i[2]))
	dictNgrams = dict.fromkeys(K, 0)
	for i in strLine:
		i = [char for char in i]
		k = len(i)
		indexBegin = 0
		indexEnd = indexBegin+2
		#print(i)
		while indexEnd < k:
			word = str(i[indexBegin]) + str(i[indexBegin + 1]) + str(i[indexEnd])
			dictNgrams[word] = dictNgrams.get(word, 0)+1
			indexBegin = indexBegin + 1
			indexEnd = indexEnd + 1
	sorted_dictNgrams = sorted(dictNgrams.items(), key=operator.itemgetter(1), reverse= True)
	returnList = sorted_dictNgrams
	#for x in list(sorted_dictNgrams)[len(sorted_dictNgrams)-10:len(sorted_dictNgrams)]:
	#	returnList.insert(0,x)
	return returnList