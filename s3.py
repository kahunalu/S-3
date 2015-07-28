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
			result = ((int(value)%81)%9)
			if result == 0:
				print 9,
			else:
				print result,

			if x % 9 == 0:
				print ""
	print "\n"


def constructCNF(sArray):

	varCount = 0
	clauseCount = 0

	if sArray:
		for i, line in enumerate(sArray):
			for j, value in enumerate(line):
				if value not in ['0', '.', '*', '?']:
					clauseCount += 1
					print (((i)*81)+((j)*9)+int(value)),
					print 0

		for i in range(9):
			i += 1
			for j in range(9):
				j += 1
				for k in range(9):
					k += 1
					print (((i-1)*81)+((j-1)*9)+k),
				clauseCount += 1
				print 0

		for i in range(9):
			i += 1
			for k in range(9):
				k += 1
				for j in range(8):
					j += 1
					l = j + 1
					while l <= 9:
						clauseCount += 1
						print (-1*(((i-1)*81)+((j-1)*9)+k)),
						print (-1*(((i-1)*81)+((l-1)*9)+k)),
						print 0
						l +=1

		for j in range(9):
			j += 1
			for k in range(9):
				k += 1
				for i in range(8):
					i += 1
					l = i + 1
					while l <= 9:
						clauseCount += 1
						print (-1*(((i-1)*81)+((j-1)*9)+k)),
						print (-1*(((l-1)*81)+((j-1)*9)+k)),
						print 0
						l +=1

		for k in range(9):
			k +=1
			for a in range(3):
				for b in range(3):				
					for u in range (3):
						u +=1
						for v in range(2):
							v += 1
							w = v + 1
							while w <= 3:
								clauseCount += 1
								print (-1*((((3*a)+u-1) * 81) + (((3*b)+v-1) * 9) + k)),
								print (-1*((((3*a)+u-1) * 81) + (((3*b)+w-1) * 9) + k)),
								print 0
								w +=1

		for k in range(9):
			k +=1
			for a in range(3):
				for b in range(3):			
					for u in range (2):
						u += 1
						for v in range(3):
							v += 1
							w = u + 1
							while w <= 3:
								for t in range(3):
									t += 1
									clauseCount += 1
									print (-1*((((3*a)+u-1) * 81) + (((3*b)+v-1) * 9) + k)),
									print (-1*((((3*a)+w-1) * 81) + (((3*b)+t-1) * 9) + k)),
									print 0
								w +=1

		print "p cnf 729 %s" %  clauseCount
	else:
		print "sArray not intialized correctly\n"

def main():
	if(sys.argv[1] == 'input.txt'):
		sArray = readFile() # Open sudoku file and parse into array
		constructCNF(sArray)
	elif(sys.argv[1] == 'output.out'):
		parseSolution()

main()
