import BayesNode

'''
Where all the calculations will be done.
'''

'''Joints
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
	
def jointSCP(cancerNode, pollutionNode, smokerNode, xrayNode):

	sGc = probSmokerGivenCancer(cancerNode, pollutionNode, smokerNode)
	cGp = probCancerGivenPollution(cancerNode, xrayNode, pollutionNode, smokerNode)
	
	joint_scp = sGc * cGp * pollutionNode.probabilities["L"]
	return joint_scp
	
def jointDSCP(cancerNode, pollutionNode, smokerNode, dNode):
	dGc = probDyspnoeaGivenCancer(cancerNode, pollutionNode, smokerNode, dNode)
	sGcp = probSmokerGivenCancerandPollution(cancerNode, pollutionNode, smokerNode, dNode)
	cGp = probCancerGivenPollutionLow(cancerNode, xrayNode, pollutionNode, smokerNode)
	
	numerator = dGc * cancerNode.probabilities["PS"] * smokerNode.marginal * pollutionNode.marginal * sGcp * cGp * pollutionNode.marginal
	
	denom = probSmokerGivenCancerandPollution(cancerNode, pollutionNode, smokerNode, dNode)
	
	j_DSCP = numerator/denom
	
	return j_DSCP
	
'''

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
	firstNum = xrayNode.probabilities["C"] * (cancerNode.probabilities["PS"]*smokerNode.probabilities["T"] * pollutionNode.probabilities["L"])
	secondNum = xrayNode.probabilities["C"] * (cancerNode.probabilities["~PS"]*smokerNode.probabilities["T"]* (1.0 - pollutionNode.probabilities["L"]))
	thirdNum = xrayNode.probabilities["~C"] * ((1.0 - cancerNode.probabilities["PS"])*smokerNode.probabilities["T"]*pollutionNode.probabilities["L"])
	fourthNum = xrayNode.probabilities["~C"] * ((1.0 - cancerNode.probabilities["~PS"])*smokerNode.probabilities["T"]*(1.0 - pollutionNode.probabilities["L"]))
	
	firstDenom = cancerNode.probabilities["PS"]*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	secondDenom = cancerNode.probabilities["~PS"]*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	thirdDenom = (1-cancerNode.probabilities["PS"])*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	fourthDenom = (1-cancerNode.probabilities["~PS"])*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	
	numerator = firstNum + secondNum + thirdNum + fourthNum
	denom = firstDenom + secondDenom + thirdDenom + fourthDenom

	
	xGs = numerator/denom
	
	return xGs
		
	
def probDyspnoeaGivenSmoker(cancerNode, xrayNode, pollutionNode, smokerNode, dNode):
	
	firstNum = dNode.probabilities["C"] * (cancerNode.probabilities["PS"]*smokerNode.probabilities["T"] * pollutionNode.probabilities["L"])
	secondNum = dNode.probabilities["C"] * (cancerNode.probabilities["~PS"]*smokerNode.probabilities["T"]* (1.0 - pollutionNode.probabilities["L"]))
	thirdNum = dNode.probabilities["~C"] * ((1.0 - cancerNode.probabilities["PS"])*smokerNode.probabilities["T"]*pollutionNode.probabilities["L"])
	fourthNum = dNode.probabilities["~C"] * ((1.0 - cancerNode.probabilities["~PS"])*smokerNode.probabilities["T"]*(1.0 - pollutionNode.probabilities["L"]))
	
	firstDenom = cancerNode.probabilities["PS"]*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	secondDenom = cancerNode.probabilities["~PS"]*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	thirdDenom = (1-cancerNode.probabilities["PS"])*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	fourthDenom = (1-cancerNode.probabilities["~PS"])*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	
	numerator = firstNum + secondNum + thirdNum + fourthNum
	denom = firstDenom + secondDenom + thirdDenom + fourthDenom

	
	dGs = numerator/denom
	
	return dGs
	
