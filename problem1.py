import sys
from hw8_1 import *

def main(datapath):
	dictNgrams = getDict(datapath)
	return dictNgrams

if __name__ == '__main__':
	#Must change Configurations
	datapath = sys.argv[1]
	dictNgrams = main(datapath)
	print(dictNgrams[0:10])