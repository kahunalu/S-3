from subprocess import call, check_output
import subprocess
import time
import re

f = open('input3.txt', 'w')
puz = open('hardPuzzles.txt', 'r')

average = 0
maximum = 0

for puzzle in range(50):
	for index, line in enumerate(puz.readlines()):
		f.write(line)

		call(["python", "s3.py", "input3.txt", "-cnf", "9"])
		time.sleep(0.1)

		p = subprocess.Popen("../../Downloads/minisat/core/minisat input.in output.out", stdout=subprocess.PIPE, shell=True)
		result = p.communicate()[0].strip()
		x = result.find('CPU time              :')
		m = re.search('[-+]?([0-9]*\.[0-9]+|[0-9]+)', result[x+24:x+30])
		if m:
		    found = m.group(1)

		found = float(found)

		if found > maximum:
			maximum = found

		average += found

		time.sleep(0.1)

		f = open('input3.txt', 'w')

print "Average time taken %s" %(average/95)
print "Maximum time taken %s" %(maximum)
