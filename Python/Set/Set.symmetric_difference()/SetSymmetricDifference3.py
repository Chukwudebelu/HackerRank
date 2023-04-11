# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  _,A,_,B = eval("{*input().split()},"*4); print(len(A ^ B))
 
