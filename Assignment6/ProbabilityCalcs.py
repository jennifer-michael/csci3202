import BayesNode.py

'''
Where all the calculations will be done.
'''
results = {}

''' 3 marginals '''
def marginal_cancer(cancerNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"])
	secondOp = cancerNode.probabilities["~P~S"] * (1.0 - pollutionNode.probabities["L"]) * (1.0 - smokerNode.probabilities["T"])
	thirdOp = cancerNode.probabilities["PS"] * pollutionNode.probabities["L"] * smokerNode.probabilities["T"]
	fourthOp = cancerNode.probabilities["P~S"] * pollutionNode.probabities["L"] * (1.0 - smokerNode.probabilities["T"])
	 
	probOfCancer = firstOp + secondOp + thirdOp + fourthOp
	
	cancerNode.marginal = probOfCancer
	results["marg_c"] = probOfCancer
	
	return probOfCancer

#is this the marginal probability of an xray?
def marginal_xRay(cancerNode, xrayNode):
	if "marg_c" not in results:
		c = marginalCancer(cancerNode, pollutionNode, smokerNode)
	else:
		c = results["marg_c"]
		
	firstOp = xrayNode.probabilities["C"] * c
	secondOp = xrayNode.probabilities["~C"] * (1.0 - c)
	
	probXrayTrue = firstOp + secondOp
	
	xrayNode.foundValues["X"] = probXrayTrue
	xrayNode.marginal = probXrayIsTrue
	return probXrayTrue

def marginal_dyspnoea(cancerNode, dyspnoeaNode):
	if "marg_c" not in results:
		c = marginalCancer(cancerNode, pollutionNode, smokerNode)
	else:
		c = results["marg_c"]
		
	firstOp = dyspnoeaNode.probabilities["C"] * c
	secondOp = dyspnoeaNode.probabilties["~C"] * (1.0 - c)
	
	probDysIsTrue = firstOp + secondOp
	
	dyspnoeaNode.marginal = probDysIsTrue
	results["d"] = probDysIsTrue
	return probDysIsTrue
	
'''Joints'''
def jointXSCP(cancerNode, xrayNode, pollutionNode, smokerNode):
	firstOp = xrayNode.probabilites["C"] * 
				cancerNode.probabilities["~PS"] * 
				smokerNode.probabilites["T"] * 
				(1.0 - pollutionNode.probabilites["L"])
				
	secondOp = xrayNode.probabilities["C"] *
				cancerNode.probabilites["PS"] *
				smokerNode.probabilities["T"] *
				pollutionNode.probabilities["L"]
				
	thirdOp = xrayNode.probabilities["~C"] *
				cancerNode.probabilites["~PS"] *
				smokerNode.probabilities["T"] *
				(1.0 - pollutionNode.probabilites["L"])
				
	fourthOp = xrayNode.probabilities["~C"] *
				cancerNode.probabilites["PS"] *
				smokerNode.probabilities["T"] *
				pollutionNode.probabilities["L"]
				
	joint_xscp = firstOp + secondOp + thirdOp + fourthOp
	
	return joint_xscp

def jointDSCP(cancerNode, dyspnoeaNode, pollutionNode, smokerNode):
	firstOp = dyspnoeaNode.probabilites["C"] * 
				cancerNode.probabilities["~PS"] * 
				smokerNode.probabilites["T"] * 
				(1.0 - pollutionNode.probabilites["L"])
				
	secondOp = dyspnoeaNode.probabilities["C"] *
				cancerNode.probabilites["PS"] *
				smokerNode.probabilities["T"] *
				pollutionNode.probabilities["L"]
				
	thirdOp = dyspnoeaNode.probabilities["~C"] *
				cancerNode.probabilites["~PS"] *
				smokerNode.probabilities["T"] *
				(1.0 - pollutionNode.probabilites["L"])
				
	fourthOp = dyspnoeaNode.probabilities["~C"] *
				cancerNode.probabilites["PS"] *
				smokerNode.probabilities["T"] *
				pollutionNode.probabilities["L"]
				
	joint_dscp = firstOp + secondOp + thirdOp + fourthOp
	
	return joint_dscp
	
def jointSCP(cancerNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilities["~PS"] *
				(1.0 - pollutionNode.probabilites["L"]) *
				smokerNode.probabilites["T"]
	
	secondOp = cancerNode.probabilities["PS"] *
				pollutionNode.probabilites["L"] *
				smokerNode.probabilites["T"]
				
	thirdOp = (1.0 - cancerNode.probabilities["~PS"]) *
				(1.0 - pollutionNode.probabilites["L"]) *
				smokerNode.probabilites["T"]
				
	fourthOp = (1.0 - cancerNode.probabilities["PS"] *
				pollutionNode.probabilites["L"] *
				smokerNode.probabilites["T"]
				
	joint_scp = firstOp + secondOp + thirdOp + fourthOp
	
	return joint_scp
	
def jointPCS(cancerNode, pollutionNode, smokerNode):
	
	
def jointCP(cancerNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilites["~PS"] *
				smokerNode.probabilites["T"] *
				(1.0 - pollutionNode.probabilites["L"])
				
	secondOp = cancerNode.probabilites["PS"] *
				smokerNode.probabilites["T"] *
				pollutionNode.probabilites["L"]
				
	joint_cp = firstOp + secondOp
	
	return joint_cp
				
'''Conditionals'''
def probCancerGivenSmoker(cancerNode, pollutionNode, smokerNode):
	#your ~'s may be wrong with the cancerNode stuff
	cGivenSNum = cancerNode.probabilities["PS"] * pollutionNode.probabilties["L"] * smokerNode.probabilities["T"] 
				+ cancerNode.probabilities["~PS"] * (1.0-pollutionNode.probabilites["L"]) * smokerNode.probabilites["T"]
	
	cGivenS = cGivenSNum / smokerNode.probabilities["T"]
	results["cGivenS"] = cGivenS
	
	return cGivenS	
	
def probSmokerGivenCancer(cancerNode, smokerNode):	
	if "cGivenS" not in results:
		cGivenS = probCancerGivenSmoker(cancerNode, pollutionNode, smokerNode)
	else:
		cGivenS = results["cGivenS"]
	if "c" not in results:
		c = marginalCancer(cancerNode, pollutionNode, smokerNode)
	else:
		c = cancerNode.marginal
	
	sGivenCancer = (cGivenS * smokerNode.probabilites["T"])/c
	results[sGivenC] = sGivenCancer
	print(sGivenCancer)
	
def probXrayGivenSmoker():
	numerator = jointXSCP(cancerNode, xrayNode, pollutionNode, smokerNode)
	denom = jointSCP(cancerNode, pollutionNode, smokerNode)
	
	xGs = numerator/denom
	
	return xGs

def probDyspnoeaGivenSmoker(cancerNode, xrayNode, pollutionNode, smokerNode):
	numerator = jointDSCP(cancerNode, xrayNode, pollutionNode, smokerNode)
	denom = jointSCP(cancerNode, pollutionNode, smokerNode)
	
	dGs = numerator/denom
	
	return dGs
	
def probCancerGivenPollution(cancerNode, xrayNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilities["~PS"] * 
				pollutionNode.probabilties["L"] * 
				smokerNode.probabilities["T"] 
	secondOp = cancerNode.probabilities["~P~S"] * 
				(1.0-pollutionNode.probabilites["L"]) * 
				smokerNode.probabilites["F"]
	
	cGivenp = (firstOp + secondOp) / pollutionNode.probabilites["L"]
	results["cGivenp"] = cGivenp
	
	return cGivenp	
	
def probPollutionGivenCancer(cancerNode, xrayNode, pollutionNode, smokerNode):
	
	cGp = results["cGivenp"]
	numerator = cGp * (1.0 - pollutionNode.probabilities["L"])
	
	pGc = numerator / results["marg_c"]
	
	results["pGivenc"] = pGc
	return pGc
	
#def probPollutionGivenCancerAndSmoker(cancerNode, xrayNode, pollutionNode, smokerNode):
	#numerator = jointPCS(cancerNode, pollutionNode, smokerNode)
	#denom = jointSC(cancerNode, pollutionNode, smokerNode)
	
	#pGivencs = numerator / denom
	
	#results["pGivencs"] = pGivencs
	
	#return pGivencs
	
