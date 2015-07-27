import sys

def readFile():
	if(len(sys.argv) == 2):
		f = open(sys.argv[1], 'r')
		sArray = [list(line.rstrip('\n')) for line in f]
		return sArray
	else:
		print "\npython s3.py <sudoku input file>\n"

def parseSolution():
	f = open(sys.argv[1], 'r')
	sArray = [line for line in f]
	solution = sArray[1].split()
	print "\n"
	x = 0
	for index, value in enumerate(solution):
		if int(value) > 0:
			x += 1
			print (((int(value)))),
			if x % 9 == 0:
				print ""
	print "\n"


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
					for y in range(8):
						y += 1
						if(idJ+y < 9 and idJ < 8):
							clauseCount += 1
							print (-1*((int(idI) * 81) + (int(idJ) * 9) + int(x) + 1)),
							print (-1*((int(idI) * 81) + (int(idJ+y) * 9) + int(x) + 1)),
							print 0

		for idI, row in enumerate(sArray):
			for idJ, value in enumerate(row):
				for x in range(8):
					for y in range(8):
						y += 1
						if(idI+y < 9 and idI < 8):
							clauseCount += 1
							print (-1*((int(idI) * 81) + (int(idJ) * 9) + int(x) + 1)),
							print (-1*((int(idI+y) * 81) + (int(idJ) * 9) + int(x) + 1)),
							print 0

		print "p cnf %s %s" % (varCount, clauseCount)
	else:
		print "sArray not intialized correctly\n"

def main():
	if(sys.argv[1] == 'input.txt'):
		sArray = readFile() # Open sudoku file and parse into array
		constructCNF(sArray)
	elif(sys.argv[1] == 'output.out'):
		parseSolution()

main()
