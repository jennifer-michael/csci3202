import BayesNode

'''
Where all the calculations will be done.
'''
results = {}

''' 3 marginals '''
#def marginal_cancer(cancerNode, pollutionNode, smokerNode):
	#firstOp = cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"]
	#secondOp = cancerNode.probabilities["~P~S"] * (1.0 - pollutionNode.probabities["L"]) * (1.0 - smokerNode.probabilities["T"])
	#thirdOp = cancerNode.probabilities["PS"] * pollutionNode.probabities["L"] * smokerNode.probabilities["T"]
	#fourthOp = cancerNode.probabilities["P~S"] * pollutionNode.probabities["L"] * (1.0 - smokerNode.probabilities["T"])
	 
	#probOfCancer = firstOp + secondOp + thirdOp + fourthOp
	
	#cancerNode.marginal = probOfCancer
	#results["marg_c"] = probOfCancer
	
	#return probOfCancer

##is this the marginal probability of an xray?
#def marginal_xRay(cancerNode, xrayNode):
	#if "marg_c" not in results:
		#c = marginalCancer(cancerNode, pollutionNode, smokerNode)
	#else:
		#c = results["marg_c"]
		
	#firstOp = xrayNode.probabilities["C"] * c
	#secondOp = xrayNode.probabilities["~C"] * (1.0 - c)
	
	#probXrayTrue = firstOp + secondOp
	
	#xrayNode.foundValues["X"] = probXrayTrue
	#xrayNode.marginal = probXrayIsTrue
	#return probXrayTrue

#def marginal_dyspnoea(cancerNode, dyspnoeaNode):
	#if "marg_c" not in results:
		#c = marginalCancer(cancerNode, pollutionNode, smokerNode)
	#else:
		#c = results["marg_c"]
		
	#firstOp = dyspnoeaNode.probabilities["C"] * c
	#secondOp = dyspnoeaNode.probabilties["~C"] * (1.0 - c)
	
	#probDysIsTrue = firstOp + secondOp
	
	#dyspnoeaNode.marginal = probDysIsTrue
	#results["d"] = probDysIsTrue
	#return probDysIsTrue
	
'''Joints'''
def jointXSCP(cancerNode, xrayNode, pollutionNode, smokerNode):
	firstOp = xrayNode.probabilities["C"] * cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] * (1.0 - pollutionNode.probabilities["L"])
				
	secondOp = xrayNode.probabilities["C"] * cancerNode.probabilities["PS"] * smokerNode.probabilities["T"] * pollutionNode.probabilities["L"]
				
	thirdOp = xrayNode.probabilities["~C"] * cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] * (1.0 - pollutionNode.probabilities["L"])
				
	fourthOp = xrayNode.probabilities["~C"] * cancerNode.probabilities["PS"] * smokerNode.probabilities["T"] * pollutionNode.probabilities["L"]
				
	joint_xscp = firstOp + secondOp + thirdOp + fourthOp
	
	return joint_xscp

def jointDSCP(cancerNode, dyspnoeaNode, pollutionNode, smokerNode):
	firstOp = dyspnoeaNode.probabilities["C"] * cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] * (1.0 - pollutionNode.probabilities["L"])
				
	secondOp = dyspnoeaNode.probabilities["C"] * cancerNode.probabilities["PS"] * smokerNode.probabilities["T"] * pollutionNode.probabilities["L"]
				
	thirdOp = dyspnoeaNode.probabilities["~C"] * cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] *(1.0 - pollutionNode.probabilities["L"])
				
	fourthOp = dyspnoeaNode.probabilities["~C"] * cancerNode.probabilities["PS"] * smokerNode.probabilities["T"] * pollutionNode.probabilities["L"]
				
	joint_dscp = firstOp + secondOp + thirdOp + fourthOp
	
	return joint_dscp
	
def jointSCP(cancerNode, pollutionNode, smokerNode):
	#firstOp = cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"]
	
	#secondOp = cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]
				
	#thirdOp = (1.0 - cancerNode.probabilities["~PS"]) * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"]
				
	#fourthOp = (1.0 - cancerNode.probabilities["PS"]) * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]
				
	#joint_scp = firstOp + secondOp + thirdOp + fourthOp
	
	sGc = probSmokerGivenCancer(cancerNode, pollutionNode, smokerNode)
	joint_scp = sGc * cancerNode.marginal * pollutionNode.probabilities["L"]
	return joint_scp
	
#def jointPCS(cancerNode, pollutionNode, smokerNode):
	
	
#def jointCP(cancerNode, pollutionNode, smokerNode):
	#firstOp = cancerNode.probabilities["~PS"] *
				#smokerNode.probabilities["T"] *
				#(1.0 - pollutionNode.probabilities["L"])
				
	#secondOp = cancerNode.probabilities["PS"] *
				#smokerNode.probabilities["T"] *
				#pollutionNode.probabilities["L"]
				
	#joint_cp = firstOp + secondOp
	
	#return joint_cp
				
'''Conditionals'''
def probCancerGivenSmoker(cancerNode, pollutionNode, smokerNode):
	cGivenSNum = cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"] + cancerNode.probabilities["~PS"] * (1.0-pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"]
	
	cGivenS = cGivenSNum / smokerNode.probabilities["T"]
	results["cGivenS"] = cGivenS
	
	return cGivenS	
	
def probSmokerGivenCancer(cancerNode, pollutionNode, smokerNode):	

	cGivenS = probCancerGivenSmoker(cancerNode, pollutionNode, smokerNode)
	c = cancerNode.marginal
	
	sGivenCancer = (cGivenS * smokerNode.probabilities["T"])/c
	return sGivenCancer
	
