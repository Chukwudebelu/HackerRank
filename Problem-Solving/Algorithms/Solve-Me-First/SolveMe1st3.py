import itertools

def solveMeFirst(a,b):
	return list(itertools.accumulate([a,b], lambda x,y: x + y))[-1]

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
