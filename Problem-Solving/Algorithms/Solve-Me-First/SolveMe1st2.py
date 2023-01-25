from functools import reduce as r

def solveMeFirst(a,b):
	return r(lambda x, y: x + y, [a,b])

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
