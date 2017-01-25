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
			shell('chmod +x make-grade', '../submissions_proj4/' + PATH + '/proj4/src/tests')
			shell('make grade', '../submissions_proj4/' + PATH + '/proj4/src/filesys')
			shell('touch GRADE_' + NAME, '../submissions_proj4/GRADE/')
			writefile = open('../submissions_proj4/GRADE/GRADE_' + NAME, 'w');
			try:
				with open('../submissions_proj4/' + PATH + '/proj4/src/filesys/build/grade') as gradefile:

					counter = 1
					for gradeline in gradefile:
						if (counter == 1):
							writefile.write("TOTAL SCORE:")
							writefile.write(gradeline)
						if (counter == 50):
							writefile.write("Filesys Functionality:")
							writefile.write(gradeline)
						if (counter == 64):
							writefile.write("Filesys Robustness:")
							writefile.write("\t");
							writefile.write(gradeline)
						if (counter == 93):
							writefile.write("Filesys Persistence:")
							writefile.write(gradeline)
						if (counter == 117):
							writefile.write("Base Filesys Robustness:")
							writefile.write(gradeline)
						if (counter == 174):
							writefile.write("Syscall Functionality:")
							writefile.write(gradeline)
						if (counter == 227):
							writefile.write("Syscall Robustness:")
							writefile.write(gradeline)

						counter += 1
			except IOError:
				sleep(0)
		except OSError:
			print("Repo " + PATH + " does not follow course directory setup convention. Must grade manually\n")




			