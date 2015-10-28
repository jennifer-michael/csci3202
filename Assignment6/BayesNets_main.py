import getopt
import argparse
import sys
import BayesNode
import ProbabilityCalcs

 #Jennifer Michael
 #Assignment 6: Bayes Nets
 #Due: October 23, 2015
 #Worked with Brooke Robinson and Mario Alanis
 
 ########################################
 #           Bayes Nets! 				#
 ########################################

def main():
	getArgs(sys.argv[1:])

			
def getArgs(argv):
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'm:j:p:g:')
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
			print(1.0 - bn.nodes["Dyspnoea"].marginal)
		elif output == "x":
			print(bn.nodes["XRay"].marginal)
		elif output == "~x":
			print(1.0 - bn.nodes["XRay"].marginal)
		else:
			print("Not a valid option")
			sys.exit(2)
			
	#elif operation == "-j":
		#if output == "PSC":
			#print()
		#elif output == "psc":
			#print()
		#elif output == "~p~s~c":
			#print()
		
		#extras
		
	
	if operation == "-g":
		if output == "p|c":
			x = ProbabilityCalcs.probPollutionGivenCancer(bn.nodes["Cancer"], 
														  bn.nodes["XRay"], 
														  bn.nodes["Pollution"], 
														  bn.nodes["Smoker"])
			print(x)
			
		elif output == "c|p":
			x = ProbabilityCalcs.probCancerGivenPollution(bn.nodes["Cancer"], 
														  bn.nodes["XRay"], 
														  bn.nodes["Pollution"], 
														  bn.nodes["Smoker"])
			print(x)
		
		#this one is wrong until i can get joint things working
		elif output == "d|s":
			x = ProbabilityCalcs.probDyspnoeaGivenSmoker(bn.nodes["Cancer"], 
														  bn.nodes["XRay"], 
														  bn.nodes["Pollution"], 
														  bn.nodes["Smoker"])
			print(x)
		
		elif output == "c|s":
			x = ProbabilityCalcs.probCancerGivenSmoker(bn.nodes["Cancer"], 
														  bn.nodes["Pollution"], 
														  bn.nodes["Smoker"])
			print(x)
		
		elif output == "s|c":
			x = ProbabilityCalcs.probSmokerGivenCancer(bn.nodes["Cancer"],
															bn.nodes["Pollution"],
															bn.nodes["Smoker"])
			print(x)
		
		#this one is also wrong because of joint crap
		elif output == "x|s":
			x = ProbabilityCalcs.probXrayGivenSmoker(bn.nodes["Cancer"], 
														  bn.nodes["XRay"], 
														  bn.nodes["Pollution"], 
														  bn.nodes["Smoker"])
			print(x)
		
		#wrong	
		elif output == "d|s":
			x = ProbabilityCalcs.probDyspnoeaGivenSmoker(bn.nodes["Cancer"], 
															bn.nodes["XRay"], 
															bn.nodes["Pollution"], 
															bn.nodes["Smoker"])
															
			print(x)
		#didn't have to do	
		elif output == "c|p":
			x = ProbabilityCalcs.probCancerGivenPollution(bn.nodes["Cancer"], 
															bn.nodes["XRay"], 
															bn.nodes["Pollution"], 
															bn.nodes["Smoker"])
			print(x)
			
		#works
		elif output == "p|c":
			x = ProbabilityCalcs.probPollutionGivenCancer(bn.nodes["Cancer"], 
															bn.nodes["XRay"], 
															bn.nodes["Pollution"], 
															bn.nodes["Smoker"])
															
			print(x)
		
		#works!	
		elif output == "x|d":
			x = ProbabilityCalcs.probXrayGivenDys(bn.nodes["Cancer"], 
													bn.nodes["XRay"], 
													bn.nodes["Dyspnoea"]) 
													
			print(x)
		
		#IT WORKS	
		elif output == "c|ds":
			x = ProbabilityCalcs.probCancerGivenDysAndSmoker(bn.nodes["Cancer"], 
													bn.nodes["Pollution"], 
													bn.nodes["Smoker"],
													bn.nodes["Dyspnoea"]) 
			print(x)
		#you left off testing here jenny!!!!!!	
		elif output == "d|p":
			x = ProbabilityCalcs.probDyspnoeaGivenPollution(bn.nodes["Cancer"], 
													bn.nodes["Pollution"], 
													bn.nodes["Smoker"],
													bn.nodes["Dyspnoea"]) 
			print(x)
			
		elif output == "p|d":
			x = ProbabilityCalcs.probPollutionGivenDys(bn.nodes["Cancer"], 
													bn.nodes["Pollution"], 
													bn.nodes["Smoker"],
													bn.nodes["Dyspnoea"])
													
			print(x)
			
		elif output == "s|d":
			x = ProbabilityCalcs.probSmokerGivenDyspnoea(bn.nodes["Cancer"], 
													bn.nodes["Pollution"], 
													bn.nodes["Smoker"],
													bn.nodes["Dyspnoea"])
			print(x)
			
		elif output == "c|d":
			x = ProbabilityCalcs.probCancerGivenDyspnoea(bn.nodes["Cancer"], bn.nodes["Dyspnoea"])
			print(x)
			
																		
		



if __name__=='__main__':
	sys.exit(main())
