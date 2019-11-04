import numpy as np

def main():
	f = open('rosalind_kmp.txt', 'r')
	lines = f.readlines()

	text = ''
	fail = [0]
	for line in lines[1:]:
		text += line.rstrip('\n')

	# print( *text, sep='  ')
	i = 1
	lon = 0
	while i < len(text):
		if text[i-lon:i+1] == text[:lon+1]:
			lon += 1
			fail.append(lon)
			i += 1
		elif lon != 0:
			lon -= 1
		else:
			fail.append(0)
			lon = 0
			i += 1

	f.close()
	f = open('out.txt', 'w')
	writer = f.write(' '.join(str(i) for i in fail))







if __name__ == '__main__':
	main()