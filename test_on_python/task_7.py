#task_7
def is_prime(n):
	d = 2
	while d <= n ** 0.5:
		if n % d == 0:
			return False
		d += 1
	return True

def digit_sum(n):
	s = 0
	while n != 0:
		s += n % 10
		n //= 10
	return s

(a, b, k) = tuple(map(int, input().split()))
for i in range(a, b + 1):
	if digit_sum(i) == k:
		if is_prime(i):
			print(i, end = ' ')