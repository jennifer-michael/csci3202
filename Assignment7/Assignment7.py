 ###############################
 #     Bayes Nets Sampling     #
 #      Jennifer Michael       #
 #      November 1, 2015       #
 #       CSCI 3202 Fall        #
 ###############################
 
'''
References:
http://www.cse.unr.edu/robotics/bekris/cs482_f09/sites/cse.unr.edu.robotics.
bekris.cs482_f09/files/notes_lec15.pdf

Collaborated With:
Jessica Petty - helped fix bug in priorSampling() 

'''

import sys
import Samples

#Number 1

def priorSampling():
	samples = Samples.samples
	sampleSize = len(samples)
	results = []
	cloudy = "~c"
	sprinkling = "~s"
	rain = "~r"
	wetGrass = "~w"
	i = 0
	while i < sampleSize:
		if samples[i] < 0.5:
			cloudy = "c"
		i = i + 1
		if cloudy == "c":
			if samples[i] < 0.1:
				sprinkling = "s"
			if samples[i+1] < 0.8:
				rain = "r"
		else:
			if samples[i] < 0.5:
				sprinkling = "s"
			if samples[i+1] < 0.2:
				rain = "r"
		i = i + 2
		if sprinkling == "s" and rain == "r":
			if samples[i] < 0.99:
				wetGrass = "w"
		elif sprinkling == "s" and rain == "~r":
			if samples[i] < 0.9:
				wetGrass = "w"
		elif sprinkling == "~s" and rain == "r":
			if samples[i] < 0.9:
				wetGrass = "w"
		results.append([cloudy, sprinkling, rain, wetGrass])
		cloudy = "~c"
		sprinkling = "~s"
		rain = "~r"
		wetGrass = "~w"
		i = i + 1
	return results
	
#1a
def prior_cTrue(resultArray):
	totalCTrue = 0.0
	for subarray in resultArray:
		if subarray[0] == "c":
			totalCTrue = totalCTrue + 1.0
	
	prob = totalCTrue / len(resultArray)
	print(("With prior sampling, P(c = true) is: {0}").format(prob))
	
#1b
def prior_cGivenR(resultArray):
	totalCTrue = 0
	totalRTrue = 0
	for subarray in resultArray:
		if subarray[2] == "r":
			totalRTrue = totalRTrue + 1.0
			if subarray[0] == "c":
				totalCTrue = totalCTrue + 1.0
			
	prob = totalCTrue / totalRTrue
	print(("With prior sampling, P(c = true | rain = true) is: {0}").format(prob))
	
#1c
def prior_sGivenW(resultArray):
	totalSTrue = 0
	totalWTrue = 0
	
	for subarray in resultArray:
		if subarray[3] == "w":
			totalWTrue = totalWTrue + 1.0
			if subarray[1] == "s":
				totalSTrue = totalSTrue + 1.0
			
	prob = totalSTrue / totalWTrue
	print(("With prior sampling, P(s = true | w = true) is: {0}").format(prob))

#1d
def prior_sGivenCandW(resultArray):
	totalSTrue = 0.0
	denom = 0.0
	
	for subarray in resultArray:
		if (subarray[0] == "c") and (subarray[3] == "w"):
			denom = denom + 1.0
			if subarray[1] == "s":
				totalSTrue = totalSTrue + 1.0

	prob = totalSTrue / denom
	print(("With prior sampling, P(s = true | c = true, w = true) is: {0}").format(prob))
			
#Number 3

#3a
def rejection_cTrue():
	samples = Samples.samples
	cloudyTrue = 0.0
	
	#Don't even generate samples for other variables
	for number in samples:
		if number < 0.5:
			cloudyTrue += 1.0
			
	prob = cloudyTrue / len(samples)
	print(("With rejection sampling, P(c = true) is: {0}").format(prob))
	
