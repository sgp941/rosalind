import numpy as np


def longest_common( string1, string2 ):
	n = len(string1)
	m = len(string2)
	matches = np.zeros( (m + 1, n + 1))
	for i, s1 in enumerate(string1):
		for j, s2 in enumerate(string2):
			if s1 == s2:
				count = matches[i, j]
				matches[i+1, j+1] = count + 1
	
	print(matches)

if __name__ == '__main__':
	with open('rosalind_lcsm.txt') as f:
		lines = f.readlines()
		string = ''
		strings = []
		for line in lines:
			if line[0] != '>':
				string += line.rstrip('\n')
			else:
				strings.append(string)
				string = ''
		strings.append(string)
		strings.pop(0)

	print(strings)
	longest_common(strings[0], strings[1])
