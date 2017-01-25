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
		try:
			shell('cp ../submissions_proj3/' + line[:-1] + '/proj3/src/vm/DESIGNDOC ../submissions_proj3/DESIGNDOC/' + line[7:-1] + '_DESIGNDOC', '.')
		except OSError:
			print("Repo " + line[:-1] + " does not follow course directory setup convention. Must grade manually\n")
