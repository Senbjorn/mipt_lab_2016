#task_E
a = int(input())
(m_1, m_2) = (0, 0)
while a != 0:
	if a > m_1:
		(m_1, m_2) = (a, m_1)
	elif a != m_1 and m_2 < a:
		m_2 = a
	a = int(input())
print(m_2)