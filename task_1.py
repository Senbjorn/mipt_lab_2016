#task_1
n = int(input())
dict1 = {}
for i in range(n):
	A = input().split()
	dict1[A[0]] = A[1]
dict2 = {}
for i in range(n):
	A = input().split()
	dict2[A[0]] = A[1]
for key in dict1:
	print(dict1[key], dict2[key])
