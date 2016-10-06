#task_1
A = input().split()
print(' '.join(A[::2]))
B = list(map(int, A))
print(max(A), A.index(max(A)))
print(' '.join(B[::-1]))