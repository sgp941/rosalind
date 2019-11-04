from __future__ import print_function
import math

def find_base_probs( gc_content ):
	p_g = gc_content / 2
	p_c = p_g
	p_a = (1 - gc_content) / 2
	p_t = p_a
	return p_a, p_c, p_g, p_t


def find_string_probs( string, base_probs ):
	switcher = {'A':base_probs[0], 'C':base_probs[1], 'G':base_probs[2], 'T':base_probs[3]}
	probs = 1
	for base in string:
		probs *= switcher[base]
	return round(math.log(probs, 10), 4)


def main():
	f = open('rosalind_prob.txt', 'r')
	lines = f.readlines()
	dna_string = lines[0].rstrip('\n')
	gc_contents = lines[1].split()
	print(dna_string)
	print(gc_contents)

	final_probs = []
	for gc in gc_contents:
		final_probs.append(find_string_probs( dna_string, find_base_probs( float(gc) ) ))

	print(*final_probs, sep=' ')


if __name__ == '__main__':
	main()