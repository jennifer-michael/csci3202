import getopt
import argparse
import sys

 #Jennifer Michael
 #Assignment 6: Bayes Nets
 #Due: October 23, 2015

def main():
	getArgs(sys.argv[1:])
	
def handle_p(p):
	p[0].split()
	print(p[0])
	if '=' not in p:
		if p[1] == 'P':
			print(p[2])
			return(float(p[2], .3))
		else:
			return(.9, float(p[1]))
	else:
		if p[0] == 'P' and p[1] == '=':
			return (float(p[2]), .3)
		elif p[0] == 'S' and p[1] == '=':
			return (.9, float(p[2]))
		else:
			print("This is not a valid request")
			
def getArgs(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', nargs='+', default=("P", .9, "S", .3), required=False)
	parser.add_argument('-m', nargs='+', required=False)
	parser.add_argument('-j', nargs='+', required=False)
	parser.add_argument('-g', nargs='+', required=False)
	
	myArgs = parser.parse_args()
	print(myArgs)
	
	
	opts, args = getopt.getopt(argv, 'm:j:p:g:')
	for opt in opts:
		if opt[0] == '-m':
			m = handle_m(myArgs.m)
			
		elif opt[0] == '-j':
			j = handle_j(myArgs.j)

		elif opt[0] == '-p':
			p = handle_p(myArgs.p)
			print(p)

		elif opt[0] == '-g':
			g = handle_g(myArgs.g)



if __name__=='__main__':
	sys.exit(main())
