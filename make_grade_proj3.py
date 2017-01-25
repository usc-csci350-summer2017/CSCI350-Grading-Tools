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
			shell('chmod +x make-grade', '../submissions_proj3/' + PATH + '/proj3/src/tests')
			shell('make grade', '../submissions_proj3/' + PATH + '/proj3/src/vm')
			shell('touch GRADE_' + NAME, '../submissions_proj3/GRADE/')
			writefile = open('../submissions_proj3/GRADE/GRADE_' + NAME, 'w');
			try:
				with open('../submissions_proj3/' + PATH + '/proj3/src/vm/build/grade') as gradefile:

					counter = 1
					for gradeline in gradefile:
						if (counter == 1):
							writefile.write("TOTAL SCORE:")
							writefile.write(gradeline)
						if (counter == 53):
							writefile.write("VM Functionality:")
							writefile.write(gradeline)
						if (counter == 79):
							writefile.write("VM Robustness:")
							writefile.write("\t");
							writefile.write(gradeline)
						if (counter == 136):
							writefile.write("USERPROG Functionality:")
							writefile.write(gradeline)
						if (counter == 189):
							writefile.write("USERPROG Robustness:")
							writefile.write(gradeline)
						if (counter == 213):
							writefile.write("FILESYS Functionality:")
							writefile.write(gradeline)
						counter += 1
			except IOError:
				sleep(0)
		except OSError:
			print("Repo " + PATH + " does not follow course directory setup convention. Must grade manually\n")