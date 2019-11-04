if __name__ == '__main__':
	with open('rosalind_iev.txt') as f:
		geno = f.read().rstrip('\n').split(' ')
		geno = [int(i) for i in geno]

	print(geno)

	total = sum(geno)
	probs_dom = [1, 1, 1, .75, .5, 0]
	print(sum([2 * probs_dom[i] * g for i, g in enumerate(geno)]))