import sys

from matplotlib import cm

from hw8_1 import *
from helper import *

def main(datapath, lengthD):
	i = 0
	listdictNgrams = []
	while i < lengthD:
		listdictNgrams.append(sorted((getDict(datapath[i]))))
		i = i + 1
	return listdictNgrams

if __name__ == '__main__':
	#Must change Configurations
	i = 1
	datapath = []
	while i < 8:
		datapath.append(sys.argv[i])
		i = i + 1
	lengthD = len(datapath)
	dictNgrams = main(datapath, lengthD)
	for x in dictNgrams:
		print(x[0:10])
	i = 0
	listName = ["english.png", "french.png", "german.png", "italian.png", "portuguese.png", "spanish.png", "mystery.png"]
	i = 0
	while i < lengthD:
		k = 0
		listK = []
		while k < len(dictNgrams[i]):
			listK.append(dictNgrams[i][k][1])
			k = k + 1
		plotHisto(listK, listName[i], minrange=0.0, maxrange=100.0, plotinline=False)
		i = i + 1
