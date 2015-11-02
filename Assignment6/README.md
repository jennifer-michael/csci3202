This folder holds files for Assignment 6 on Bayesian Networks for CSCI3202, Fall 2015.
This program will give correct answers for all calculations given in the table 2.2 specified in the assignment.

Usuage instructions:

Run via command line using flags that include -m (marginal), -g (condition), -j (point), or -p (to change prior values of smoking and pollution).
Arguments for the condition flag -g must be in quotes to avoid the piping issue. 
For example:
python BayesNets_main.py -g"p|ds"
The above command will give the conditional probability that pollution is high given observed dyspnoea and smoking.

Arguments for the other flags do not need quotes.
For example:
python BayesNets_main.py -mc
python BayesNets_main.py -pP.5 -mc
The above commands will print the marginal probability of cancer with default pollution prior of .9 (low) and the marginal probability of cancer with new prior pollution of .5, respectively.


BayesNode.py contains the node construction and the BayesNet construction given inputs.
BayesNets_main.py contains the flag argument parsing and calls the math functions
ProbabilityCalcs.py contains all the math functions.
