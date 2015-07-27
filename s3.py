import sys

def readFile():
	if(len(sys.argv) == 2):
		f = open(sys.argv[1], 'r')
		sArray = [list(line.rstrip('\n')) for line in f]
		return sArray
	else:
		print "\npython s3.py <sudoku input file>\n"

def constructCNF(sArray):

	varCount = 0
	clauseCount = 0

	if sArray:
		for idI, row in enumerate(sArray):
			for idJ, value in enumerate(row):
				if value in ['0', '.', '*', '?']:
					varCount += 9
					clauseCount +=1
					for x in range(9):
						print ((int(idI) * 81) + (int(idJ) * 9) + int(x) + 1),
					print 0

				else:
					varCount += 1
					clauseCount +=1
					print ((int(idI) * 81) + (int(idJ) * 9) + int(value)),
					print 0

		for idI, row in enumerate(sArray):
			for idJ, value in enumerate(row):
				for x in range(8):
					if(idJ < 8):
						clauseCount += 1
						print (-1*((int(idI) * 81) + (int(idJ) * 9) + int(x) + 1)),
						print (-1*((int(idI) * 81) + (int(idJ+1) * 9) + int(x) + 1)),
						print 0

		for idI, row in enumerate(sArray):
			for idJ, value in enumerate(row):
				for x in range(8):
					if(idI < 8):
						clauseCount += 1
						print (-1*((int(idI) * 81) + (int(idJ) * 9) + int(x) + 1)),
						print (-1*((int(idI+1) * 81) + (int(idJ) * 9) + int(x) + 1)),
						print 0

		print "p cnf %s %s" % (varCount, clauseCount)
	else:
		print "sArray not intialized correctly\n"

def main():
	sArray = readFile() # Open sudoku file and parse into array
	constructCNF(sArray)

main()
