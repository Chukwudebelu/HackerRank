# Enter your code here. Read input from STDIN. Print output to STDOUT
A, B = input().split(), input().split()
[print((int(i),int(j)), end=' ') for i in A for j in B]
