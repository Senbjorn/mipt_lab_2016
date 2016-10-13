#task_3
n = int(input())
A = list(map(int, input().split()))
even = 0
e_ind = 0
a = True
odd = 0
o_ind = 0
b = True
for i in range(len(A)):
	if a and A[i] % 2 == 0:
		a = False
		e_ind = i
		even = A[i]
	if b and A[i] % 2 == 1:
		b = False
		o_ind = i
		odd = A[i]
	if A[i] % 2 == 0 and A[i] < even:
		even = A[i]
		e_ind = i
	if A[i] % 2 == 1 and A[i] > odd:
		odd = A[i]
		o_ind = i
if not (b or a):
	A[e_ind], A[o_ind] = A[o_ind], A[e_ind]
print(*A)
