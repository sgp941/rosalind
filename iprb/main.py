
def main():
	k = 30
	m = 23
	n = 18
	total = sum([k,m,n])
	p_k = k / total
	p_m = m / total
	p_n = n / total
	# p_k_k = p_k * (k-1) / (total-1)
	# p_k_m = p_k * m / (total-1)
	# p_k_n = p_k * n / (total-1)
	p_m_m = p_m * (m-1) / (total-1)
	p_m_n = p_m * n / (total-1)
	# p_m_k = p_m * k / (total-1)
	p_n_n = p_n * (n-1) / (total-1)
	p_n_m = p_n * m / (total-1)
	# p_n_k = p_n * k / (total-1)

	prob = 1 - 0.5*(p_m_n + p_n_m) - 0.25*p_m_m - p_n_n

	print(prob)


if __name__ == '__main__':
	main()