#3b
def rejection_cGivenR():
	samples = Samples.samples
	sampleSize = len(samples)
	cloudy = "~c"
	sprinkling = "~s"
	rain = "~r"
	wetGrass = "~w"
	results = []
	
	i = 0
	while i < sampleSize-1:
		if samples[i] < 0.5:
			cloudy = "c"
		i = i + 1
		if cloudy == "c":
			#get sample for r, since that's what we want
			if samples[i] < 0.8:
				rain = "r"
				i = i + 1
				#complete sample set for s and w
				if samples[i] < 0.1:
					sprinkling = "s"
					i = i + 1
					if samples[i] < 0.99:
						wetGrass = "w"
				else:
					i = i + 1
			else:
				i = i + 1
				continue
		#Continue generating samples for r for all cases of c
		else:
			if samples[i] < 0.2:
				rain = "r"
				i = i + 1
				if samples[i] < 0.5:
					sprinkling = "s"
					i = i + 1
					if samples[i] < 0.99:
						wetGrass = "w"
					i = i + 1
				else:
					i = i + 1
					if samples[i] < 0.9:
						wetGrass = "w"
					i = i + 1
			else:
				i = i + 1
				continue
		results.append([cloudy, sprinkling, rain, wetGrass])
		cloudy = "~c"
		sprinkling = "~s"
		rain = "~r"
		wetGrass = "~w"
			
	totalCTrue = 0
	totalRTrue = 0
	
	for sample in results:
		totalRTrue = totalRTrue + 1.0
		if sample[0] == "c":
			totalCTrue = totalCTrue + 1.0
	
	prob = totalCTrue / totalRTrue
	print(("With rejection sampling, P(c = true | rain = true) is: {0}").format(prob))
	
#3c
def rejection_sGivenW():
	samples = Samples.samples
	sampleSize = len(samples)
	cloudy = "~c"
	sprinkler = "~s"
	rain = "~r"
	results = []
	
	i = 0
	while i < sampleSize-4:
		if samples[i] < 0.5:
			cloudy = "c"
		i = i + 1
		#generate samples for s in both cases of c
		if cloudy == "c":
			if samples[i] < 0.1:
				sprinkler = "s"
			i = i + 1
			if samples[i] < 0.8:
				rain = "r"
			i = i + 1
		else:
			if samples[i] < 0.5:
				sprinkler = "s"
			i = i + 1
			if samples[i] < 0.2:
				rain = "r"
			i = i + 1
		#get only true w samples
		if sprinkler == "s" and rain == "r":
			if samples[i] < 0.99:
				results.append([cloudy, sprinkler, rain, "w"])
		elif sprinkler == "s" and rain == "~r":
			if samples[i] < 0.9:
				results.append([cloudy, sprinkler, rain, "w"])
		elif sprinkler == "~s" and rain == "r":
			if samples[i] < 0.9:
				results.append([cloudy, sprinkler, rain, "w"])
				#we don't even add a sample set to results unless w is true
		i = i + 1
		cloudy = "~c"
		sprinkler = "~s"
		rain = "~r"
		
	totalS = 0.0
	for sample in results:
		if sample[1] == "s":
			totalS = totalS + 1.0		
	prob = totalS / len(results)
	print(("With rejection sampling, P(s = true | w = true) is: {0}").format(prob))

def rejection_sGivenCandW():
	samples = Samples.samples
	sampleSize = len(samples)
	cloudy = "~c"
	sprinkler = "~s"
	rain = "~r"
	wetGrass = "~w"
	results = []
	
	i = 0
	while i < sampleSize - 3:
		if samples[i] < 0.5:
				cloudy = "c"
				i = i + 1
		#we reject if c isn't true
		else:
			i = i + 1
			continue
			
		if samples[i] < 0.1:
			sprinkler = "s"
		i = i + 1
		
		if samples[i] < 0.8:
			rain = "r"
		i = i + 1
		
		#we also reject if w isn't true (by not added sample set to results)
		if (sprinkler == "s") and (rain == "r"):
			if samples[i] < .99:
				results.append([cloudy, sprinkler, rain, "w"])
		elif (rain == "r") and (sprinkler == "~s"):
			if samples[i] < .90:
				results.append([cloudy, sprinkler, rain, "w"])
		elif (rain == "~r") and (sprinkler == "s"):
			if samples[i] < .90:
				results.append([cloudy, sprinkler, rain, "w"]) 
			
		i = i + 1
		cloudy = "~c"
		sprinkler = "~s"
		rain = "~r"
			
	totalS = 0.0
	for sample in results:
		if sample[1] == "s":
			totalS = totalS + 1.0
			
	prob = totalS / len(results)
	print(("With rejection sampling, P(s = true | c = true, w = true) is: {0}").format(prob))				
		

  
if __name__=='__main__':
	stuff = priorSampling()
	
	#All the prior calculations for number 1
	prior_cTrue(stuff)
	prior_cGivenR(stuff)
	prior_sGivenW(stuff)
	prior_sGivenCandW(stuff) #unsure, weird coincidence? 
	
	#All the rejection calculations for number 3
	rejection_cTrue()
	rejection_cGivenR()
	rejection_sGivenW()
	rejection_sGivenCandW() #don't like
			
 
