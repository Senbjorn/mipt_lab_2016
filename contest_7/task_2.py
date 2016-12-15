#task_2
a = int(input())
print(sum(list(map(int, list((bin(a))[2:])))))