def probXrayGivenSmoker(cancerNode, xrayNode, pollutionNode, smokerNode):
	numerator = jointXSCP(cancerNode, xrayNode, pollutionNode, smokerNode)
	denom = jointSCP(cancerNode, pollutionNode, smokerNode)
	
	xGs = numerator/smokerNode.probabilities["T"]
	
	return xGs
		
	
def probDyspnoeaGivenSmoker(cancerNode, xrayNode, pollutionNode, smokerNode):
	numerator = jointDSCP(cancerNode, xrayNode, pollutionNode, smokerNode)
	denom = jointSCP(cancerNode, pollutionNode, smokerNode)
	
	dGs = numerator/denom
	
	return dGs
	
def probCancerGivenPollution(cancerNode, xrayNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"] 
				
	secondOp = cancerNode.probabilities["~P~S"] * (1.0-pollutionNode.probabilities["L"]) * (1.0 - smokerNode.probabilities["T"])
	
	cGivenp = (firstOp + secondOp) / (1.0 - pollutionNode.probabilities["L"])
	#results["cGivenp"] = cGivenp

	return cGivenp	
	
def probPollutionGivenCancer(cancerNode, xrayNode, pollutionNode, smokerNode):
	
	cGp = probCancerGivenPollution(cancerNode, xrayNode, pollutionNode, smokerNode)
	numerator = cGp * (1.0 - pollutionNode.probabilities["L"])
	
	pGc = numerator / cancerNode.marginal
	
	results["pGivenc"] = pGc
	return pGc
	
def probXrayGivenDys(cancerNode, xrayNode, dyspnoeaNode):
	#prob(x|c)*P(c)*P(d|c) + P(x|~c)*P(~c)*P(d|~c) / P(d)
	
	firstOp = xrayNode.probabilities["C"] * cancerNode.marginal * dyspnoeaNode.probabilities["C"]
	secondOp = xrayNode.probabilities["~C"] * (1.0 - cancerNode.marginal) * dyspnoeaNode.probabilities["~C"]
	denom = dyspnoeaNode.marginal
	
	xGivend = (firstOp + secondOp) / denom
	
	return xGivend
def probCancerGivenDysAndSmoker(cancerNode, pollutionNode, smokerNode, dyspnoeaNode):
	firstNum = dyspnoeaNode.probabilities["C"] * cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]
	secondNum = dyspnoeaNode.probabilities["C"] * cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"]
	
	firstDen = dyspnoeaNode.probabilities["C"] * cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]
	secondDen = dyspnoeaNode.probabilities["C"] * cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"]
	thirdDen = dyspnoeaNode.probabilities["~C"] * (1-cancerNode.probabilities["PS"]) * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]
	fourthDen = dyspnoeaNode.probabilities["~C"] * (1-cancerNode.probabilities["~PS"]) * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"]
	
	
	numerator = firstNum + secondNum
	denom = firstDen + secondDen + thirdDen + fourthDen
	cGivends = numerator/denom
	
	return cGivends

def probDyspnoeaGivenPollution(cancerNode, pollutionNode, smokerNode, dyspnoeaNode):
	firstNum = dyspnoeaNode.probabilites["C"] * cancerNode.probabilities["~PS"] * smokerNode.probabilites["T"] * pollutionNode["H"]
	secondNum = dyspnoeaNode.probabilites["C"] * cancerNode.probabilites["~P~S"] * smokerNode.probabilities["F"] * pollutionNode["H"]
	thirdNum = dyspnoeaNode.probabilities["~C"] * cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] * pollutionNode["H"]
	fouthNum = dyspnoeaNode.probabilities["~C"] * cancerNode.probabilities["~P~S"] * smokerNode.probabilities["F"] * pollutionNode["H"]
	
	firstDen = cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] * pollutionNode.probabilities["H"]
	secondDen = cancerNode.probabilities["~P~S"] * smokerNode.probabilities["F"] * pollutionNode.probabilities["H"]
	thirdDen = (1.0 - cancerNode.probabilites["~PS"]) * smokerNode.probabilites["T"] * pollutionNode.probabilities["H"]
	fourthDen = (1.0 - cancerNode.probabilities["~P~C"]) * smokerNode.probabilities["F"] * pollutionNode.probabilities["H"]
	
	numerator = firstNum + secondNum + thirdNum + fourthNum
	denom = firstDen + secondDen + thirdDen + fourthDen
	
	dGivenp = numerator/denom
	
	return dGivenp
	
def probPollutionGivenDys(cancerNode, pollutionNode, smokerNode, dyspnoeaNode):
	x = probDyspnoeaGivenPollution(cancerNode, pollutionNode, smokerNode, dyspnoeaNode)
	
	pGivend = (x * dyspnoeaNode.marginal) / pollutionNode.probabilites["H"]
	
	return pGivend
	
def probSmokerGivenDyspnoea(cancerNode, pollutionNode, smokerNode, dyspnoeaNode):
	x = probDyspnoeaGivenSmoker(cancerNode, xrayNode, pollutionNode, smokerNode)
	
	sGivend = (x * dyspnoeaNode.marginal) / smokerNode.probabilities["T"]
	
	return sGivend
	
def probCancerGivenDyspnoea(cancerNode, dyspnoeaNode):
	cGivend = (dyspnoeaNode["C"] * cancerNode.marginal) / dyspnoeaNode.marginal
	
	return cGivend
	
#def probPollutionGivenCancerAndSmoker(cancerNode, xrayNode, pollutionNode, smokerNode):
	#numerator = jointPCS(cancerNode, pollutionNode, smokerNode)
	#denom = jointSC(cancerNode, pollutionNode, smokerNode)
	
	#pGivencs = numerator / denom
	
	#results["pGivencs"] = pGivencs
	
	#return pGivencs
	
