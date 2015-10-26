 #Class for a Bayes Node
 
class BayesNode:
	'''
	Class that keeps track of all the info a node should have
	'''
	
	def __init__(self, name):
		self.name = name
		self.marginal = 0
		self.probabilities = {} #maybe change name to conditionals
	
	def set_probability(self, key, value):
		self.probabilities[key] = value
		
	def get_marginal(self):
		return self.marginal
		
	def __str__(self):
		return (str(self.name))
		
class BayesNet(object):
	'''
	Object that basicially just a dictionary mapping nodes
	'''
	
	def __init__(self):
		self.nodes = {}
		self.results = {}
	
	def add_node(self, node):
		self.nodes[node.name] = node
		
	#def get_marginal(self, nodeName):
		
		
				
def create_bayesNet(value1, value2):
	'''
	Creates all the BayesNodes based on the values they have 
	and then creates the actual BayesNet graph 
	'''
	
	#Pollution Node
	pollution = BayesNode("Pollution")
	pollution.set_probability("L", (value1))
	pollution.marginal = (value1)
	
	#Smoker Node
	smoker = BayesNode("Smoker")
	smoker.set_probability("T", value2)
	smoker.marginal = value2
	
	#Cancer Node
	cancer = BayesNode("Cancer")
	cancer.set_probability("~PS",.05) #high pollution, smoker
	cancer.set_probability("~P~S", .02) #high pollution, nonsmoker
	cancer.set_probability("PS", .03) #low pollution, smoker
	cancer.set_probability("P~S", .001) #low pollutin, nonsmoker
	cancer.marginal = marginal_cancer(cancer, pollution, smoker)
	#print(cancer.marginal)

	#Xray Node
	xray = BayesNode("XRay")
	xray.set_probability("C",.9 )#cancer is true
	xray.set_probability("~C", .2) #cancer is false
	xray.marginal = marginal_xRay(cancer, xray)
	#print(xray.marginal)
	
	#Dyspnoea Node
	dyspnoea = BayesNode("Dyspnoea")
	dyspnoea.set_probability("C",.65) #cancer is true
	dyspnoea.set_probability("~C", .3) #cancer is false
	dyspnoea.marginal = marginal_dyspnoea(cancer, dyspnoea)
	#print(dyspnoea.marginal)
	
	
	#Create graph network
	bayesNet = BayesNet()
	bayesNet.add_node(pollution)
	bayesNet.add_node(smoker)
	bayesNet.add_node(cancer)
	bayesNet.add_node(xray)
	bayesNet.add_node(dyspnoea)
	
	return bayesNet

def marginal_cancer(cancerNode, pollutionNode, smokerNode):
	firstOp = (cancerNode.probabilities["~PS"]) * (1.0 - pollutionNode.probabilities["L"]) * (smokerNode.probabilities["T"])
	secondOp = cancerNode.probabilities["~P~S"] * (1.0 - pollutionNode.probabilities["L"]) * (1.0 - smokerNode.probabilities["T"])
	thirdOp = cancerNode.probabilities["PS"] * pollutionNode.probabilities["L"] * smokerNode.probabilities["T"]
	fourthOp = cancerNode.probabilities["P~S"] * pollutionNode.probabilities["L"] * (1.0 - smokerNode.probabilities["T"])
	 
	probOfCancer = firstOp + secondOp + thirdOp + fourthOp
	
	cancerNode.marginal = probOfCancer
	return(probOfCancer)
	
def marginal_dyspnoea(cancerNode, dyspnoeaNode):
	
	firstOp = dyspnoeaNode.probabilities["C"] * cancerNode.marginal
	secondOp = dyspnoeaNode.probabilities["~C"] * (1.0 - cancerNode.marginal)
	
	probDysIsTrue = firstOp + secondOp
	
	dyspnoeaNode.marginal = probDysIsTrue
	#self.results["marg_d"] = probDysIsTrue
	return(probDysIsTrue)
	
def marginal_xRay(cancerNode, xrayNode):

	firstOp = xrayNode.probabilities["C"] * cancerNode.marginal
	secondOp = xrayNode.probabilities["~C"] * (1.0 - cancerNode.marginal)
	
	probXrayTrue = firstOp + secondOp
	
	#self.results["marg_x"] = probXrayTrue
	xrayNode.marginal = probXrayTrue
	return(probXrayTrue)

def main():
	bn = create_bayesNet(.9, .3)
	
	
if __name__ == '__main__':
	main()
