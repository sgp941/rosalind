





if __name__ == '__main__':
	with open('rosalind_tree.txt', 'r') as f:
		lines = f.readlines()
	
	n = int(lines.pop(0))
	edges = []
	for line in lines:
		edges.append(line.split())

	nodes = range(1, n+1)
	for i, node in enumerate(nodes):
		if node in edges:
			print('y')
	print(nodes)
	print(edges)