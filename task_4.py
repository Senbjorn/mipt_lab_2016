#task_4
n = int(input())
A = list(map(int, input().split()))
A = sorted(A)
s = len(A) // 2
print(sum(A[s:]))