

def main():
	f = open('rosalind_gc.txt', 'r')
	text = f.readlines()

	labels = []
	gc_count = []
	length = []
	count = 0
	char = 0
	for line in text:
		if line[0] == '>':
			gc_count.append(count)
			length.append(char)
			labels.append(line[1:-1])
			count = 0
			char = 0
		else:
			count += line.count('C')
			count += line.count('G')
			char += len(line) - line.count('\n')
	gc_count.append(count)
	length.append(char)
			
	gc_content = []
	for label in labels:
		i = labels.index(label) + 1
		gc_content.append( round( float(gc_count[i]) / float(length[i]) * 100, 7) )

	# print(gc_content)
	# print(labels)
	i = gc_content.index(max(gc_content))
	print( labels[i] )
	print( gc_content[i] )


if __name__ == '__main__':
	main()