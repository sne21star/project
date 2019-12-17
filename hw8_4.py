import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from helper import remove_punc
from tfidf import *
import numpy as np
from collections import Counter
from heapq import nsmallest

#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words lemmatized
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    with open(doc, 'r') as file:
        words = file.read().replace('\n', ' ')
    #2. Tokenize string using nltk.tokenize.word_tokenize
    words = nltk.tokenize.word_tokenize(words)
    #3. Filter out punctuation from list of words (use remove_punc)
    words = (remove_punc(words))
    #4. Make the words lower case
    words = [i.lower() for i in words]
    #5. Filter out stopwords
    stop_words = stopwords.words('english')
    words = [w for w in words if not w in stop_words]
    #words = [''.join(remove_punc(i)) for i in words]
    #6. Lemmatize words
    lemmentizer = WordNetLemmatizer()
    words = [lemmentizer.lemmatize(i) for i in words]
    return words
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    readClean = [readAndCleanDoc(i) for i in doclist]
    wordslist = [val for sublist in readClean for val in sublist]
    wordslist = list(set(wordslist))
    wordslist.sort()
    #print(wordslist)
    #2. Use these word lists to build the doc word matrix
    w, h = [len(readClean), len(wordslist)]
    docword = np.zeros((w, h))
    i = 0
  #  print(readClean[0].index["red"])
    while i < len(readClean):
        c = Counter(readClean[i])
        k = 0
        keysC = list(c.keys())
        while k < len(keysC):
            if keysC[k] in wordslist:
                docword[i][wordslist.index(keysC[k])] = c.get(keysC[k])
            k = k + 1
        i = i + 1
    return docword, wordslist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    [row, col] = docword.shape
    i = 0
    docwordX = np.copy(docword)
    while i < row:
        sumR = sum(docwordX[i])
        sumList = list([sumR] * col)
        docwordX[i] = np.divide(docwordX[i], sumList)
        i = i + 1
    tf = docwordX
    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    [row, col] = docword.shape
    docwordX = np.copy(docword)
    sumR = np.count_nonzero(docwordX, axis = 0)
    sumR = [np.log10(row / i) for i in sumR]
    idf = [sumR]
    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    idf = buildIDFMatrix(docword)
    tf = buildTFMatrix(docword)
    tfidf = idf * tf
    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    tfidfDict = []
    [row,col] = docword.shape
    i = 0
    tfidf = buildTFIDFMatrix(docword)
    while i < row:
        tfidfDict.append([[k, z] for k, z in zip(wordlist, tfidf[i])])
        i = i + 1
    #np.argsort(tfidfDict)
    i = 0
    while i < row:
        tfidfDict[i].sort(key = lambda x: x[1], reverse = True)
        i = i + 1
    i = 0
    while i < len(doclist):
        distinctiveWords[doclist[i]] = [item[0] for item in tfidfDict[i][0:3]]
        i = i + 1
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    return distinctiveWords