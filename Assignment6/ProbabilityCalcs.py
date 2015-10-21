'''
Where all the calculations will be done.
'''

def probCancer(cancerNode, pollutionNode, smokerNode):
	firstOp = cancerNode.probabilities["~PS"] * (1.0 - pollutionNode.probabilities["L"]) * smokerNode.probabilities["T"])
	secondOp = cancerNode.probabilities["~P~S"] * (1.0 - pollutionNode.probabities["L"]) * (1.0 - smokerNode.probabilities["T"])
	thirdOp = cancerNode.probabilities["PS"] * pollutionNode.probabities["L"] * smokerNode.probabilities["T"]
	fourthOp = cancerNode.probabilities["P~S"] * pollutionNode.probabities["L"] * (1.0 - smokerNode.probabilities["T"])
	 
	probOfCancer = firstOp + secondOp + thirdOp + fourthOp
	
	cancerNode.marginal = probOfCancer
	return probOfCancer
	
def probXrayIsTrue(cancerNode, xrayNode):
	firstOp = xrayNode.probabilities["C"] * cancerNode.joint
	secondOp = xrayNode.probabilities["~C"] * (1.0 - cancerNode.joint)
	
	probXrayTrue = firstOp + secondOp
	
	xrayNode.foundValues["X"] = probXrayTrue
	return probXrayTrue
	
def probCancerGivenSmoker(cancerNode, pollutionNode, smokerNode):
	cGivenSNum = cancerNode.probabilities["PS"] * pollutionNode.probabilties["L"] * smokerNode.probabilities["T"] 
				+ cancerNode.probabilities["~PS"] * (1.0-pollutionNode.probabilites["L"]) * smokerNode.probabilites["T"]
	
	cGivenS = cGivenSNum / smokerNode.probabilities["T"]
	
	return cGivenS		
	
def probRootGivenLeaf(rootNode, leafNode):
	
