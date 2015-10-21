 #Class for a Bayes Node
 
class BayesNode:
	'''
	Class that keeps track of all the info a node should have
	'''
	
	def __init__(self, name):
		self.name = name
		self.conditionals = {}
		#self.marginal = 0
		self.probabilities = {}
		self.parents = []
		self.children = []
	
	#Keep track of parents
	def add_parent(self, parent):
		self.parents.append(parent)
	
	#Keep track of children
	def add_child(self, child):
		self.children.append(child)
	
	#Get probability based off parents	
	#This doesn't work at all cuz I suck.

	def set_probability(self, key, value):
		self.probability[key] = value
		
	def __str__(self):
		return (str(self.name))
		
class BayesNet(object):
	'''
	Object that basicially just a dictionary mapping nodes
	'''
	
	def __init__(self):
		self.nodes = {}
	
	def add_node(self, node):
		self.nodes[node.name] = node
			
def create_bayesNet(value1, value2):
	'''
	Creates all the BayesNodes based on the values they have 
	and then creates the actual BayesNet graph 
	'''
	
	#Pollution Node
	pollution = BayesNode("Pollution")
	pollution.set_probability("L", value1)
	
	#Smoker Node
	smoker = BayesNode("Smoker")
	smoker.set_probability("T", value2)
	
	#Cancer Node
	cancer = BayesNode("Cancer")
	cancer.set_probability["~PS"] = .05 #high pollution, smoker
	cancer.set_probability["~P~S"] = .02 #high pollution, nonsmoker
	cancer.set_probability["PS"] = .03 #low pollution, smoker
	cancer.set_probability["P~S"] = .001 #low pollutin, nonsmoker

	#Xray Node
	xray = BayesNode("XRay")
	xray.set_probability(.9)
	xray.set_probability["C"] = .9 #cancer is true
	xray.set_probability["~C"] = .2 #cancer is false
	
	#Dyspnoea Node
	dyspnoea = BayesNode("Dyspnoea")
	dyspnoea.set_probability(.65)
	dyspnoea.set_probability["C"] = .65 #cancer is true
	dyspnoea.set_probability["~C"] = .3 #cancer is false
	
	#Add parents and children to everyone
	cancer.add_parent(pollution)
	cancer.add_parent(smoker)
	xray.add_parent(cancer)
	dyspnoea.add_parent(cancer)
	pollution.add_child(cancer)
	smoker.add_child(cancer)
	cancer.add_child(xray)
	cancer.add_child(dyspnoea)
	
	#Create graph network
	bayesNet = BayesNet()
	bayesNet.add_node(pollution)
	bayesNet.add_node(smoker)
	bayesNet.add_node(cancer)
	bayesNet.add_node(xray)
	bayesNet.add_node(dyspnoea)
	
	return bayesNet

#def set_conditionals():
#something....	

def main():
	create_bayesNet(.9, .3)
	set_conditionals()
	
if __name__ == '__main__':
	main()
