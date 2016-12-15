#task_1
(a, b) = tuple(input().split())
print((hex(int(a, base = 16) ^ int(b, base = 16)))[2:])