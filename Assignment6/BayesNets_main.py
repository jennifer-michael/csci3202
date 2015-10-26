import getopt
import argparse
import sys
import BayesNode

 #Jennifer Michael
 #Assignment 6: Bayes Nets
 #Due: October 23, 2015

def main():
	getArgs(sys.argv[1:])

			
def getArgs(argv):
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'm:j:p:g')
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(2)
	
	output = None
	operation = None
	p_output = None
	val = None
	
	for o,a in opts:
		if o in ("-j"):
			operation = o
			output = a
			
		elif o == ("-m"):
			operation = o
			output = a

		elif o == ("-g"):
			operation = o
			output = a

		elif o == ("-p"):
			operation = o
			p_output = a[0]
			val = float(a[1:])
			output = a[0]
		else:
			assert False, "unhandled option"
			
	pollution_val = .9
	smoker_val = .3
	
	if(p_output == "S"):
		bn = BayesNode.create_bayesNet(pollution_val, val)
	elif(p_output == "P"):
		bn = BayesNode.create_bayesNet(val, smoker_val)
	else:
		bn = BayesNode.create_bayesNet(pollution_val, smoker_val)
		
	#call functions for math
	
	if operation == "-m":
		if output == "p":
			print(bn.nodes["Pollution"].marginal)
		elif output == "~p":
			print(1.0 - bn.nodes["Pollution"].marginal)
		elif output == "s":
			print(bn.nodes["Smoker"].marginal)
		elif output == "~s":
			print(1.0 - bn.nodes["Smoker"].marginal)
		elif output == "c":
			print(bn.nodes["Cancer"].marginal) 
		elif output == "~c":
			print(1.0 - bn.nodes["Cancer"].marginal)
		elif output == "d":
			print(bn.nodes["Dyspnoea"].marginal)
		elif output == "~d":
			(1.0 - bn.nodes["Dyspnoea"].marginal)
		elif output == "x":
			print(bn.nodes["Xray"].marginal)
		elif output == "~x":
			(1.0 - bn.nodes["Xray"].marginal)
		else:
			print("Not a valid option")
			sys.exit(2)
			
	#elif operation == "-j":
		#if output == ""
			#print()
	
	#elif operation == "-g":
		#if output == ""
		



if __name__=='__main__':
	sys.exit(main())
