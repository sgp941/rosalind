from __future__ import print_function
import numpy as np


switcher = {
	'A': 0,
	'C': 1,
	'G': 2,
	'T': 3,
	0: 'A',
	1: 'C',
	2: 'G',
	3: 'T'
}


def main():
	f = open('rosalind_cons.txt', 'r')
	lines = f.readlines()

	dna_strings = []
	string = ''
	for line in lines:
		# print(line)
		if line[0] != '>':
			string += line.rstrip('\n')
		else:
			dna_strings.append(string)
			string = ''

	dna_strings.append(string)

	profile = np.zeros((4, len(dna_strings[1])), dtype = int)
	for string in dna_strings:	
		for j, base in enumerate(string):
			i = switcher[ base ]
			profile[i][j] += 1
	# print(profile)

	consensus = ''
	for i in range(len(profile[0])):
		consensus += switcher[ np.argmax( profile[:, i] ) ]

	print(consensus)
	print('A: ', *profile[0], sep=' ')
	print('C: ', *profile[1], sep=' ')
	print('G: ', *profile[2], sep=' ')
	print('T: ', *profile[3], sep=' ')

	# print(len(consensus), len(profile[0]), len(line))



if __name__ == '__main__':
	main()