from random import randint, shuffle

def monkey_sort(A):
	B = sorted(A)
	while B != A:
		shuffle(A)

A = [randint(0, 20) for i in range(5)]
print(*A)
monkey_sort(A)
print(*A)