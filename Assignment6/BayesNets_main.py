import getopt
import argparse
import sys

 #Jennifer Michael
 #Assignment 6: Bayes Nets
 #Due: October 23, 2015

def main():
	getArgs(sys.argv[1:])

			
def getArgs(argv):
	
	opts, args = getopt.getopt(sys.argv[1:], 'm:j:p:g')
	for opt,arg in opts, args:
		if opt[0] == '-m':
			variable = opt[1]
			
		elif opt[0] == '-j':
			variable = opt[1]

		elif opt[0] == '-p':
			variable = opt[1]
			probability = sys.argv[1]
			print(probability)

		elif opt[0] == '-g':
			variable = opt[1]



if __name__=='__main__':
	sys.exit(main())
