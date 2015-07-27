import sys

def readFile():
    if(len(sys.argv) == 2):
        f = open(sys.argv[1], 'r')
        sArray = [list(line.rstrip('\n')) for line in f] 
        return sArray
    else:
        print "\npython s3.py <sudoku input file>\n"

def main():
    sArray = readFile() # Open sudoku file and parse into array
    for line in sArray:
        print line

main()