def probCancerGivenPollutionHigh(cancerNode, xrayNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"] 
				
	secondOp = cancerNode.probabilities["~P~S"] * (1.0-pollutionNode.probabilities["L"]) * (1.0 - smokerNode.probabilities["T"])
	
	cGivenp = (firstOp + secondOp) / (1.0 - pollutionNode.probabilities["L"])

	return cGivenp	
	
def probCancerGivenPollutionLow(cancerNode, xrayNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"] 
				
	secondOp = cancerNode.probabilities["P~S"] * pollutionNode.probabilities["L"] * (1.0 - smokerNode.probabilities["T"])
	
	cGivenpl = (firstOp + secondOp) / pollutionNode.probabilities["L"]

	return cGivenpl	
	
def probPollutionGivenCancer(cancerNode, xrayNode, pollutionNode, smokerNode):
	
	cGp = probCancerGivenPollution(cancerNode, xrayNode, pollutionNode, smokerNode)
	numerator = cGp * (1.0 - pollutionNode.probabilities["L"])
	
	pGc = numerator / cancerNode.marginal
	
	results["pGivenc"] = pGc
	return pGc
	
def probXrayGivenDys(cancerNode, xrayNode, dyspnoeaNode):
	
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

def probDyspnoeaGivenPollution(cancerNode, pollutionNode, smokerNode, dNode):
	firstNum = dNode.probabilities["C"] * (cancerNode.probabilities["~PS"]*smokerNode.probabilities["T"] * (1.0 - pollutionNode.probabilities["L"]))
	secondNum = dNode.probabilities["C"] * (cancerNode.probabilities["~P~S"]*(1.0 - smokerNode.probabilities["T"])* (1.0 - pollutionNode.probabilities["L"]))
	thirdNum = dNode.probabilities["~C"] * ((1.0 - cancerNode.probabilities["~PS"])*smokerNode.probabilities["T"]*(1.0 - pollutionNode.probabilities["L"]))
	fourthNum = dNode.probabilities["~C"] * ((1.0 - cancerNode.probabilities["~P~S"])*(1.0 - smokerNode.probabilities["T"])* (1.0 - pollutionNode.probabilities["L"]))
	
	firstDenom = cancerNode.probabilities["~PS"]* (1.0 - pollutionNode.probabilities["L"]) *smokerNode.probabilities["T"]
	secondDenom = cancerNode.probabilities["~P~S"]*(1.0 - pollutionNode.probabilities["L"])* (1.0 - smokerNode.probabilities["T"])
	thirdDenom = (1.0 -cancerNode.probabilities["~PS"])* (1.0 - pollutionNode.probabilities["L"]) *smokerNode.probabilities["T"]
	fourthDenom = (1.0 -cancerNode.probabilities["~P~S"])*(1.0 - pollutionNode.probabilities["L"])* (1.0 - smokerNode.probabilities["T"])
	
	numerator = firstNum + secondNum + thirdNum + fourthNum
	denom = firstDenom + secondDenom + thirdDenom + fourthDenom

	
	dGp = numerator/denom
	
	return dGp
	
def probPollutionGivenDys(cancerNode, pollutionNode, smokerNode, dyspnoeaNode):
	x = probDyspnoeaGivenPollution(cancerNode, pollutionNode, smokerNode, dyspnoeaNode)
	
	pGivend = (x * (1.0 -pollutionNode.probabilities["L"])) / dyspnoeaNode.marginal
	
	return pGivend
	
def probSmokerGivenDyspnoea(cancerNode, xrayNode, pollutionNode, smokerNode, dyspnoeaNode):
	x = probDyspnoeaGivenSmoker(cancerNode, xrayNode, pollutionNode, smokerNode, dyspnoeaNode)
	
	sGivend = (x * smokerNode.probabilities["T"]) / dyspnoeaNode.marginal
	
	return sGivend
	
def probCancerGivenDyspnoea(cancerNode, dyspnoeaNode):
	cGivend = (dyspnoeaNode.probabilities["C"] * cancerNode.marginal) / dyspnoeaNode.marginal
	
	return cGivend
	
def probDyspnoeaGivenCancer(cancerNode, pollutionNode, smokerNode, dNode):
	cGd = probCancerGivenDyspnoea(cancerNode, dNode)
	numerator = cGd * dNode.marginal
	denom = cancerNode.marginal
	
	dGc = numerator / denom
	
	return dGc
	
def probSmokerGivenCancerandPollution(cancerNode, pollutionNode, smokerNode, dNode):
	numerator = smokerNode.marginal * cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]
	denom = (cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]) + (cancerNode.probabilities["P~S"] * pollutionNode.probabilities["L"] * (1.0 - smokerNode.probabilities["T"]))
	
	sGcp = numerator / denom
	
	return sGcp
	
def probPollutionGivenCancerAndSmoker(cancerNode, xrayNode, pollutionNode, smokerNode):
	
	numerator = cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] * (1.0 - pollutionNode.probabilities["L"])
	denom = cancerNode.probabilities["~PS"] * smokerNode.probabilities["T"] * (1.0 - pollutionNode.probabilities["L"]) + (cancerNode.probabilities["PS"] * smokerNode.probabilities["T"] * pollutionNode.probabilities["L"])
	
	pGcs = numerator/denom
	return pGcs
	
def probPollutionGivenDysAndSmoker(cancerNode, pollutionNode, smokerNode, dNode):
	n1 = dNode.probabilities["C"]*cancerNode.probabilities["~PS"]*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	n2 = dNode.probabilities["~C"]*(1-cancerNode.probabilities["~PS"])*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	d1 = dNode.probabilities["C"]*cancerNode.probabilities["~PS"]*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	d2 = dNode.probabilities["C"]*cancerNode.probabilities["PS"]*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	d3 = dNode.probabilities["~C"]*(1-cancerNode.probabilities["~PS"])*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	d4 = dNode.probabilities["~C"]*(1-cancerNode.probabilities["PS"])*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	
	numerator = n1+n2
	denom = d1+d2+d3+d4
	
	p = numerator/denom
	
	return p
	
def probXrayGivenDysandSmoker(smokerNode, cancerNode, pollutionNode, dNode, xrayNode):
	n1 = xrayNode.probabilities["C"]*dNode.probabilities["C"]*cancerNode.probabilities["~PS"]*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	n2 = xrayNode.probabilities["~C"]*dNode.probabilities["~C"]*(1-cancerNode.probabilities["~PS"])*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]	
	n3 = xrayNode.probabilities["C"]*dNode.probabilities["C"]*cancerNode.probabilities["PS"]*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	n4 = xrayNode.probabilities["~C"]*dNode.probabilities["~C"]*(1-cancerNode.probabilities["PS"])*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	d1 = dNode.probabilities["C"]*cancerNode.probabilities["~PS"]*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]
	d2 = dNode.probabilities["~C"]*(1-cancerNode.probabilities["~PS"])*(1.0 - pollutionNode.probabilities["L"])*smokerNode.probabilities["T"]	
	d3 = dNode.probabilities["C"]*cancerNode.probabilities["PS"]*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]
	d4 = dNode.probabilities["~C"]*(1-cancerNode.probabilities["PS"])*pollutionNode.probabilities["L"]*smokerNode.probabilities["T"]

	num = n1+n2+n3+n4
	den = d1+d2+d3+d4
	
	p = num/den
	
	return p
