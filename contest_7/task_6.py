#task_6
(d, s) = tuple(input().split())
print(len([s[i] for i in range(len(s)) if s[i] == d]))