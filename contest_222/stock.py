n, k = tuple(map(int, input().split()))

def ans(n, k, s):
	if n == k:
		print(s + "1" * k)
		return
	ans(n - 1, k, s + "0")
	if k > 0:
		ans(n - 1, k - 1, s + "1")

ans(n, k, "")



