import sys

extended = False
nk = 16

def readFile():
	global nk
	if(len(sys.argv) >= 2):
		f = open(sys.argv[1], 'r')
		sArray = []
		length = len(f.readlines())

		if length >= nk:
			f = open(sys.argv[1], 'r')
			sArray = [list(line.rstrip('\n')) for line in f]
		else:
			f = open(sys.argv[1], 'r')
			suList = f.readlines()
			string = suList[0]
			for i in range(nk):
				sArray.append(list(string[(nk*i):(nk*(i+1))]))
		
		if nk == 16:
			for i, line in enumerate(sArray):
				for j, value in enumerate(line):
					if value not in ['0', '.', '*', '?']:
						sArray[i][j] = int(value, nk)
				

		return sArray
	else:
		print "\npython s3.py <sudoku input file>\n"

def parseSolution():
	global nk

	f = open(sys.argv[1], 'r')
	sArray = [line for line in f]
	solution = sArray[1].split()

	print ""
	x = 0
	for index, value in enumerate(solution):
		if int(value) > 0:
			x += 1
			result = ((int(value)%(nk*nk))%nk)
			if result == 0:
				if nk == 16:
					print hex(nk),
				else:
					print nk,
			else:
				if nk == 16:
					print hex(result),
				else:	
					print result,

			if x % nk == 0:
				print ""

	print ""

def constructCNF(sArray):
	global nk
	varCount = 0
	unitCount = 0

	f = open('input.in', 'w')

	if sArray:
		
		for i, line in enumerate(sArray):
			for j, value in enumerate(line):
				if value not in ['0', '.', '*', '?']:
					unitCount += 1

		if(extended):
			f.write("p cnf %s %s\n" % ((nk*nk*nk), unitCount+11988))
		elif nk == 16:
			f.write("p cnf %s %s\n" % ((nk*nk*nk), unitCount+86272))
		else:
			f.write("p cnf %s %s\n" % ((nk*nk*nk), unitCount+8829))


		for i, line in enumerate(sArray):
			for j, value in enumerate(line):
				if value not in ['0', '.', '*', '?']:
					f.write(str((((i)*(nk*nk))+((j)*nk)+int(value))))
					f.write(" 0\n")

		for i in range(nk):
			i += 1
			for j in range(nk):
				j += 1
				for k in range(nk):
					k += 1
					f.write(str((((i-1)*(nk*nk))+((j-1)*nk)+k))+" ")
				f.write("0\n")

		for i in range(nk):
			i += 1
			for k in range(nk):
				k += 1
				for j in range(nk-1):
					j += 1
					l = j + 1
					while l <= nk:
						f.write(str((-1*(((i-1)*(nk*nk))+((j-1)*nk)+k)))+" ")
						f.write(str((-1*(((i-1)*(nk*nk))+((l-1)*nk)+k)))+" ")
						f.write("0\n")
						l +=1

		for j in range(nk):
			j += 1
			for k in range(nk):
				k += 1
				for i in range(nk-1):
					i += 1
					l = i + 1
					while l <= nk:
						f.write(str((-1*(((i-1)*(nk*nk))+((j-1)*nk)+k)))+" ")
						f.write(str((-1*(((l-1)*(nk*nk))+((j-1)*nk)+k)))+" ")
						f.write("0\n")
						l +=1

		for k in range(nk):
			k +=1
			for a in range(int(nk ** 0.5)):
				for b in range(int(nk ** 0.5)):				
					for u in range (int(nk ** 0.5)):
						u +=1
						for v in range((int(nk ** 0.5)-1)):
							v += 1
							w = v + 1
							while w <= int(nk ** 0.5):
								f.write(str((-1*((((int(nk ** 0.5)*a)+u-1) * (nk*nk)) + (((int(nk ** 0.5)*b)+v-1) * nk) + k)))+" ")
								f.write(str((-1*((((int(nk ** 0.5)*a)+u-1) * (nk*nk)) + (((int(nk ** 0.5)*b)+w-1) * nk) + k)))+" ")
								f.write("0\n")
								w +=1

		for k in range(nk):
			k +=1
			for a in range(int(nk ** 0.5)):
				for b in range(int(nk ** 0.5)):			
					for u in range (int(nk ** 0.5)-1):
						u += 1
						for v in range(int(nk ** 0.5)-1):
							v += 1
							w = u + 1
							while w <= int(nk ** 0.5):
								for t in range(int(nk ** 0.5)):
									t += 1
									f.write(str((-1*((((int(nk ** 0.5)*a)+u-1) * (nk*nk)) + (((int(nk ** 0.5)*b)+v-1) * nk) + k)))+" ")
									f.write(str((-1*((((int(nk ** 0.5)*a)+w-1) * (nk*nk)) + (((int(nk ** 0.5)*b)+t-1) * nk) + k)))+" ")
									f.write("0\n")
								w +=1
		if(extended):
			extendedEncoding(f)

	else:
		print "sArray not intialized correctly\n"

def extendedEncoding(f):
	global nk

	for x in range(9):
		x += 1
		for y in range(9):
			y += 1
			for z in range(8):
				z += 1
				i = z+1
				while i <= 9:
					f.write(str(-1*(((x-1) * 81) + ((y-1) * 9) + z))+" ")
					f.write(str(-1*(((x-1) * 81) + ((y-1) * 9) + i))+" ")
					f.write("0\n")
					i +=1

	for y in range(9):
		y += 1
		for z in range(9):
			z += 1
			for x in range(9):
				x += 1
				f.write(str(((x-1) * 81) + ((y-1) * 9) + z)+" ")
			f.write("0\n")

	for x in range(9):
		x += 1
		for z in range(9):
			z += 1
			for y in range(9):
				y += 1
				f.write(str(((x-1) * 81) + ((y-1) * 9) + z)+" ")
			f.write("0\n")

	
	for z in range(9):
		z += 1
		for i in range(3):
			for j in range(3):
				for x in range(3):
					x += 1
					for y in range(3):
						y += 1
						f.write(str((((3*i)+x-1) * 81) + (((3*j)+y-1) * 9) + z)+" ")
		f.write("0\n")

def main():
	global nk
	if(len(sys.argv) == 4):
		nk = int(sys.argv[3])

	if(len(sys.argv) == 5):
		nk = int(sys.argv[4])
		if(sys.argv[3] == '-ex'):
			global extended
			extended = True

	if(sys.argv[2] == '-cnf'):
		sArray = readFile() # Open sudoku file and parse into array
		constructCNF(sArray)
	elif(sys.argv[2] == '-slv'):
		parseSolution()

main()
