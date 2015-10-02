#Jennifer Michael
#October 1, 2015
#Csci 3202: Articial Intelligence
#Assignment 5: Value Iteration
#References: Ian Char

import math
import sys
 
 
UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"
HERE = "*"
NONE = "X"

class MyNode(object):
	 
	def __init__(self, position, obstacle):
		
		#Will get these when matrix of nodes is made
		self.position = position
		self.obstacle = obstacle
		
		#Reward calculation based on obstacle
		if obstacle == 0 or obstacle == 2:
			#Walkable path or wall
			self.reward = 0		
		elif obstacle == 50:
			#Apple
			self.reward = 50
		elif obstacle == 4:
			#Barn
			self.reward = 1
		elif obstacle == 1:
			#Mountain
			self.reward = -1
		elif obstacle == 3:
			#Snake
			self.reward = -2
		
		#Utility and best direction setting if we find the apple
		if obstacle == 50:
			self.bestDir = HERE
			self.utility = 50
		
		#Initilize all nodes to have 0 utility:
		else:
			self.bestDir = NONE
			self.utility = 0
	
	#Getter and setter functions that could be useful	
	
	def getPosition(self):
		return self.position
		
	def getObstacle(self):
		return self.obstacle
	
	def getUtility(self):
		return self.utility
	
	def setUtility(self, utility):
		self.utility = utility
	
	#Used in Bellman equation
	def getReward(self):
		return self.reward
	
	def getBestDir(self):
		return self.bestDir
	
	def setBestDir(self, direction):
		self.bestDir = direction

	def equals(self, diffNode):
		return(self.x == diffNode.x and self.y == diffNode.y)
	
	#What prints when I want to print a MyNode	 
	def __str__(self):
		return (str(self.position) + " has the utility " + str(self.utility))


		
class MDPSearch(object):
	def __init__(self, maze, epsilon):
		self.maze = maze
		self.epsilon = epsilon
		
	def search(self):
	
		delta = float("inf")
		gamma = float(0.9)
	
		#Basic Value Iteration loop to check with epsilon
		while not(delta < self.epsilon * (1-gamma)/gamma):
			delta = -1 * float("inf")
			for row in reversed(self.maze):
				for node in reversed(row):
					possDelta = self.findUtility(node)
					if possDelta > delta:
						delta = possDelta
		
		self.printPath()
		
	
	def findUtility(self,node):

		nodePosition = node.getPosition()
		estimates = []
		gamma = 0.9
	
		#No need to check if its a wall or the apple
		if node.getObstacle() == 2 or node.getObstacle() == 50:
			return
		
		#Node below....
		if nodePosition[1] -1 < 0:
			downUtility = 0
		else:
			downUtility = self.maze[nodePosition[1]-1][nodePosition[0]].getUtility()
		
		#Node to the left.....
		if nodePosition[0] -1 < 0:
			leftUtility = 0
		else:
			leftUtility = self.maze[nodePosition[1]][nodePosition[0]-1].getUtility()
		
		#Node to the right....
		if nodePosition[0] + 1 > 9:
			rightUtility = 0
		else:
			rightUtility = self.maze[nodePosition[1]][nodePosition[0]+1].getUtility()
		
		#Node above.....
		if nodePosition[1] + 1 > 7:
			upUtility = 0
		else:
			upUtility = self.maze[nodePosition[1] + 1][nodePosition[0]].getUtility()
		
		#Calculate all the things and add to a list so we can find the max
		estimates.append(((0.8 * upUtility + 0.1 * leftUtility + 0.1 * rightUtility), UP))
		estimates.append(((0.8 * leftUtility + 0.1 * upUtility + 0.1 * downUtility), LEFT))
		estimates.append(((0.8 * rightUtility + 0.1 * upUtility + 0.1 * downUtility), RIGHT))
		estimates.append(((0.8 * downUtility + 0.1 * leftUtility + 0.1 * rightUtility), DOWN))
		
		#Find the max
		maxExpectedUtility = max(estimates) 
		
		#nodeJs is just a temporary node
		nodeJs = node.getUtility()
		
		#Set the utility of the current node state with Bellman equation
		node.setUtility(float(node.getReward() + gamma * maxExpectedUtility[0]))
		
		#Contains either UP, DOWN, LEFT, or RIGHT. Establishes what the best move
		#in that state is based off the equation
		node.setBestDir(maxExpectedUtility[1])
		
		#Return how much better it is.
		return abs(nodeJs - node.getUtility())

	
	#Method to print the best path as determined by this algorithm			
	def printPath(self):
		print("\n*******************HOW THE HORSE SHOULD GET TO THE APPLE********************")
		x = 0
		y = 0
		curr = self.maze[y][x]
		
		# * means we have found the apple
		while(curr.getBestDir() != '*'):
			print curr
			if curr.getBestDir() == 'U':
				y += 1
			elif curr.getBestDir() == 'D':
				y -= 1
			elif curr.getBestDir() == 'L':
				x -= 1
			if curr.getBestDir() == 'R':
				x += 1

			#Move to the best node
			curr = self.maze[y][x]
			
		print curr
		
		print("\n********************THIS IS THE POLICY FOR THE MAZE**********************")
		policyMatrix = [[node.getBestDir() for node in row]
			for row in reversed(self.maze)]
		for row in policyMatrix:
			print(" ".join(row))
		
		
		
#Creates a maze from from the file name
#As well as what a maze of nodes! 
#The nodeMaze contains nodes with backwards coordinates since we traverse backwards		
def getMaze(fileName):
	maze = []
	f = open(fileName, 'r').readlines()
		
	for line in reversed(f):			
		maze.append(line.split(" "))
		
	nodeMaze = []
	
	for i in range(len(maze)):
		nodeMaze.append([])
		for j in range(len(maze[0])):
			#the int(maze) param is the obstacle
			nodeMaze[i].append(MyNode((j,i), int(maze[i][j])))
	return nodeMaze	 

								
if __name__ == '__main__':
	
	#createMaze = MazeMaker()
	
	myFile = raw_input("Please give me a world to navigate! Please type 'World1MDP.txt': ")
	epsilon = raw_input("Please give me a value of epsilon: ")
	
	maze = getMaze(myFile)
	
	mdp = MDPSearch(maze, float(epsilon))
	mdp.search()
		
						
