def main():
	months = 84
	life = 19

	t = 1
	f = [0] * life
	f[0] = 1

	while t < months:
		new = sum(f[1:])
		for i in reversed(range(1,life)):
			f[i] = f[i - 1]
		f[0] = new
		t += 1
	print(sum(f))


if __name__ == '__main__':
	main()