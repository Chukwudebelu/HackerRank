# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import pow

if __name__ == "__main__":
    a, b, m = [int(input().strip()) for _ in range(3)]
    print(int(pow(a, b)), int(divmod(pow(a, b), m)[1]), sep='\n')
