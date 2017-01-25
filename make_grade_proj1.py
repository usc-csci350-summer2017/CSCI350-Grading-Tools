import subprocess
import sys
import os
from time import sleep

CSV_FILENAME = sys.argv[1]

def hint(text, color='34'):
	return '\t\033[{}m{}\033[0m'.format(color, text)

def shell(command, cwd=None):
	if cwd is None:
		print hint('/: ' + command)
	else:
		print hint(cwd + '/: ' + command)

	shell_output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, cwd=cwd)
	return shell_output.communicate()[0]



with open(CSV_FILENAME) as infile:
	for line in infile:
		NAME = line[7:-1]
		PATH = line[:-1]
		try:
			shell('make grade', '../submissions_proj1/' + PATH + '/proj1/src/threads')
			shell('touch GRADE_' + NAME, '../submissions_proj1/GRADE/')
			writefile = open('../submissions_proj1/GRADE/GRADE_' + NAME, 'w');
			try:
				with open('../submissions_proj1/' + PATH + '/proj1/src/threads/build/grade') as gradefile:
					#get to line 29
					counter = 1
					for gradeline in gradefile:
						if (counter == 29):
							writefile.write("\tAlarm Result:")
							writefile.write(gradeline)
						if (counter == 49):
							writefile.write("\tPriority Result:")
							writefile.write(gradeline)
						if (counter == 50):
							break
						counter += 1
			except IOError:
				sleep(0)
		except OSError:
			print("Repo " + PATH + " does not follow course directory setup convention. Must grade manually\n")