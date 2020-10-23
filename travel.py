from collections import deque
class Node:
	def __init__(self, val):
		self.val = val
		self.child = []

def helper(nodes, i):
	q = deque([i])
	seen = set()
	while q:
		t = q.popleft()
		seen.add(t)
		for ch in t.child:
			if ch not in seen:
				q.append(ch)
	
	return list(seen)
	
t = int(input())
pp = 1
while t>0:
	n = int(input())
	inc = input()
	out = input()
	nodes = [Node(i) for i in range(n)]
	for i in range(1, n):
		if inc[i] == out[i-1] == 'Y':
			nodes[i-1].child.append(nodes[i])
		if inc[i-1] == out[i] == 'Y':
			nodes[i].child.append(nodes[i-1])
	print ('Case #'+str(pp)+': ')
	for i in range(n):
		op = helper(nodes, nodes[i])
		l = ['N']*n
		for o in op:
			l[o.val] = 'Y'
		print (''.join(l))
	pp+=1
	t-=1
