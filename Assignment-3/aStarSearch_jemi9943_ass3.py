import math
import sys
 
class MyNode(object):
	 
	def __init__(self, x, y):
		self.x = x
		self.y = y
		 
		self.distFromStart = 0
		self.parent = None
		self.heuristic = None
		self.f = None
		
	def getDistance(self, parent, specialNum, heuristic): 
		self.parent = parent
		parentDistance = abs(parent.x-self.x) + abs(parent.y-self.y)

		#diagonal case
		if(parentDistance == 2):
			self.distFromStart = parent.distFromStart + 14
		elif(parentDistance == 1):
			self.distFromStart = parent.distFromStart + 10
		
                #mountains
		if(specialNum == 1):
			self.distFromStart += 10
		
		#manhatten
		if(heuristic == 'M'):
			self.heuristic = abs(9-self.x)+abs(7-self.y)
		
		#euclidean distance
		else:
			dx = abs(9-self.x)
			dy = abs(7-self.y)
			self.heuristic = 10 * (math.sqrt(dx * dx + dy * dy))
		
		self.f = self.distFromStart + self.heuristic
		
	def compareNodes(self, otherNode, specialNum):
		distToOtherNode = abs(otherNode.x-self.x)+abs(otherNode.y-self.y)
		runningDist = 0
		
		if(distToOtherNode == 2):
			runningDist = otherNode.distFromStart + 14
		elif(distToOtherNode ==1):
			runningDist = otherNode.distFromStart + 10
			
		if(specialNum == 1):
			runningDist += 10
		
		if(runningDist < self.distFromStart):
			self.distFromStart = runningDist
			self.parent = otherNode
			self.f = self.distFromStart + self.heuristic
	
	#helper function	
	def equals(self, diffNode):
		return(self.x == diffNode.x and self.y == diffNode.y)
		 
		 
def aStarSearch(matrix, heuristic):
	opened = []
	closed = [MyNode(-1, -1)]
	start = MyNode(0,0)
	opened.append(start)
	visited = 1
	
	while(not closed[-1].equals(MyNode(9,7)) and len(opened) > 0):
		opened.sort(key = lambda x: x.f)
		curr = opened[0]
		opened.remove(curr)
		closed.append(curr)
		
		for i in range(-1,2):
			for j in range(-1,2):
				xPosition = curr.x+i
				yPosition = curr.y+j
				if(xPosition >= 0 and xPosition <=9 and yPosition >= 0 and yPosition <= 7):
					nextNode = MyNode(xPosition, yPosition)
					notInClosed = True
					for k in closed:
						if k.equals(nextNode):
							notInClosed = False
					if(matrix[xPosition][7-yPosition] != 2 and notInClosed):
						notInOpened = True
						#have we looked at it?
						for l in opened:
							if l.equals(nextNode):
								notInOpened = False
						#if we haven't, we should look at it.
						if notInOpened:
							opened.append(nextNode)
							visited += 1
							nextNode.getDistance(curr, matrix[xPosition][7-yPosition], heuristic) #add heuristc
						#and if we have, we should compare it to our curr node
						else:
							nextNode.compareNodes(curr, matrix[xPosition][7-yPosition])
		
		#What have we accomplished in this pass?
		selected = closed[-1]
		print("Distance: " + `selected.distFromStart` + ". Locations evaluated: " + `visited` + ".\n")
		final = []
		while(selected != None):
			final.insert(0, selected)
			selected = selected.parent
		for i in final:
			print(i.x, i.y)					
if __name__ == '__main__':
	
	myFile = raw_input("Please type 'World1.txt' for World1 and 'World2.txt' for World2: ")
	heuristic = raw_input("Please type 'M' for Manhatten and 'E' for Euclidean: ")
	
	maze = [[],[],[],[],[],[],[],[],[],[]]
	
	with open(myFile) as f:
		for line in f:
			for i, j in enumerate(line.split()):
				maze[i].append(int(j))
				
	aStarSearch(maze, heuristic)
		
						
