#task_4
price, delta, m = tuple(map(int, input().split()))
day = 1
week = 1
s = 0
while week <= m:
	s += price
	price += delta
	day += 1
	week += 1 if day % 7 == 1 else 0
print(s)